import { useEffect, useState } from 'react'
import { motion, AnimatePresence } from 'framer-motion'
import { FileText, Trash2, RefreshCw, Database } from 'lucide-react'
import { api } from '../services/api'
import LoadingSpinner from '../components/LoadingSpinner'

export default function Documents() {
  const [documents, setDocuments] = useState([])
  const [loading, setLoading] = useState(true)
  const [deleting, setDeleting] = useState(null)

  const loadDocuments = async () => {
    setLoading(true)
    try {
      const data = await api.listDocuments()
      setDocuments(data.documents || [])
    } catch {
      setDocuments([])
    } finally {
      setLoading(false)
    }
  }

  useEffect(() => {
    loadDocuments()
  }, [])

  const handleDelete = async (id) => {
    if (!confirm('Delete this document and all its indexed chunks?')) return
    setDeleting(id)
    try {
      await api.deleteDocument(id)
      setDocuments((prev) => prev.filter((d) => d.id !== id))
    } catch (err) {
      alert(err.message)
    } finally {
      setDeleting(null)
    }
  }

  const formatSize = (bytes) => {
    if (bytes < 1024) return `${bytes} B`
    if (bytes < 1048576) return `${(bytes / 1024).toFixed(1)} KB`
    return `${(bytes / 1048576).toFixed(1)} MB`
  }

  const formatDate = (iso) => {
    if (!iso) return '—'
    return new Date(iso).toLocaleDateString('en-US', {
      month: 'short',
      day: 'numeric',
      year: 'numeric',
      hour: '2-digit',
      minute: '2-digit',
    })
  }

  if (loading) return <LoadingSpinner text="Loading documents..." />

  return (
    <div className="space-y-6">
      <div className="flex items-center justify-between">
        <div>
          <h1 className="font-display text-2xl font-bold text-slate-800 dark:text-white">
            Document Library
          </h1>
          <p className="text-sm text-slate-500">
            {documents.length} document{documents.length !== 1 ? 's' : ''} indexed
          </p>
        </div>
        <button
          onClick={loadDocuments}
          className="flex items-center gap-2 rounded-xl bg-slate-100 px-4 py-2 text-sm font-medium text-slate-700 hover:bg-slate-200 dark:bg-slate-800 dark:text-slate-300 dark:hover:bg-slate-700"
        >
          <RefreshCw className="h-4 w-4" /> Refresh
        </button>
      </div>

      {documents.length === 0 ? (
        <motion.div
          initial={{ opacity: 0 }}
          animate={{ opacity: 1 }}
          className="glass rounded-2xl py-16 text-center"
        >
          <FileText className="mx-auto mb-4 h-12 w-12 text-slate-300 dark:text-slate-600" />
          <p className="text-slate-500">No documents uploaded yet.</p>
          <a href="/upload" className="mt-2 inline-block text-sm text-brand-500 hover:underline">
            Upload your first document →
          </a>
        </motion.div>
      ) : (
        <div className="grid gap-4">
          <AnimatePresence>
            {documents.map((doc, i) => (
              <motion.div
                key={doc.id}
                initial={{ opacity: 0, y: 10 }}
                animate={{ opacity: 1, y: 0 }}
                exit={{ opacity: 0, x: -20 }}
                transition={{ delay: i * 0.05 }}
                className="glass card-hover flex items-center justify-between rounded-2xl p-5"
              >
                <div className="flex items-center gap-4">
                  <div className="flex h-12 w-12 items-center justify-center rounded-xl bg-brand-500/10">
                    <FileText className="h-6 w-6 text-brand-500" />
                  </div>
                  <div>
                    <h3 className="font-medium text-slate-800 dark:text-white">
                      {doc.filename}
                    </h3>
                    <div className="mt-1 flex items-center gap-3 text-xs text-slate-500">
                      <span className="uppercase">{doc.file_type?.replace('.', '')}</span>
                      <span>{formatSize(doc.file_size)}</span>
                      <span className="flex items-center gap-1">
                        <Database className="h-3 w-3" />
                        {doc.chunk_count} chunks
                      </span>
                      <span>{formatDate(doc.uploaded_at)}</span>
                    </div>
                  </div>
                </div>

                <div className="flex items-center gap-3">
                  <span className="rounded-full bg-green-500/10 px-3 py-1 text-xs font-medium text-green-600 dark:text-green-400">
                    {doc.status}
                  </span>
                  <button
                    onClick={() => handleDelete(doc.id)}
                    disabled={deleting === doc.id}
                    className="rounded-lg p-2 text-red-400 transition-colors hover:bg-red-500/10 disabled:opacity-50"
                  >
                    <Trash2 className="h-4 w-4" />
                  </button>
                </div>
              </motion.div>
            ))}
          </AnimatePresence>
        </div>
      )}
    </div>
  )
}
