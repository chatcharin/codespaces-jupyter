
import subprocess
import threading
import os
import time

def start_ollama():
    subprocess.run(['ollama', 'serve'])

def download_model():
    subprocess.run(['ollama', 'pull', 'deepseek-r1:7b'])

def start_open_webui():
    subprocess.run(['venv/bin/open-webui', 'serve', '--port', '8081'])

# Start servers in separate threads
threading.Thread(target=start_ollama).start()
time.sleep(5)
threading.Thread(target=download_model).start()
threading.Thread(target=start_open_webui).start()
