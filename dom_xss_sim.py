import webview
import threading

def create_window():
    html = """
    <h1>DOM XSS Simulation</h1>
    <p>Enter payload below (Educational demo only):</p>
    <input id="input" value="<img src=x onerror=alert(1)>">
    <button onclick="document.getElementById('output').innerHTML = document.getElementById('input').value">Inject</button>
    <div id="output"></div>
    <script>alert('This simulates a vulnerable sink!');</script>
    """
    window = webview.create_window('DOM XSS Simulator - Euan Smith', html=html, width=800, height=600)
    webview.start()

if __name__ == "__main__":
    print("Launching DOM XSS Simulation (Safe Educational Demo)")
    create_window()
