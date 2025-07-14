import requests
from datetime import datetime

URL = "https://your-app-name.onrender.com/run"  # Change this to your actual Render URL

try:
    res = requests.get(URL, timeout=10)
    print(f"[{datetime.now()}] Pinged Render: Status {res.status_code}")
except Exception as e:
    print(f"[{datetime.now()}] Failed to ping Render: {e}")
