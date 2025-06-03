import win32gui
import win32process
import win32con
import time
import threading

def close_explorer_windows():
    def callback(hwnd, extra):
        if win32gui.IsWindowVisible(hwnd):
            _, pid = win32process.GetWindowThreadProcessId(hwnd)
            try:
                import psutil
                process = psutil.Process(pid)
                if process.name().lower() == 'explorer.exe':
                    win32gui.PostMessage(hwnd, win32con.WM_CLOSE, 0, 0)
            except:
                pass
    win32gui.EnumWindows(callback, None)

def watcher_loop():
    while True:
        close_explorer_windows()
        time.sleep(1)

def start_watcher():
    thread = threading.Thread(target=watcher_loop, daemon=True)
    thread.start() 