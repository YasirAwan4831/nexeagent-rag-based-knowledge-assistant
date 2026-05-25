const API_BASE = import.meta.env.VITE_API_URL || '/api'

async function request(endpoint, options = {}) {
  const url = `${API_BASE}${endpoint}`
  const response = await fetch(url, {
    headers: {
      'Content-Type': 'application/json',
      ...options.headers,
    },
    ...options,
  })

  if (!response.ok) {
    const error = await response.json().catch(() => ({ detail: 'Request failed' }))
    throw new Error(error.detail || `HTTP ${response.status}`)
  }

  return response.json()
}

export const api = {
  health: () => request('/health'),
  settings: () => request('/settings'),

  listDocuments: () => request('/documents'),
  getDocument: (id) => request(`/documents/${id}`),
  deleteDocument: (id) =>
    request(`/documents/${id}`, { method: 'DELETE' }),

  uploadDocument: async (file, onProgress) => {
    const formData = new FormData()
    formData.append('file', file)

    const response = await fetch(`${API_BASE}/upload`, {
      method: 'POST',
      body: formData,
    })

    if (!response.ok) {
      const error = await response.json().catch(() => ({ detail: 'Upload failed' }))
      throw new Error(error.detail || 'Upload failed')
    }

    return response.json()
  },

  chat: (message, sessionId, useRag = true) =>
    request('/chat', {
      method: 'POST',
      body: JSON.stringify({
        message,
        session_id: sessionId,
        use_rag: useRag,
      }),
    }),

  listSessions: () => request('/chat/sessions'),
  getSession: (id) => request(`/chat/sessions/${id}`),
  deleteSession: (id) =>
    request(`/chat/sessions/${id}`, { method: 'DELETE' }),
}
