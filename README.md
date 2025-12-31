# 🎙️ LLaMA-Powered Offline Voice AI Assistant
A fully offline, privacy-first Voice AI Assistant built using LLaMA 3.2 via ollama, capable of real-time speech interaction, conversational memory, and voice responses — all running locally without cloud-based LLM APIs.

## 🚀 Project Overview
This project implements an end-to-end Voice AI pipeline that allows users to speak naturally, receive intelligent responses from a local LLM, and experience continuous conversation with short-term memory.

> Key Idea:
Replicate how humans converse — listen → think → respond → remember — using open-source tools and a local Large Language Model.


## 🧠 Key Features

- 🎤 Real-time Speech-to-Text (STT)
- 🧠 Local LLaMA 3.2 inference via Ollama
- 🔁 Conversational Memory (context-aware replies)
- 🗣️ Text-to-Speech (TTS) responses
- 🔐 Offline-first & privacy-preserving architecture
- 🧩 Modular and extensible design

### 🏗️ System Architecture

```
User Speech
   ↓
Speech-to-Text (STT)
   ↓
Conversation Memory (Context)
   ↓
LLaMA 3.2 (via Ollama)
   ↓
Text-to-Speech (TTS)
   ↓
Voice Response
```

Each component is decoupled, making the system easy to extend or replace.

## 📁 Project Structure

```
LLaMA-powered-VoiceAI/
│
├── main.py        # Orchestrates the full voice-AI loop
├── llm.py         # Handles interaction with LLaMA 3.2 via Ollama
├── memory.py      # Manages conversational context (short-term memory)
├── sst.py         # Speech-to-Text (microphone input)
├── tts.py         # Text-to-Speech (voice output)
└── README.md
```

## 📄 Module Explanations

1️⃣ sst.py — Speech-to-Text (Listening Layer)
- Captures live microphone audio
- Adjusts dynamically for ambient noise
- Converts speech into text commands

## Why this matters:
Ensures the assistant works in real-world environments, not just quiet rooms.

> ⚠️ Note: Uses Google STT (internet required).
Designed to be easily replaceable with Whisper or Vosk for full offline STT.

2️⃣ memory.py — Conversational Memory
- Stores recent user and assistant messages
- Maintains a sliding window of the last 6 interactions
- Prevents prompt overload while preserving context

-> Why this matters:
- Without memory, conversations feel robotic.
- With memory, responses feel continuous and intelligent.

3️⃣ llm.py — Local LLM Inference (Thinking Layer)
- Uses LLaMA 3.2 running locally via Ollama
- Communicates through a subprocess call
- Injects conversation context directly into the prompt

### Why Ollama + subprocess?
- OS-agnostic
- Lightweight integration
- No dependency lock-in
- Optimized local inference

4️⃣ tts.py — Text-to-Speech (Speaking Layer)
- Converts AI responses into natural voice output
- Tuned speech rate for better human-like delivery

### Why this matters:
Voice UX is critical — clarity and pacing improve usability.

5️⃣ main.py — Orchestrator
- Controls the full conversation loop
- Handles exit commands gracefully
- Manages memory, LLM calls, and voice interaction
- This file ties all intelligence layers together.


## 🔁 Execution Flow

1. Assistant greets the user
2. Listens for voice input
3. Converts speech → text
4. Appends conversation to memory
5. Sends prompt + context to LLaMA
6. Receives response
7. Converts text → speech
8. Speaks response
9. Repeats until user exits

## 🛠️ Installation & Setup

-> Prerequisites
- Python 3.9+
- Microphone
- Ollama installed
- Install Ollama & Model
- ollama pull llama3.2

### Install Python Dependencies
```
pip install speechrecognition pyttsx3 pyaudio
```

> ⚠️ pyaudio installation may require OS-specific setup.

▶️ Run the Assistant

**python main.py**

- Speak naturally — say “exit”, “quit”, or “stop” to end the session.
- 🔐 Privacy & Offline Design
- No cloud-based LLM APIs
- No data sent to external servers for inference
- LLM runs fully on the local machine


> Ideal for privacy-sensitive environments.

#### 🚧 Known Limitations

- Current STT uses Google Speech Recognition (internet required)
- Memory is short-term (in-memory only)


## 🎯 Why This Project Matters

- This is not just a chatbot.

It demonstrates:

- End-to-end AI system design
- Real-time voice interaction
- Local LLM deployment
- Conversational memory handling
- Modular, production-ready architecture


👤 Author

Sowmya Kanithii
Aspiring Machine Learning Engineer | AI Systems Builder
GitHub: (Sowmya)[https://github.com/sowmya13531]

