# NewClient

A simple net cafe client for kiosk management, compatible with the newserver.

## Features
- Login dialog (username/password)
- Session timer overlay
- Lock screen when session not active
- Handles server messages: auth_success, auth_error, session_started, session_end
- Reconnects automatically after session end or disconnect

## Requirements
- Python 3.8+
- PySide6
- qasync

## Installation
```
pip install -r requirements.txt
```

## Usage
```
python main.py
```

## Configuration
- By default, connects to 127.0.0.1:8765. Change `SERVER_HOST` and `SERVER_PORT` in `main.py` if needed.

---
For use with the newserver backend. 