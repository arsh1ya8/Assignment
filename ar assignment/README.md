# 🔥 Ember — AI Studio

> *A warm, organic AI chat interface built with pure HTML, CSS, and JavaScript.*

Ember is a beautifully crafted, single-file AI chat UI with an earthy, artisanal design aesthetic — intentionally distinct from mainstream AI interfaces like ChatGPT, Gemini, or Claude. Built on a warm parchment, terracotta, and sage palette, it delivers a calm and focused conversational experience.

---

## ✨ Features

### 🎨 Design System
- **Earthy / Organic theme** — warm parchment, terracotta red (`#E0312A`), and sage green (`#5a8a60`) colour palette
- **Dual typography** — *Fraunces* (serif, italic) for display + *Plus Jakarta Sans* for body text
- **Dark & Light modes** — fully themed with CSS custom properties, toggled at runtime
- **Subtle grain texture** — SVG-based fractal noise overlay for a tactile feel
- **Smooth animations** — `fadeUp`, `riseUp`, `sway`, `typeBounce` keyframes throughout

### 💬 Chat Interface
- **Welcome screen** with animated emblem and 4 suggestion cards to jumpstart conversations
- **Message bubbles** — distinct styles for user (terracotta) and AI (card background) messages
- **Typing indicator** — animated bouncing dots with AI avatar while a response is pending
- **Auto-scrolling** — smooth animated scroll to the latest message
- **Inline code & preformatted blocks** — styled code rendering inside AI responses
- **Chat history sidebar** — browsable session list with active state highlighting
- **New session** — clears the chat and prepends a new history entry with a random label

### 🎤 Voice Input
- **Web Speech API integration** — click the microphone to dictate your message
- **Real-time interim transcription** — toast shows the transcribed text as you speak
- **Auto-send** — message is sent automatically after speech ends
- **Graceful fallback** — microphone button is visually disabled with a tooltip on unsupported browsers
- **Error handling** — friendly toasts for denied permissions, no speech detected, or network errors

### 🔊 Sound Engine
- **Web Audio API** — synthesized send and receive sounds (no external audio files needed)
- **Toggle on/off** — sound button in the topbar with persistent icon state
- **Two distinct tones** — a soft click on send, a gentle chime on receive

### 📤 Export
- **One-click export** — downloads the full conversation as a formatted `.txt` file
- **Timestamped entries** — each message includes the sender name and time

### 📱 Responsive Layout
- **Collapsible sidebar** — slides off-canvas on mobile with a hamburger menu
- **Overlay backdrop** — blurred dark overlay when the sidebar is open on small screens
- **Fluid typography** — `clamp()`-based welcome title scales from mobile to desktop
- **Single-column suggestion cards** on narrow viewports

---

## 🗂️ File Structure

Ember is a **single self-contained HTML file** with no build step required.

```
ember.html
├── <head>
│   ├── Bootstrap 5.3 (layout utilities)
│   ├── Font Awesome 6.4 (icons)
│   └── Google Fonts — Fraunces + Plus Jakarta Sans
│
├── <style>  (embedded CSS)
│   ├── CSS custom properties (design tokens)
│   ├── [data-theme="light"] overrides
│   ├── Layout — sidebar + main panel
│   ├── Welcome screen & suggestion cards
│   ├── Message bubbles & typing indicator
│   ├── Input area & voice/sound buttons
│   └── Responsive breakpoints
│
└── <script>  (embedded JS — jQuery)
    ├── SoundEngine  — Web Audio API synth tones
    ├── addMessage() — renders user/AI message bubbles
    ├── sendMessage() — handles send flow + simulated AI reply
    ├── SpeechRecognition — voice input lifecycle
    ├── Export — Blob download of chat transcript
    └── UI events — theme toggle, sidebar, history, suggestions
```

---

## 🚀 Getting Started

No installation or build process needed.

1. **Download** `ember.html`
2. **Open** it in any modern browser (Chrome, Edge, Firefox, Safari)
3. Start chatting — click a suggestion card or type your own message

```bash
# Or serve it locally
npx serve .
# then visit http://localhost:3000/ember.html
```

---

## 🛠️ Customisation

All visual tokens live in the `:root` block at the top of the `<style>` section. Key variables:

| Variable | Default (Dark) | Purpose |
|---|---|---|
| `--accent` | `#E0312A` | Primary brand colour (terracotta red) |
| `--accent2` | `#5a8a60` | Secondary accent (sage green) |
| `--bg-root` | `#16120e` | Page background |
| `--bg-sidebar` | `#19140d` | Sidebar background |
| `--font-serif` | `'Fraunces'` | Display / logo font |
| `--font-sans` | `'Plus Jakarta Sans'` | Body / UI font |
| `--sidebar-w` | `264px` | Sidebar width |

To change the accent colour throughout the entire UI, update `--accent` and `--accent-hover` in both `:root` and `[data-theme="light"]`.

---

## 🔌 Connecting a Real AI Backend

The current implementation uses a local array of canned responses (`RESPONSES[]`) for demo purposes. To wire up a live model:

1. Find the `getReply()` function in the `<script>` block
2. Replace the random response logic with a `fetch()` call to your preferred API endpoint (OpenAI, Anthropic, Ollama, etc.)
3. Pass the full conversation history for multi-turn context

```js
// Example — replace getReply() with an async call
async function getReply(userMessage) {
  const res = await fetch('/api/chat', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ message: userMessage })
  });
  const data = await res.json();
  return data.reply;
}
```

---

## 🧰 Dependencies (CDN)

| Library | Version | Purpose |
|---|---|---|
| Bootstrap | 5.3.0 | Grid & utility classes |
| Font Awesome | 6.4.0 | Icons |
| Google Fonts | — | Fraunces + Plus Jakarta Sans |
| jQuery | 3.7.1 | DOM manipulation & events |

All dependencies are loaded from public CDNs — no `npm install` required.

---

## 🌐 Browser Support

| Feature | Chrome | Firefox | Safari | Edge |
|---|---|---|---|---|
| Core UI | ✅ | ✅ | ✅ | ✅ |
| Web Audio (sounds) | ✅ | ✅ | ✅ | ✅ |
| Voice input (Speech API) | ✅ | ⚠️ Partial | ✅ | ✅ |
| CSS custom properties | ✅ | ✅ | ✅ | ✅ |

> Voice input degrades gracefully — the microphone button is disabled with a tooltip on unsupported browsers.

---

## 📄 License

MIT — free to use, modify, and distribute.

---

*Ember — where ideas catch fire.*
