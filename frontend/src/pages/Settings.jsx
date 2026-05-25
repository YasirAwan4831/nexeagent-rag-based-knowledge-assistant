import { useEffect, useState } from 'react'
import { motion } from 'framer-motion'
import { Settings as SettingsIcon, Key, Cpu, Layers, Search } from 'lucide-react'
import { api } from '../services/api'
import LoadingSpinner from '../components/LoadingSpinner'
import { useTheme } from '../context/ThemeContext'

export default function Settings() {
  const [settings, setSettings] = useState(null)
  const [health, setHealth] = useState(null)
  const [loading, setLoading] = useState(true)
  const { darkMode } = useTheme()

  useEffect(() => {
    Promise.all([api.settings(), api.health()])
      .then(([s, h]) => {
        setSettings(s)
        setHealth(h)
      })
      .catch(() => {})
      .finally(() => setLoading(false))
  }, [])

  if (loading) return <LoadingSpinner text="Loading settings..." />

  const configItems = [
    { icon: Key, label: 'Gemini API', value: settings?.gemini_configured ? 'Configured' : 'Not Configured', ok: settings?.gemini_configured },
    { icon: Cpu, label: 'AI Model', value: settings?.gemini_model || 'gemini-2.0-flash' },
    { icon: Layers, label: 'Chunk Size', value: `${settings?.chunk_size || 800} characters` },
    { icon: Layers, label: 'Chunk Overlap', value: `${settings?.chunk_overlap || 150} characters` },
    { icon: Search, label: 'Top-K Results', value: settings?.top_k_results || 5 },
  ]

  return (
    <div className="mx-auto max-w-2xl space-y-8">
      <motion.div initial={{ opacity: 0, y: 20 }} animate={{ opacity: 1, y: 0 }}>
        <div className="flex items-center gap-3">
          <SettingsIcon className="h-7 w-7 text-brand-500" />
          <h1 className="font-display text-2xl font-bold text-slate-800 dark:text-white">
            Settings
          </h1>
        </div>
        <p className="mt-1 text-sm text-slate-500">
          Application configuration and system status
        </p>
      </motion.div>

      <motion.div
        initial={{ opacity: 0, y: 20 }}
        animate={{ opacity: 1, y: 0 }}
        transition={{ delay: 0.1 }}
        className="glass rounded-2xl p-6"
      >
        <h2 className="mb-4 font-semibold text-slate-800 dark:text-white">System Configuration</h2>
        <div className="space-y-4">
          {configItems.map((item) => (
            <div
              key={item.label}
              className="flex items-center justify-between rounded-xl bg-slate-50 px-4 py-3 dark:bg-slate-800/50"
            >
              <div className="flex items-center gap-3">
                <item.icon className="h-4 w-4 text-brand-500" />
                <span className="text-sm text-slate-600 dark:text-slate-300">{item.label}</span>
              </div>
              <span
                className={`text-sm font-medium ${
                  item.ok === false
                    ? 'text-orange-500'
                    : item.ok === true
                    ? 'text-green-500'
                    : 'text-slate-800 dark:text-white'
                }`}
              >
                {item.value}
              </span>
            </div>
          ))}
        </div>
      </motion.div>

      <motion.div
        initial={{ opacity: 0, y: 20 }}
        animate={{ opacity: 1, y: 0 }}
        transition={{ delay: 0.2 }}
        className="glass rounded-2xl p-6"
      >
        <h2 className="mb-4 font-semibold text-slate-800 dark:text-white">System Info</h2>
        <div className="space-y-3 text-sm text-slate-600 dark:text-slate-300">
          <p>Version: {health?.version || '1.0.0'}</p>
          <p>Theme: {darkMode ? 'Dark' : 'Light'}</p>
          <p>Documents: {health?.documents_count ?? 0}</p>
          <p>Vector Chunks: {health?.vector_chunks ?? 0}</p>
        </div>
      </motion.div>

      {!settings?.gemini_configured && (
        <motion.div
          initial={{ opacity: 0 }}
          animate={{ opacity: 1 }}
          className="rounded-2xl border border-orange-500/30 bg-orange-500/5 p-6"
        >
          <h3 className="font-semibold text-orange-600 dark:text-orange-400">
            API Key Required
          </h3>
          <p className="mt-2 text-sm text-slate-600 dark:text-slate-400">
            Copy <code className="rounded bg-slate-200 px-1 dark:bg-slate-700">backend/.env.example</code> to{' '}
            <code className="rounded bg-slate-200 px-1 dark:bg-slate-700">backend/.env</code> and set your{' '}
            <code className="rounded bg-slate-200 px-1 dark:bg-slate-700">GEMINI_API_KEY</code>.
            Get a key at{' '}
            <a
              href="https://aistudio.google.com/apikey"
              target="_blank"
              rel="noreferrer"
              className="text-brand-500 hover:underline"
            >
              Google AI Studio
            </a>.
          </p>
        </motion.div>
      )}
    </div>
  )
}
