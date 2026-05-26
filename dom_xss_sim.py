import webview
import threading

def load_simulator():
    html = """
    <h1>DOM XSS Simulation - Educational Demo</h1>
    <p><strong>Warning:</strong> This is a safe local simulation only.</p>
    <input id="payload" style="width:80%" value="<img src=x onerror=alert('XSS')>">
    <button onclick="inject()">Inject into Vulnerable Sink</button>
    <hr>
    <div id="output" style="border:1px solid red; padding:10px; min-height:100px;"></div>

    <script>
    function inject() {
        const payload = document.getElementById('payload').value;
        document.getElementById('output').innerHTML = payload;
        alert('DOM XSS triggered! This simulates a real vulnerable sink (innerHTML).');
    }
    </script>
    """
    
    window = webview.create_window('Reflex DOM XSS Simulator - Euan Smith', html=html, width=900, height=700)
    webview.start()

if __name__ == "__main__":
    print(f"{Fore.CYAN}[*] Launching DOM XSS Educational Simulator...")
    load_simulator()
