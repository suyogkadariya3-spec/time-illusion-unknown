import streamlit as str_lit
import streamlit.components.v1 as web_comps

# Configure the browser tab layout tightly
str_lit.set_page_config(
    page_title="TIME_STAMP_BURST",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Automated 10-second isolated time-burst payload with a cute cookie notification at the end
custom_time_burst_html = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>🚨 TIME_STAMP_BURST 🚨</title>
    <style>
        * { box-sizing: border-box; margin: 0; padding: 0; }
        body, html { width: 100%; height: 100%; background-color: #000; overflow: hidden; font-family: 'Courier New', Courier, monospace; user-select: none; }
        canvas { width: 100vw; height: 100vh; display: block; }
        #strobe-layer { position: fixed; top: 0; left: 0; width: 100vw; height: 100vh; pointer-events: none; z-index: 999; opacity: 0.12; mix-blend-mode: difference; }

        /* Cute Cookie/Pop-up notification card styling */
        #cookie-popup {
            position: fixed;
            bottom: 30px;
            right: 30px;
            background: #ffffff;
            color: #111111;
            padding: 20px 40px;
            border-radius: 20px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.3);
            text-align: center;
            z-index: 10000;
            display: none;
            opacity: 0;
            border: 3px solid #ffb703;
            transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
        }
        #cookie-popup.show {
            display: block;
            opacity: 1;
            transform: translateY(0) scale(1);
            animation: bounceIn 0.5s ease-out;
        }
        .cookie-title {
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
            font-size: 36px;
            font-weight: 800;
            color: #ffb703;
            letter-spacing: -0.5px;
        }

        @keyframes bounceIn {
            0% { transform: translateY(50px) scale(0.8); opacity: 0; }
            70% { transform: translateY(-10px) scale(1.05); opacity: 1; }
            100% { transform: translateY(0) scale(1); }
        }
    </style>
</head>
<body>
    <div id="strobe-layer"></div>
    <div id="cookie-popup">
        <div class="cookie-title">hi</div>
    </div>
    <canvas id="time-canvas"></canvas>

    <script>
        const canvas = document.getElementById('time-canvas');
        const ctx = canvas.getContext('2d');
        const strobe = document.getElementById('strobe-layer');
        const cookieBox = document.getElementById('cookie-popup');

        let frame = 0;
        let startTime = Date.now();
        const durationLimit = 10000; // Exact 10 seconds execution checkpoint

        function resize() { canvas.width = window.innerWidth; canvas.height = window.innerHeight; }
        window.addEventListener('resize', resize);

        function generateRandomTime() {
            const y = Math.floor(Math.random() * 1200) + 1800;
            const m = String(Math.floor(Math.random() * 12) + 1).padStart(2, '0');
            const d = String(Math.floor(Math.random() * 28) + 1).padStart(2, '0');
            const h = String(Math.floor(Math.random() * 24)).padStart(2, '0');
            const mn = String(Math.floor(Math.random() * 60)).padStart(2, '0');
            const s = String(Math.floor(Math.random() * 60)).padStart(2, '0');
            const ms = String(Math.floor(Math.random() * 999)).padStart(3, '0');
            return `${y}/${m}/${d} ${h}:${mn}:${s}.${ms}`;
        }

        function animate() {
            let elapsed = Date.now() - startTime;

            // Trigger stop hook once timeline threshold breaches 10 seconds
            if (elapsed >= durationLimit) {
                strobe.style.backgroundColor = 'transparent';
                cookieBox.classList.add('show');
                return;
            }

            frame++;

            // Fast strobe lines matrix layer calculation
            if (frame % 3 === 0) strobe.style.backgroundColor = Math.random() > 0.5 ? '#fff' : '#00ffff';
            else if (frame % 3 === 1) strobe.style.backgroundColor = '#ff0055';
            else strobe.style.backgroundColor = 'transparent';

            // Motion-trail fade layout mechanics
            ctx.fillStyle = 'rgba(0, 0, 0, 0.12)'; 
            ctx.fillRect(0, 0, canvas.width, canvas.height);

            // Print changing date arrays randomly over spatial viewport paths
            ctx.fillStyle = Math.random() > 0.88 ? '#ff0055' : '#00ffaa'; 
            ctx.font = 'bold ' + (Math.floor(Math.random() * 10) + 12) + 'px monospace';

            for(let i = 0; i < 8; i++) {
                ctx.fillText(generateRandomTime(), Math.random() * (canvas.width - 200), Math.random() * canvas.height);
            }

            requestAnimationFrame(animate);
        }

        // Initialize layout constraints and start tracking loops immediately automatically
        resize();
        animate();
    </script>
</body>
</html>
"""

# Embed the modified source seamlessly inside your app layout
web_comps.html(custom_time_burst_html, height=900, scrolling=False)
