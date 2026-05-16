# 📱 Device Fleet Automation (AI-style Mobile Automation Engine)

A Python-based multi-device mobile automation system built using **ADB + uiautomator2**, designed to control Android emulators and real devices for automated app interactions like YouTube search, scrolling, and task execution.

---

## 🚀 Features

* 🔌 Multi-device support (Real Android + Emulators)
* 📱 Automatic device detection (ADB)
* ⚙️ Task queue system for handling automation jobs
* 🤖 App automation (YouTube, Chrome, Docs, Camera, etc.)
* 🔍 UI-based automation using `uiautomator2` (no coordinate tapping)
* 🔁 Worker threads per device (parallel execution)
* 📊 Device state tracking (FREE / BUSY)
* 🧠 Fallback system for app launching (monkey + am start)

---

## 🏗 Architecture

```
User Input → Task Queue → Device Pool → Worker Thread
                           ↓
                    ADB Controller
                           ↓
                 UIAutomation Layer
                           ↓
                App Automation Logic
```

---

## 📦 Tech Stack

* Python 3
* ADB (Android Debug Bridge)
* uiautomator2
* threading + queue (Python concurrency)

---

## 📲 Supported Devices

* Android Emulators (AVD)
* Real Android Devices (USB / Wireless ADB)
* iOS simulator detection (basic support)

---

## 🧠 How It Works

1. System detects connected devices via ADB
2. Creates a device pool (threads per device)
3. User sends app task (e.g., "youtube")
4. Task is assigned to an available device
5. For YouTube:

   * Opens app
   * Finds search button via UI selectors
   * Types query (e.g., "MrBeast")
   * Executes search
   * Scrolls results automatically

---

## ▶️ Run Project

```bash
python main.py
```

---

## 📌 Example Commands

```
Enter app (chrome/docs/camera/exit): youtube
Enter app (chrome/docs/camera/exit): chrome
Enter app (chrome/docs/camera/exit): camera
```

---

## ⚠️ Notes

* Requires USB debugging enabled (for real devices)
* Emulator must be running before execution
* YouTube UI elements may vary by version (handled via fallback selectors)
* System is designed for learning & automation experimentation

---

## 🔧 Future Improvements

* AI-based UI self-healing selectors
* OpenCV fallback for UI detection
* OCR-based text recognition
* Advanced scheduling system
* Cloud-based device orchestration

---

## 💡 Goal

This project is built to explore:

> “How AI-style automation systems interact with real mobile UIs in a scalable way.”

---

## 👨‍💻 Author

Faizan — Mobile Automation & AI Systems Learner
