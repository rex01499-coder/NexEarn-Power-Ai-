from flask import Flask, render_template_string

app = Flask(__name__)

HTML = """<!DOCTYPE html>
<html>
<head>
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>NexEarn Power AI</title>
<style>
body{margin:0;font-family:Arial;background:linear-gradient(135deg,#0f0c29,#302b63,#24243e);color:white;min-height:100vh}
.container{max-width:480px;margin:auto;padding:20px}
.card{background:rgba(255,255,255,0.1);backdrop-filter:blur(10px);border-radius:20px;padding:20px;margin:15px 0;border:1px solid rgba(255,255,255,0.2)}
h1{text-align:center;font-size:32px;background:linear-gradient(90deg,#00f2fe,#4facfe);-webkit-background-clip:text;-webkit-text-fill-color:transparent}
.power{font-size:60px;text-align:center}
.btn{width:100%;padding:15px;border:none;border-radius:12px;background:linear-gradient(90deg,#00f2fe,#4facfe);color:white;font-weight:bold;font-size:18px;margin-top:10px}
input{width:100%;padding:12px;border-radius:10px;border:none;margin:8px 0;color:black}
.stats{display:flex;justify-content:space-between}
.stat{text-align:center}
.stat h2{color:#00f2fe}
</style>
</head>
<body>
<div class="container">
<h1>⚡ NexEarn Power AI</h1>
<div class="card">
<div class="power">🔋💰</div>
<h2 style="text-align:center">Power Mode: ULTRA ACTIVE</h2>
<p style="text-align:center">AI is calculating your earnings...</p>
<div class="stats">
<div class="stat"><h2 id="power">98%</h2><p>Power</p></div>
<div class="stat"><h2 id="earn">₹12,450</h2><p>Today</p></div>
<div class="stat"><h2>Level 9</h2><p>Level</p></div>
</div>
</div>
<div class="card">
<h3>💡 Power Calculator</h3>
<input type="number" id="clients" placeholder="Kitne Clients?">
<input type="number" id="rate" placeholder="Per Client Kitna?">
<button class="btn" onclick="calc()">CALCULATE POWER EARNING</button>
<h2 id="result" style="text-align:center;color:#00f2fe;margin-top:15px"></h2>
</div>
<div class="card">
<h3>🚀 NexEarn Features</h3>
<p>✅ Auto Client Power Boost</p>
<p>✅ AI Earning Predictor</p>
<p>✅ 24x7 Power Monitoring</p>
<button class="btn" onclick="alert('Power AI Activated! Earning Power 200% Badh Gayi!')">ACTIVATE POWER AI</button>
</div>
<p style="text-align:center;opacity:0.6;margin-top:20px">Live on Render | Gurugram, India</p>
</div>
<script>
function calc(){
 let c=document.getElementById('clients').value||0;
 let r=document.getElementById('rate').value||0;
 let total=c*r;
 let power=total*1.5;
 document.getElementById('result').innerHTML='💰 Total: ₹'+total+'<br>⚡ With Power AI: ₹'+power;
}
setInterval(()=>{document.getElementById('power').innerText=Math.floor(85+Math.random()*15)+'%';},2000);
</script>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(HTML)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
