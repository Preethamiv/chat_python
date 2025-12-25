# 💬 Real-Time Chat Application 

A real-time chat application built using **Python and WebSockets**, demonstrating persistent, bidirectional communication between clients and a server.  
This project focuses on understanding **real-time networking concepts** using Python instead of JavaScript.

---

## 🚀 Aim
The aim of this project is to implement a **real-time messaging system using Python**, showcasing how WebSockets enable instant communication without relying on traditional HTTP request–response cycles.

This project was built to strengthen:
- Networking fundamentals
- Event-driven programming in Python
- Real-time system design concepts

---

## 📝 Introduction
Standard HTTP communication is not suitable for real-time applications like chat systems.  
WebSockets overcome this limitation by maintaining a **persistent connection** between the client and the server.

This application allows multiple users to connect to a Python-based WebSocket server and exchange messages instantly.

---

## ✨ Features

### ⚡ Real-Time Messaging
- Instant message delivery using WebSockets
- Persistent client–server connection
- No page reloads required

---

### 👥 Multi-User Support
- Multiple clients can connect simultaneously
- Messages are broadcast to all connected users
- Simple username-based identification

---

### 🧑‍💻 Simple Frontend
- Minimal HTML/CSS frontend
- Focus on clarity and functionality
- Easy to understand client-side logic

---

### 🔌 Connection Handling
- Manages client connections and disconnections
- Graceful handling of WebSocket events
- Clean separation of server and client logic

---

## 🧱 Tech Stack
- **Python**
- **WebSockets (Python library)**
- **HTML**
- **CSS**
- **JavaScript (client-side)**

---

## 📂 Project Structure
```text
realtime-chat-python/
 ├─ public/
 │   └─ index.html
 ├─ server.py
 ├─ requirements.txt
 └─ README.md
