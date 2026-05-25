import { useState } from 'react'
import { motion } from 'framer-motion'
import { Upload as UploadIcon, FileCheck, Cpu, Database } from 'lucide-react'
import { api } from '../services/api'
import FileUpload from '../components/FileUpload'

const steps = [
  { icon: UploadIcon, title: 'Upload', desc: 'Select PDF, TXT, or DOCX files' },
  { icon: FileCheck, title: 'Extract', desc: 'Text extraction & intelligent chunking' },
  { icon: Cpu, title: 'Embed', desc: 'Gemini embedding generation' },
  { icon: Database, title: 'Store', desc: 'Vector storage in ChromaDB' },
]

export default function Upload() {
  const [loading, setLoading] = useState(false)

  const handleUpload = async (file) => {
    setLoading(true)
    try {
      return await api.uploadDocument(file)
    } finally {
      setLoading(false)
    }
  }

  return (
    <div className="mx-auto max-w-3xl space-y-8">
      <motion.div initial={{ opacity: 0, y: 20 }} animate={{ opacity: 1, y: 0 }}>
        <h1 className="font-display text-2xl font-bold text-slate-800 dark:text-white">
          Upload Company Documents
        </h1>
        <p className="mt-1 text-sm text-slate-500">
          Documents are processed, chunked, embedded, and stored in the vector knowledge base.
        </p>
      </motion.div>

      <motion.div
        initial={{ opacity: 0, y: 20 }}
        animate={{ opacity: 1, y: 0 }}
        transition={{ delay: 0.1 }}
        className="glass rounded-2xl p-8"
      >
        <FileUpload onUpload={handleUpload} loading={loading} />
      </motion.div>

      <div className="grid grid-cols-2 gap-4 md:grid-cols-4">
        {steps.map((step, i) => (
          <motion.div
            key={step.title}
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ delay: 0.2 + i * 0.1 }}
            className="glass rounded-xl p-4 text-center"
          >
            <step.icon className="mx-auto mb-2 h-6 w-6 text-brand-500" />
            <p className="text-sm font-medium text-slate-700 dark:text-slate-200">
              {step.title}
            </p>
            <p className="mt-0.5 text-xs text-slate-500">{step.desc}</p>
          </motion.div>
        ))}
      </div>
    </div>
  )
}
