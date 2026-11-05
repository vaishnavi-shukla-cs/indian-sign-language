# ISL - Indian Sign Language Translator

A real-time web app that translates Indian Sign Language (ISL) hand gestures
into text using AI-powered hand tracking — all in your browser with just a webcam.

## Features

- **Real-time hand tracking** - Detects 21 hand landmarks per hand using MediaPipe
- **A-Z gesture recognition** - Recognizes the complete ISL alphabet
- **Live translation buffer** - Converts held gestures into readable text
- **Text-to-Speech** - Speaks out the translated text
- **Two-hand support** - Tracks both hands simultaneously
- **Mirrored camera view** - Natural, intuitive display
- **No installation needed** - Runs entirely in the browser

## Tech Stack

- **MediaPipe Hands** - Hand landmark detection (Google)
- **React 18** - UI framework
- **Tailwind CSS** - Styling
- **Framer Motion** - Animations
- **Vanilla Python** - Local server (no dependencies)

## Getting Started

### Prerequisites

- Python 3.x installed
- A webcam
- A modern browser (Chrome/Edge recommended)

### Run the app

1. Clone this repository:
   ```bash
   git clone https://github.com/vaishnavi-shukla-cs/ISL.git
   cd isl-translator
   ```

2. Start the server:
   ```bash
   python app.py
   ```

3. Open **http://localhost:8000** in your browser

4. Log in (any valid email/password works in the demo) and click **Start Detection**

## How to Use

1. Allow camera access when prompted
2. Show your hand clearly to the camera
3. Hold each letter gesture steady for about 1 second
4. Watch the translation build in the right panel
5. Click **Speak** to hear the translation aloud
6. Click **Clear** to reset the buffer

## How It Works

1. The webcam feed is processed frame-by-frame by **MediaPipe Hands**
2. Each frame yields 21 3D landmarks per detected hand
3. A geometric classifier checks finger extension
   (tip-to-wrist distance vs knuckle-to-wrist distance)
4. Stable gestures are appended to the translation buffer
5. The buffer is rendered as text and can be spoken via the Web Speech API

## Project Structure

```
isl-translator/
├── app.py                      # Local server (built-in Python only)
├── isl-translator-fixed.html   # The full web app
└── README.md                   # This file
```

## Notes

- This is a demo-grade recognizer: it uses simple geometric rules for the
  static ISL alphabet, not a trained ML model. Accuracy depends on lighting,
  camera angle, and hand distance from the lens.
- Login is front-end only (no real authentication) — any valid-format
  credentials will work.

## License

MIT
