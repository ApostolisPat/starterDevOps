from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/status")
def read_status():
    return {"status": "OK"}

@app.get("/", response_class=HTMLResponse)
def home():
    return """
    <html>
    <head><title>MiniCloudApp</title></head>
    <body>
        <h1>Status Check</h1>
        <button onclick="checkStatus()">Check</button>
        <div id="result"></div>
        <script>
            async function checkStatus() {
                const res = await fetch('/status');
                const data = await res.json();
                document.getElementById('result').innerText = data.status;
            }
        </script>
    </body>
    </html>
    """