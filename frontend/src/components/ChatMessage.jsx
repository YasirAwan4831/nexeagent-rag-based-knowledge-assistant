import { motion } from 'framer-motion'
import { Bot, User, FileText } from 'lucide-react'

export default function ChatMessage({ message }) {
  const isUser = message.role === 'user'

  return (
    <motion.div
      initial={{ opacity: 0, y: 10 }}
      animate={{ opacity: 1, y: 0 }}
      className={`flex items-start gap-3 ${isUser ? 'flex-row-reverse' : ''}`}
    >
      <div
        className={`flex h-8 w-8 shrink-0 items-center justify-center rounded-lg ${
          isUser
            ? 'bg-slate-200 dark:bg-slate-700'
            : 'bg-brand-500/10'
        }`}
      >
        {isUser ? (
          <User className="h-4 w-4 text-slate-600 dark:text-slate-300" />
        ) : (
          <Bot className="h-4 w-4 text-brand-500" />
        )}
      </div>

      <div
        className={`max-w-[75%] rounded-2xl px-4 py-3 ${
          isUser
            ? 'rounded-tr-sm bg-brand-500 text-white'
            : 'rounded-tl-sm bg-slate-100 dark:bg-slate-800'
        }`}
      >
        <p className="whitespace-pre-wrap text-sm leading-relaxed">{message.content}</p>

        {message.sources?.length > 0 && (
          <div className="mt-3 space-y-1 border-t border-slate-200/50 pt-2 dark:border-slate-700/50">
            <p className="text-xs font-medium text-slate-500">Sources:</p>
            {message.sources.map((src, i) => (
              <div
                key={i}
                className="flex items-center gap-1.5 text-xs text-slate-500 dark:text-slate-400"
              >
                <FileText className="h-3 w-3" />
                <span>{src.filename}</span>
                <span className="text-brand-500">
                  ({Math.round((src.similarity || 0) * 100)}% match)
                </span>
              </div>
            ))}
          </div>
        )}
      </div>
    </motion.div>
  )
}
