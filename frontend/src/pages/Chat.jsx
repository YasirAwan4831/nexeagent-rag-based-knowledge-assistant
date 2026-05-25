import { useEffect, useRef, useState } from 'react'
import { motion } from 'framer-motion'
import { Send, Plus, Trash2, Sparkles } from 'lucide-react'
import { api } from '../services/api'
import ChatMessage from '../components/ChatMessage'
import TypingIndicator from '../components/TypingIndicator'

export default function Chat() {
  const [messages, setMessages] = useState([])
  const [input, setInput] = useState('')
  const [sessionId, setSessionId] = useState(null)
  const [sessions, setSessions] = useState([])
  const [loading, setLoading] = useState(false)
  const [useRag, setUseRag] = useState(true)
  const messagesEndRef = useRef(null)

  useEffect(() => {
    loadSessions()
  }, [])

  useEffect(() => {
    messagesEndRef.current?.scrollIntoView({ behavior: 'smooth' })
  }, [messages, loading])

  const loadSessions = async () => {
    try {
      const data = await api.listSessions()
      setSessions(data.sessions || [])
    } catch {
      /* ignore */
    }
  }

  const loadSession = async (id) => {
    try {
      const data = await api.getSession(id)
      setSessionId(data.session_id)
      setMessages(data.messages || [])
    } catch {
      /* ignore */
    }
  }

  const newChat = () => {
    setSessionId(null)
    setMessages([])
  }

  const deleteSession = async (id, e) => {
    e.stopPropagation()
    try {
      await api.deleteSession(id)
      if (sessionId === id) newChat()
      loadSessions()
    } catch {
      /* ignore */
    }
  }

  const sendMessage = async (e) => {
    e.preventDefault()
    if (!input.trim() || loading) return

    const userMessage = { role: 'user', content: input.trim() }
    setMessages((prev) => [...prev, userMessage])
    setInput('')
    setLoading(true)

    try {
      const response = await api.chat(userMessage.content, sessionId, useRag)
      setSessionId(response.session_id)
      setMessages((prev) => [
        ...prev,
        {
          role: 'assistant',
          content: response.answer,
          sources: response.sources,
        },
      ])
      loadSessions()
    } catch (err) {
      setMessages((prev) => [
        ...prev,
        {
          role: 'assistant',
          content: `Error: ${err.message}. Please ensure the backend is running and GEMINI_API_KEY is configured.`,
        },
      ])
    } finally {
      setLoading(false)
    }
  }

  return (
    <div className="flex h-[calc(100vh-4rem)] gap-6">
      <div className="glass w-64 shrink-0 rounded-2xl p-4">
        <button
          onClick={newChat}
          className="mb-4 flex w-full items-center justify-center gap-2 rounded-xl bg-brand-500 px-4 py-2.5 text-sm font-medium text-white hover:bg-brand-600"
        >
          <Plus className="h-4 w-4" /> New Chat
        </button>
        <div className="space-y-1 overflow-y-auto max-h-[calc(100vh-12rem)]">
          {sessions.map((s) => (
            <button
              key={s.session_id}
              onClick={() => loadSession(s.session_id)}
              className={`group flex w-full items-center justify-between rounded-lg px-3 py-2 text-left text-sm transition-colors ${
                sessionId === s.session_id
                  ? 'bg-brand-500/10 text-brand-600 dark:text-brand-400'
                  : 'hover:bg-slate-100 dark:hover:bg-slate-800'
              }`}
            >
              <span className="truncate">{s.title}</span>
              <Trash2
                className="h-3.5 w-3.5 shrink-0 opacity-0 group-hover:opacity-100 text-red-400"
                onClick={(e) => deleteSession(s.session_id, e)}
              />
            </button>
          ))}
        </div>
      </div>

      <div className="flex flex-1 flex-col glass rounded-2xl">
        <div className="flex items-center justify-between border-b border-slate-200/50 px-6 py-4 dark:border-slate-700/50">
          <div className="flex items-center gap-2">
            <Sparkles className="h-5 w-5 text-brand-500" />
            <h2 className="font-display text-lg font-semibold">AI Knowledge Chat</h2>
          </div>
          <label className="flex items-center gap-2 text-sm text-slate-500">
            <input
              type="checkbox"
              checked={useRag}
              onChange={(e) => setUseRag(e.target.checked)}
              className="rounded border-slate-300 text-brand-500 focus:ring-brand-500"
            />
            Use RAG Context
          </label>
        </div>

        <div className="flex-1 space-y-4 overflow-y-auto p-6">
          {messages.length === 0 && (
            <motion.div
              initial={{ opacity: 0 }}
              animate={{ opacity: 1 }}
              className="flex h-full flex-col items-center justify-center text-center"
            >
              <Sparkles className="mb-4 h-12 w-12 text-brand-500/50" />
              <h3 className="text-lg font-medium text-slate-700 dark:text-slate-200">
                Ask anything about your company documents
              </h3>
              <p className="mt-1 max-w-md text-sm text-slate-500">
                Upload documents first, then ask questions. The AI will search your
                knowledge base and provide contextual answers.
              </p>
            </motion.div>
          )}

          {messages.map((msg, i) => (
            <ChatMessage key={i} message={msg} />
          ))}

          {loading && <TypingIndicator />}
          <div ref={messagesEndRef} />
        </div>

        <form
          onSubmit={sendMessage}
          className="border-t border-slate-200/50 p-4 dark:border-slate-700/50"
        >
          <div className="flex gap-3">
            <input
              type="text"
              value={input}
              onChange={(e) => setInput(e.target.value)}
              placeholder="Ask a question about your documents..."
              className="flex-1 rounded-xl border border-slate-200 bg-white px-4 py-3 text-sm outline-none transition-colors focus:border-brand-500 dark:border-slate-700 dark:bg-slate-800 dark:focus:border-brand-400"
              disabled={loading}
            />
            <button
              type="submit"
              disabled={loading || !input.trim()}
              className="flex items-center justify-center rounded-xl bg-brand-500 px-5 text-white transition-colors hover:bg-brand-600 disabled:opacity-50"
            >
              <Send className="h-5 w-5" />
            </button>
          </div>
        </form>
      </div>
    </div>
  )
}
