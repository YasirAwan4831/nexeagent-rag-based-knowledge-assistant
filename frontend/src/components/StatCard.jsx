import { motion } from 'framer-motion'

export default function StatCard({ icon: Icon, label, value, color = 'brand' }) {
  const colors = {
    brand: 'from-brand-500/20 to-cyan-500/20 text-brand-500',
    green: 'from-green-500/20 to-emerald-500/20 text-green-500',
    purple: 'from-purple-500/20 to-violet-500/20 text-purple-500',
    orange: 'from-orange-500/20 to-amber-500/20 text-orange-500',
  }

  return (
    <motion.div
      whileHover={{ y: -2 }}
      className="glass card-hover rounded-2xl p-6"
    >
      <div className={`mb-4 inline-flex rounded-xl bg-gradient-to-br p-3 ${colors[color]}`}>
        <Icon className="h-6 w-6" />
      </div>
      <p className="text-2xl font-bold text-slate-800 dark:text-white">{value}</p>
      <p className="mt-1 text-sm text-slate-500 dark:text-slate-400">{label}</p>
    </motion.div>
  )
}
