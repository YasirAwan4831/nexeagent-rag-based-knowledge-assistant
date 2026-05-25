import { NavLink } from 'react-router-dom'
import { motion } from 'framer-motion'
import {
  Home,
  MessageSquare,
  FileText,
  Upload,
  Settings,
  Bot,
  Moon,
  Sun,
} from 'lucide-react'
import { useTheme } from '../context/ThemeContext'

const navItems = [
  { to: '/', icon: Home, label: 'Home' },
  { to: '/chat', icon: MessageSquare, label: 'Chat' },
  { to: '/documents', icon: FileText, label: 'Documents' },
  { to: '/upload', icon: Upload, label: 'Upload' },
  { to: '/settings', icon: Settings, label: 'Settings' },
]

export default function Sidebar() {
  const { darkMode, toggleTheme } = useTheme()

  return (
    <aside className="fixed left-0 top-0 z-40 flex h-screen w-64 flex-col glass border-r">
      <div className="flex items-center gap-3 border-b border-slate-200/50 dark:border-slate-700/50 px-6 py-5">
        <div className="flex h-10 w-10 items-center justify-center rounded-xl bg-gradient-to-br from-brand-500 to-cyan-400 shadow-lg shadow-brand-500/30">
          <Bot className="h-6 w-6 text-white" />
        </div>
        <div>
          <h1 className="font-display text-lg font-bold gradient-text">NEXEAGENT</h1>
          <p className="text-xs text-slate-500 dark:text-slate-400">Knowledge Assistant</p>
        </div>
      </div>

      <nav className="flex-1 space-y-1 px-3 py-4">
        {navItems.map(({ to, icon: Icon, label }) => (
          <NavLink
            key={to}
            to={to}
            end={to === '/'}
            className={({ isActive }) =>
              `flex items-center gap-3 rounded-xl px-4 py-3 text-sm font-medium transition-all duration-200 ${
                isActive
                  ? 'bg-brand-500/10 text-brand-600 dark:text-brand-400 shadow-sm'
                  : 'text-slate-600 hover:bg-slate-100 dark:text-slate-400 dark:hover:bg-slate-800/50'
              }`
            }
          >
            {({ isActive }) => (
              <>
                <Icon className={`h-5 w-5 ${isActive ? 'text-brand-500' : ''}`} />
                {label}
                {isActive && (
                  <motion.div
                    layoutId="activeNav"
                    className="absolute left-0 h-8 w-1 rounded-r-full bg-brand-500"
                  />
                )}
              </>
            )}
          </NavLink>
        ))}
      </nav>

      <div className="border-t border-slate-200/50 dark:border-slate-700/50 p-4">
        <button
          onClick={toggleTheme}
          className="flex w-full items-center justify-center gap-2 rounded-xl bg-slate-100 px-4 py-2.5 text-sm font-medium text-slate-700 transition-colors hover:bg-slate-200 dark:bg-slate-800 dark:text-slate-300 dark:hover:bg-slate-700"
        >
          {darkMode ? <Sun className="h-4 w-4" /> : <Moon className="h-4 w-4" />}
          {darkMode ? 'Light Mode' : 'Dark Mode'}
        </button>
      </div>
    </aside>
  )
}
