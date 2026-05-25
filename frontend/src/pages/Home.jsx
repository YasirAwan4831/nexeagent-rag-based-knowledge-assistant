import { useEffect, useState } from 'react'
import { Link } from 'react-router-dom'
import { motion } from 'framer-motion'
import {
  MessageSquare,
  Upload,
  FileText,
  Database,
  ArrowRight,
  Sparkles,
} from 'lucide-react'
import { api } from '../services/api'
import StatCard from '../components/StatCard'
import LoadingSpinner from '../components/LoadingSpinner'

export default function Home() {
  const [health, setHealth] = useState(null)
  const [loading, setLoading] = useState(true)

  useEffect(() => {
    api.health()
      .then(setHealth)
      .catch(() => setHealth(null))
      .finally(() => setLoading(false))
  }, [])

  if (loading) return <LoadingSpinner text="Loading dashboard..." />

  return (
    <div className="space-y-8">
      <motion.div
        initial={{ opacity: 0, y: 20 }}
        animate={{ opacity: 1, y: 0 }}
        className="relative overflow-hidden rounded-3xl bg-gradient-to-br from-brand-600 via-brand-500 to-cyan-500 p-8 text-white shadow-2xl shadow-brand-500/20"
      >
        <div className="relative z-10">
          <div className="mb-2 flex items-center gap-2">
            <Sparkles className="h-5 w-5" />
            <span className="text-sm font-medium text-white/80">AI Knowledge Assistant</span>
          </div>
          <h1 className="font-display text-3xl font-bold md:text-4xl">
            Welcome to NEXEAGENT
          </h1>
          <p className="mt-2 max-w-xl text-white/80">
            Your intelligent company knowledge assistant. Upload documents, ask questions,
            and get accurate AI-powered answers from your company data.
          </p>
          <div className="mt-6 flex gap-3">
            <Link
              to="/chat"
              className="inline-flex items-center gap-2 rounded-xl bg-white px-5 py-2.5 text-sm font-semibold text-brand-600 transition-transform hover:scale-105"
            >
              Start Chatting <ArrowRight className="h-4 w-4" />
            </Link>
            <Link
              to="/upload"
              className="inline-flex items-center gap-2 rounded-xl bg-white/20 px-5 py-2.5 text-sm font-semibold text-white backdrop-blur transition-colors hover:bg-white/30"
            >
              Upload Documents
            </Link>
          </div>
        </div>
        <div className="absolute -right-10 -top-10 h-64 w-64 rounded-full bg-white/10 blur-3xl" />
        <div className="absolute -bottom-10 right-20 h-48 w-48 rounded-full bg-cyan-300/20 blur-3xl" />
      </motion.div>

      <div className="grid gap-6 sm:grid-cols-2 lg:grid-cols-4">
        <StatCard
          icon={FileText}
          label="Documents Indexed"
          value={health?.documents_count ?? 0}
          color="brand"
        />
        <StatCard
          icon={Database}
          label="Vector Chunks"
          value={health?.vector_chunks ?? 0}
          color="purple"
        />
        <StatCard
          icon={Sparkles}
          label="AI Status"
          value={health?.gemini_configured ? 'Ready' : 'Setup Required'}
          color={health?.gemini_configured ? 'green' : 'orange'}
        />
        <StatCard
          icon={MessageSquare}
          label="System Status"
          value={health?.status === 'healthy' ? 'Online' : 'Offline'}
          color="green"
        />
      </div>

      <div className="grid gap-6 md:grid-cols-3">
        {[
          {
            icon: Upload,
            title: 'Upload Documents',
            desc: 'Add PDF, TXT, or DOCX company files',
            to: '/upload',
          },
          {
            icon: MessageSquare,
            title: 'AI Chat',
            desc: 'Ask questions about your documents',
            to: '/chat',
          },
          {
            icon: FileText,
            title: 'Manage Files',
            desc: 'View and manage uploaded documents',
            to: '/documents',
          },
        ].map((item, i) => (
          <motion.div
            key={item.title}
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ delay: i * 0.1 }}
          >
            <Link
              to={item.to}
              className="glass card-hover block rounded-2xl p-6"
            >
              <item.icon className="mb-4 h-8 w-8 text-brand-500" />
              <h3 className="font-semibold text-slate-800 dark:text-white">{item.title}</h3>
              <p className="mt-1 text-sm text-slate-500 dark:text-slate-400">{item.desc}</p>
            </Link>
          </motion.div>
        ))}
      </div>
    </div>
  )
}
