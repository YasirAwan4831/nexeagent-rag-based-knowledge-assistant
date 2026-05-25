import { useCallback, useState } from 'react'
import { motion, AnimatePresence } from 'framer-motion'
import { Upload, File, X, CheckCircle, AlertCircle } from 'lucide-react'

const ACCEPTED = '.pdf,.txt,.docx'

export default function FileUpload({ onUpload, loading }) {
  const [dragOver, setDragOver] = useState(false)
  const [selectedFile, setSelectedFile] = useState(null)
  const [status, setStatus] = useState(null)

  const handleFile = useCallback((file) => {
    const ext = '.' + file.name.split('.').pop().toLowerCase()
    if (!ACCEPTED.includes(ext)) {
      setStatus({ type: 'error', message: 'Only PDF, TXT, and DOCX files are supported' })
      return
    }
    setSelectedFile(file)
    setStatus(null)
  }, [])

  const handleDrop = useCallback(
    (e) => {
      e.preventDefault()
      setDragOver(false)
      const file = e.dataTransfer.files[0]
      if (file) handleFile(file)
    },
    [handleFile],
  )

  const handleUpload = async () => {
    if (!selectedFile || loading) return
    setStatus({ type: 'loading', message: 'Processing document...' })
    try {
      const result = await onUpload(selectedFile)
      setStatus({ type: 'success', message: result.message || 'Upload successful!' })
      setSelectedFile(null)
    } catch (err) {
      setStatus({ type: 'error', message: err.message })
    }
  }

  return (
    <div className="space-y-4">
      <div
        onDragOver={(e) => { e.preventDefault(); setDragOver(true) }}
        onDragLeave={() => setDragOver(false)}
        onDrop={handleDrop}
        className={`relative rounded-2xl border-2 border-dashed p-12 text-center transition-all duration-300 ${
          dragOver
            ? 'border-brand-500 bg-brand-500/5'
            : 'border-slate-300 dark:border-slate-600 hover:border-brand-400'
        }`}
      >
        <input
          type="file"
          accept={ACCEPTED}
          onChange={(e) => e.target.files[0] && handleFile(e.target.files[0])}
          className="absolute inset-0 cursor-pointer opacity-0"
        />
        <Upload className="mx-auto mb-4 h-12 w-12 text-brand-500" />
        <p className="text-lg font-medium text-slate-700 dark:text-slate-200">
          Drag & drop your document here
        </p>
        <p className="mt-1 text-sm text-slate-500">or click to browse (PDF, TXT, DOCX)</p>
      </div>

      <AnimatePresence>
        {selectedFile && (
          <motion.div
            initial={{ opacity: 0, height: 0 }}
            animate={{ opacity: 1, height: 'auto' }}
            exit={{ opacity: 0, height: 0 }}
            className="flex items-center justify-between rounded-xl bg-slate-100 px-4 py-3 dark:bg-slate-800"
          >
            <div className="flex items-center gap-3">
              <File className="h-5 w-5 text-brand-500" />
              <div>
                <p className="text-sm font-medium">{selectedFile.name}</p>
                <p className="text-xs text-slate-500">
                  {(selectedFile.size / 1024).toFixed(1)} KB
                </p>
              </div>
            </div>
            <div className="flex items-center gap-2">
              <button
                onClick={handleUpload}
                disabled={loading}
                className="rounded-lg bg-brand-500 px-4 py-2 text-sm font-medium text-white transition-colors hover:bg-brand-600 disabled:opacity-50"
              >
                {loading ? 'Processing...' : 'Upload & Index'}
              </button>
              <button
                onClick={() => setSelectedFile(null)}
                className="rounded-lg p-2 text-slate-500 hover:bg-slate-200 dark:hover:bg-slate-700"
              >
                <X className="h-4 w-4" />
              </button>
            </div>
          </motion.div>
        )}
      </AnimatePresence>

      {status && (
        <motion.div
          initial={{ opacity: 0 }}
          animate={{ opacity: 1 }}
          className={`flex items-center gap-2 rounded-xl px-4 py-3 text-sm ${
            status.type === 'success'
              ? 'bg-green-500/10 text-green-600 dark:text-green-400'
              : status.type === 'error'
              ? 'bg-red-500/10 text-red-600 dark:text-red-400'
              : 'bg-brand-500/10 text-brand-600 dark:text-brand-400'
          }`}
        >
          {status.type === 'success' ? (
            <CheckCircle className="h-4 w-4" />
          ) : status.type === 'error' ? (
            <AlertCircle className="h-4 w-4" />
          ) : (
            <Upload className="h-4 w-4 animate-pulse" />
          )}
          {status.message}
        </motion.div>
      )}
    </div>
  )
}
