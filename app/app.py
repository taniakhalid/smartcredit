import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.express as px
import requests


# ---------------- LOGIN STATE ---------------- #
import time
# ------------------------------
# LOAD MODEL (FIX)
# ------------------------------
import pickle

saved_data = pickle.load(open("models/credit_risk_model.pkl", "rb"))
model = saved_data["model"]
feature_names = saved_data["features"]
# ---------------- SESSION ----------------
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
from datetime import datetime

clock_placeholder = st.empty()

def render_clock():
    now = datetime.now().strftime("%H:%M")
    clock_placeholder.markdown(f"""
    <style>
    .cyber-clock {{
        position: fixed;
        bottom: 20px;
        left: 25px;
        color: #00D4FF;
        font-family: monospace;
        font-size: 14px;
        text-shadow: 0 0 8px #00D4FF, 0 0 18px #00D4FF;
        z-index: 999999;
    }}
    </style>

    <div class="cyber-clock">
        {now} | AI MODE
    </div>
    """, unsafe_allow_html=True)

render_clock()

USERS = {
    "admin": "smartcredit",
    "tania": "ai123",
    "analyst": "risk2025"
}

# ---------------- LOGIN PAGE ----------------
if not st.session_state.logged_in:

    st.markdown("""
    <style>

    .stApp {
        background: radial-gradient(circle at top,#071A2F,#020617);
        overflow:hidden;
    }

    /* CLOCK bottom-left */
    .cyber-clock{
        position:fixed;
        bottom:20px;
        left:25px;
        color:#00D4FF;
        font-family:monospace;
        font-size:14px;
        text-shadow:0 0 8px #00D4FF,0 0 18px #00D4FF;
        z-index:999999;
        animation:clockPulse 2s infinite;
    }

    @keyframes clockPulse{
        0%,100%{opacity:0.6}
        50%{opacity:1}
    }

    /* SCAN BAR */
    .scan{
        text-align:center;
        margin-top:80px;
        color:#00D4FF;
        font-family:monospace;
        letter-spacing:3px;
        text-shadow:0 0 10px #00D4FF;
        animation:scanPulse 2s infinite;
    }

    @keyframes scanPulse{
        0%,100%{opacity:0.5}
        50%{opacity:1}
    }

    /* TITLE */
    .title{
        text-align:center;
        font-size:56px;
        margin-top:40px;
        color:white;
        text-shadow:0 0 25px #00D4FF,0 0 45px #00D4FF;
    }

    /* FLOATING TEXT */
    .float1,.float2,.float3,.float4{
        position:fixed;
        font-family:monospace;
        color:#00D4FF;
        opacity:0.25;
        white-space:nowrap;
    }

    .float1{ left:10%; animation:move1 18s linear infinite; }
    .float2{ left:30%; animation:move2 20s linear infinite; }
    .float3{ left:50%; animation:move3 22s linear infinite; }
    .float4{ left:70%; animation:move4 24s linear infinite; }

    @keyframes move1{
        0%{ transform:translateY(110vh);}
        100%{ transform:translateY(-10vh);}
    }

    @keyframes move2{
        0%{ transform:translateY(120vh);}
        100%{ transform:translateY(-20vh);}
    }

    @keyframes move3{
        0%{ transform:translateY(115vh);}
        100%{ transform:translateY(-15vh);}
    }

    @keyframes move4{
        0%{ transform:translateY(125vh);}
        100%{ transform:translateY(-25vh);}
    }

    /* PARTICLES */
    .p1,.p2,.p3,.p4,.p5{
        position:fixed;
        width:3px;
        height:3px;
        background:#00D4FF;
        border-radius:50%;
        box-shadow:0 0 8px #00D4FF;
    }

    .p1{left:15%; animation:pMove1 12s linear infinite;}
    .p2{left:25%; animation:pMove2 14s linear infinite;}
    .p3{left:35%; animation:pMove3 16s linear infinite;}
    .p4{left:65%; animation:pMove4 13s linear infinite;}
    .p5{left:85%; animation:pMove5 18s linear infinite;}

    @keyframes pMove1{0%{transform:translateY(100vh);}100%{transform:translateY(-10vh);}}
    @keyframes pMove2{0%{transform:translateY(110vh);}100%{transform:translateY(-20vh);}}
    @keyframes pMove3{0%{transform:translateY(105vh);}100%{transform:translateY(-15vh);}}
    @keyframes pMove4{0%{transform:translateY(115vh);}100%{transform:translateY(-25vh);}}
    @keyframes pMove5{0%{transform:translateY(120vh);}100%{transform:translateY(-10vh);}}

    </style>

   

    <div class="scan">
    [ AI CREDIT ENGINE SCANNING ███████████░░ ]
    </div>

    <div class="title">
    Smart<span style="color:#00D4FF;">Credit</span> AI
    </div>

    <!-- floating text -->
    <div class="float1">$982.77 → VERIFIED</div>
    <div class="float2">$5432.11 → PROCESSING</div>
    <div class="float3">$7432.21 → AI RISK CHECK</div>
    <div class="float4">$9301.44 → CREDIT SCORE</div>

    <!-- particles -->
    <div class="p1"></div>
    <div class="p2"></div>
    <div class="p3"></div>
    <div class="p4"></div>
    <div class="p5"></div>

    """, unsafe_allow_html=True)

    # LOGIN FORM CENTER
    col1,col2,col3 = st.columns([1,2,1])

    with col2:
        with st.form("login"):
            username = st.text_input("", placeholder="Username")
            password = st.text_input("", placeholder="Password", type="password")

            submit = st.form_submit_button("Authenticate")

            if submit:
                if username in USERS and USERS[username] == password:
                    with st.spinner("Authenticating..."):
                        time.sleep(1)
                    st.session_state.logged_in = True
                    st.rerun()
                else:
                    st.error("Access Denied")

    st.stop()
# -------------------------------------------------
# PAGE CONFIG
# -------------------------------------------------

st.set_page_config(page_title="SmartCredit AI", layout="wide")
st.markdown(
"""
<div class="ai-scan">
[ AI CREDIT ENGINE SCANNING ██████████░░ ]
</div>
""",
unsafe_allow_html=True
)
# -------------------------------------------------
# CYBERPUNK UI + ANIMATION
# -------------------------------------------------
st.markdown("""
<style>

/* ===== MAIN CYBERPUNK BACKGROUND ===== */

.stApp{
background:
radial-gradient(circle at top,#051424,#020617 60%);
color:white;
overflow:hidden;
}

/* ===== NEURAL NETWORK BACKGROUND ===== */

.network-line{
position:fixed;
width:2px;
height:200px;
background:linear-gradient(transparent,#00D4FF,transparent);
opacity:0.15;
animation:flow 10s linear infinite;
}

@keyframes flow{
0%{transform:translateY(100vh)}
100%{transform:translateY(-100vh)}
}

/* ===== FLOATING PARTICLES ===== */

.particle{
position:fixed;
width:4px;
height:4px;
background:#00D4FF;
border-radius:50%;
box-shadow:0 0 8px #00D4FF;
animation:particleMove 14s linear infinite;
opacity:0.6;
}

@keyframes particleMove{
0%{transform:translateY(100vh)}
100%{transform:translateY(-100vh)}
}

/* ===== CYBERPUNK TITLE ===== */

h1{
color:#00D4FF;
text-shadow:
0 0 8px #00D4FF,
0 0 16px #00D4FF,
0 0 32px #00D4FF;
font-weight:700;
}

/* ===== METRIC CARDS ===== */

[data-testid="metric-container"]{
background:rgba(0,212,255,0.05);
border:1px solid rgba(0,212,255,0.35);
border-radius:14px;
padding:15px;
box-shadow:0 0 12px rgba(0,212,255,0.4);
}

/* ===== SIDEBAR ===== */

section[data-testid="stSidebar"]{
background:#020617;
border-right:1px solid #00D4FF;
}

/* ===== CYBERPUNK BUTTON ===== */

.stButton>button{
background:linear-gradient(90deg,#00D4FF,#2563EB);
border-radius:12px;
color:white;
font-weight:600;
box-shadow:0 0 10px #00D4FF;
}

/* ===== AI SCANNING BAR ===== */

.ai-scan{
font-family:monospace;
color:#00D4FF;
font-size:14px;
letter-spacing:2px;
margin-bottom:15px;
text-shadow:0 0 8px #00D4FF;
animation:scanPulse 2s infinite;
}

@keyframes scanPulse{
0%,100%{opacity:0.6}
50%{opacity:1}
}

</style>

<div class="network-line" style="left:10%"></div>
<div class="network-line" style="left:30%"></div>
<div class="network-line" style="left:50%"></div>
<div class="network-line" style="left:70%"></div>
<div class="network-line" style="left:90%"></div>

<div class="particle" style="left:15%"></div>
<div class="particle" style="left:35%"></div>
<div class="particle" style="left:55%"></div>
<div class="particle" style="left:75%"></div>

""", unsafe_allow_html=True)
st.markdown("""
<style>

@keyframes pulseNode {
0%,100% {opacity:0.6; transform:scale(1);}
50% {opacity:1; transform:scale(1.2);}
}

@keyframes glowPulse {
0%,100% {filter:drop-shadow(0 0 6px rgba(0,212,255,0.4));}
50% {filter:drop-shadow(0 0 18px rgba(0,212,255,0.9));}
}

.logo-container{
display:flex;
align-items:center;
gap:15px;
margin-bottom:20px;
}

.neural-node{
animation:pulseNode 2s ease-in-out infinite;
}

.logo-glow{
animation:glowPulse 3s ease-in-out infinite;
}

.logo-text{
font-size:34px;
font-weight:700;
font-family:Inter, sans-serif;
color:white;
}

.logo-accent{
color:#00D4FF;
}

.logo-tag{
font-size:11px;
letter-spacing:3px;
text-transform:uppercase;
color:#00D4FF;
opacity:0.7;
}

</style>

<div>
<div class="logo-text">
Smart<span class="logo-accent">Credit</span>
</div>

<div class="logo-tag">
AI-POWERED FINANCE
</div>
</div>

</div>
""", unsafe_allow_html=True)
st.markdown("""
<style>

/* main background */

.stApp{
background: radial-gradient(circle at top,#071A2F,#020617);
color:white;
}

/* glowing titles */

h1,h2,h3{
color:#00D4FF;
text-shadow:
0 0 8px #00D4FF,
0 0 16px #00D4FF,
0 0 32px #00D4FF;
}

/* sidebar */

section[data-testid="stSidebar"]{
background:#020617;
border-right:1px solid #00D4FF;
}

/* metrics */

[data-testid="metric-container"]{
background:rgba(0,212,255,0.05);
border-radius:14px;
padding:15px;
border:1px solid rgba(0,212,255,0.3);
box-shadow:0 0 10px rgba(0,212,255,0.3);
}

/* moving particles */

.particle{
position:fixed;
width:3px;
height:3px;
background:#00D4FF;
border-radius:50%;
animation:move 20s linear infinite;
opacity:0.6;
}

@keyframes move{
0%{transform:translateY(100vh);}
100%{transform:translateY(-100vh);}
}

/* moving logo */

.logo{
font-size:28px;
font-weight:bold;
color:#00D4FF;
text-shadow:0 0 10px #00D4FF;
animation:float 6s ease-in-out infinite;
}

@keyframes float{
0%{transform:translateY(0px)}
50%{transform:translateY(-8px)}
100%{transform:translateY(0px)}
}

</style>


<div class="particle" style="left:10%"></div>
<div class="particle" style="left:20%"></div>
<div class="particle" style="left:30%"></div>
<div class="particle" style="left:40%"></div>
<div class="particle" style="left:60%"></div>
<div class="particle" style="left:70%"></div>
<div class="particle" style="left:80%"></div>



""", unsafe_allow_html=True)
st.markdown("""
<div class="neural-network"></div>

<style>

.neural-network{
position:fixed;
top:0;
left:0;
width:100%;
height:100%;
pointer-events:none;
z-index:-1;
}

.node{
position:absolute;
width:6px;
height:6px;
background:#00D4FF;
border-radius:50%;
box-shadow:0 0 10px #00D4FF;
animation:pulse 3s infinite;
}

@keyframes pulse{
0%,100%{opacity:0.4}
50%{opacity:1}
}

.line{
position:absolute;
width:2px;
background:linear-gradient(#00D4FF,transparent);
opacity:0.2;
animation:flowline 10s linear infinite;
}

@keyframes flowline{
0%{transform:translateY(100vh)}
100%{transform:translateY(-100vh)}
}

</style>
""", unsafe_allow_html=True)
st.markdown("""
<div class="transactions"></div>

<style>

.tx{
position:fixed;
color:#00D4FF;
font-family:monospace;
font-size:12px;
opacity:0.5;
animation:txmove linear infinite;
}

@keyframes txmove{
0%{transform:translateX(-200px)}
100%{transform:translateX(120vw)}
}

</style>

<script>

const container = document.body;

for(let i=0;i<40;i++){

let tx=document.createElement("div");

tx.className="tx";

tx.innerText="$"+(Math.random()*9000).toFixed(2);

tx.style.top=Math.random()*100+"vh";

tx.style.animationDuration=(10+Math.random()*10)+"s";

container.appendChild(tx);

}

</script>

""", unsafe_allow_html=True)
st.markdown("""
<style>

.tx-stream{
position:fixed;
left:-200px;
font-family:monospace;
color:#00D4FF;
font-size:12px;
opacity:0.5;
letter-spacing:1px;
animation:txMove linear infinite;
}

@keyframes txMove{
0%{
transform:translateX(0);
}
100%{
transform:translateX(120vw);
}

}

</style>

<div class="tx-stream" style="top:10%;animation-duration:12s;">$1283.45 → APPROVED</div>
<div class="tx-stream" style="top:20%;animation-duration:15s;">$5432.11 → PROCESSING</div>
<div class="tx-stream" style="top:30%;animation-duration:18s;">$982.77 → VERIFIED</div>
<div class="tx-stream" style="top:40%;animation-duration:14s;">$7432.21 → AI RISK CHECK</div>
<div class="tx-stream" style="top:50%;animation-duration:16s;">$235.00 → APPROVED</div>
<div class="tx-stream" style="top:60%;animation-duration:13s;">$9301.44 → CREDIT SCORE 712</div>
<div class="tx-stream" style="top:70%;animation-duration:17s;">$4512.89 → LOAN ANALYSIS</div>
<div class="tx-stream" style="top:80%;animation-duration:19s;">$1200.00 → FRAUD SCAN</div>

""", unsafe_allow_html=True)
# -------------------------------------------------
# LOAD MODEL
# -------------------------------------------------
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
model_path = os.path.join(BASE_DIR, "models", "credit_risk_model.pkl")



# -------------------------------------------------
# SIDEBAR
# -------------------------------------------------

st.sidebar.markdown("""
<h3 style="
color:#00D4FF;
text-shadow:0 0 10px #00D4FF;">
SmartCredit AI
</h3>
""", unsafe_allow_html=True)

page = st.sidebar.radio(
"Navigation",
[
"Dashboard",
"Credit Risk Prediction",
"Loan Simulator",
"Portfolio Analytics",
"AI Loan Assistant"
]
)

# -------------------------------------------------
# DASHBOARD
# -------------------------------------------------

if page == "Dashboard":
    st.markdown("""
<div style="text-align:center; margin-top:20px; margin-bottom:40px;">

<h1 style="
font-size:48px;
font-weight:700;
color:white;
text-shadow:
0 0 10px #00D4FF,
0 0 20px #00D4FF,
0 0 40px #00D4FF;">
Smart<span style="color:#00D4FF;">Credit</span> AI
</h1>

<div style="
font-family:monospace;
color:#00D4FF;
text-align:center;
letter-spacing:3px;
margin-top:10px;
text-shadow:0 0 8px #00D4FF;">
[ AI CREDIT ENGINE SCANNING ███████████░░ ]
</div>

<p style="
margin-top:10px;
letter-spacing:4px;
color:#00D4FF;
font-size:12px;">
AI-POWERED FINANCE
</p>

</div>
""", unsafe_allow_html=True)
    st.markdown("""
<style>

.scan-container{
text-align:center;
margin-top:10px;
margin-bottom:20px;
font-family:monospace;
color:#00D4FF;
letter-spacing:3px;
text-shadow:0 0 10px #00D4FF;
}

.scan-bar{
width:300px;
height:8px;
border:1px solid #00D4FF;
margin:auto;
margin-top:8px;
overflow:hidden;
box-shadow:0 0 10px #00D4FF;
}

.scan-progress{
height:100%;
width:0%;
background:linear-gradient(90deg,#00D4FF,#3B82F6);
animation:scanMove 3s infinite;
}

@keyframes scanMove{
0%{width:0%}
50%{width:100%}
100%{width:0%}
}

</style>

<div class="scan-container">
CREDIT ENGINE SCANNING
<div class="scan-bar">
<div class="scan-progress"></div>
</div>
</div>
""", unsafe_allow_html=True)
# -------------------------------------------------
# CREDIT RISK PREDICTION
# -------------------------------------------------
elif page == "Credit Risk Prediction":

    st.title("Borrower Credit Risk Analysis")

    col1, col2 = st.columns(2)

    with col1:
        age = st.slider("Age", 18, 75, 30)
        loan_amount = st.number_input("Loan Amount", 500, 1000000, 50000)
        duration = st.slider("Loan Duration", 6, 72, 24)
        income_ratio = st.slider("Payment to Income Ratio", 1, 5, 2)

    with col2:
        approval_threshold = st.slider("Approval Threshold", 0, 100, 60)
        interest_rate = st.slider("Interest Rate", 5, 30, 15) / 100
        scenario = st.selectbox(
            "Macroeconomic Condition",
            ["Normal Economy", "Mild Recession", "Severe Recession"]
        )

    if st.button("Run Credit Risk Analysis"):

        # ---------- MODEL PREDICTION ----------
        data = pd.DataFrame({col:[0] for col in feature_names})

        data["age"] = age
        data["credit_amount"] = loan_amount
        data["month_duration"] = duration
        data["payment_to_income_ratio"] = income_ratio

        prob = model.predict_proba(data)[0][1]

        # ---------- YOUR LOGIC (UNCHANGED) ----------
        prob = prob * 0.7
        risk_score = prob * 85 + 10

        credit_score = int(850 - risk_score * 3)
        credit_score = max(300, min(850, credit_score))

        stress_factor = 1
        if scenario == "Mild Recession":
            stress_factor = 1.2
        elif scenario == "Severe Recession":
            stress_factor = 1.5

        adjusted_probability = min(prob * stress_factor, 1)

        # ---------- METRICS ----------
        c1, c2, c3 = st.columns(3)
        c1.metric("Default Probability", f"{adjusted_probability:.2%}")
        c2.metric("Risk Score", round(risk_score, 2))
        c3.metric("Credit Score", credit_score)

        # ---------- PROFIT ----------
        expected_profit = (
            (1 - adjusted_probability) * (loan_amount * interest_rate)
            - (adjusted_probability * loan_amount * 0.2)
        )

        st.subheader("Expected Profit")
        st.write(round(expected_profit, 2))

        # ---------- DECISION ----------
        st.subheader("Loan Decision")

        if adjusted_probability < 0.4:
            st.success("Low Risk – Loan Approved")
        elif adjusted_probability < 0.6:
            st.warning("Medium Risk – Manual Review")
        else:
            st.error("High Risk – Loan Rejected")

        # ---------- GRAPHS ----------
        st.subheader("Risk Breakdown")

        chart_data = pd.DataFrame({
            "Metric": ["Default Risk", "Safe Probability"],
            "Value": [adjusted_probability, 1 - adjusted_probability]
        })

        st.bar_chart(chart_data.set_index("Metric"))

        # Profit curve
        st.subheader("Profit vs Risk")

        probs = [i/100 for i in range(10, 90, 5)]
        profits = []

        for p in probs:
            profit = (1 - p) * (loan_amount * interest_rate) - (p * loan_amount * 0.2)
            profits.append(profit)

        chart_df = pd.DataFrame({"Risk": probs, "Profit": profits})
        st.line_chart(chart_df.set_index("Risk"))

        # Radar
        st.subheader("Borrower Profile")

        categories = ["Age", "Loan", "Duration", "Income"]
        values = [age/75, loan_amount/1000000, duration/72, income_ratio/5]

        fig = go.Figure()
        fig.add_trace(go.Scatterpolar(r=values, theta=categories, fill="toself"))
        st.plotly_chart(fig, use_container_width=True)

        # ---------- AI EXPLANATION ----------
        st.subheader("AI Explanation")

        if adjusted_probability < 0.4:
            explanation = "Low default risk. Borrower has strong repayment ability."
        elif adjusted_probability < 0.6:
            explanation = "Moderate risk. Loan should be reviewed carefully."
        else:
            explanation = "High risk. Loan likely to default based on financial indicators."

        st.info(explanation)


# -------------------------------------------------
# PORTFOLIO ANALYTICS (FIXED - NO API)
# -------------------------------------------------
elif page == "Portfolio Analytics":

    st.title("Loan Portfolio Analytics")

    uploaded_file = st.file_uploader("Upload Portfolio CSV", type=["csv"])

    if uploaded_file is not None:

        df = pd.read_csv(uploaded_file)
        st.dataframe(df.head())

        results = []

        for _, row in df.iterrows():

            data = pd.DataFrame({col:[0] for col in feature_names})

            data["age"] = int(row["age"])
            data["credit_amount"] = int(row["credit_amount"])
            data["month_duration"] = int(row["month_duration"])
            data["payment_to_income_ratio"] = int(row["payment_to_income_ratio"])

            prob = model.predict_proba(data)[0][1]
            results.append(prob)

        df["default_probability"] = results

        st.bar_chart(df["default_probability"])

        high_risk = df[df["default_probability"] > 0.6]
        st.subheader("High Risk Loans")
        st.dataframe(high_risk)

        c1, c2 = st.columns(2)
        c1.metric("Average Risk", round(df["default_probability"].mean(), 2))
        c2.metric("High Risk Loans", len(high_risk))
def categorize(p):
    if p < 0.3:
        return "Low Risk"
    elif p < 0.6:
        return "Medium Risk"
    else:
        return "High Risk"

df["category"] = df["default_probability"].apply(categorize)

st.subheader("Portfolio Segmentation")
st.plotly_chart(
    px.pie(df, names="category")
)


# -------------------------------------------------
# LOAN SIMULATOR (FIXED)
# -------------------------------------------------
elif page == "Loan Simulator":

    st.title("Loan Profit Simulator")

    sim_amount = st.slider("Loan Amount", 1000, 100000, 20000)
    sim_duration = st.slider("Duration", 6, 60, 24)
    sim_interest = st.slider("Interest Rate", 5, 25, 12) / 100

    if st.button("Simulate Loan"):

        data = pd.DataFrame({col:[0] for col in feature_names})

        data["age"] = 30
        data["credit_amount"] = sim_amount
        data["month_duration"] = sim_duration
        data["payment_to_income_ratio"] = 2

        prob = model.predict_proba(data)[0][1]

        expected_profit = (
            (1 - prob) * (sim_amount * sim_interest)
            - (prob * sim_amount * 0.2)
        )

        st.metric("Default Risk", f"{prob:.2%}")
        st.metric("Expected Profit", round(expected_profit, 2))

        # Graph
        amounts = range(5000, 50000, 5000)
        profits = []

        for amt in amounts:
            data["credit_amount"] = amt
            p = model.predict_proba(data)[0][1]
            profit = (1 - p) * (amt * sim_interest) - (p * amt * 0.2)
            profits.append(profit)

        st.line_chart(profits)


# -------------------------------------------------
# AI LOAN ASSISTANT (FIXED)
# -------------------------------------------------
elif page == "AI Loan Assistant":

    st.title("AI Loan Assistant 🤖")

    user_question = st.text_input("Ask anything about loan risk...")

    if st.button("Ask AI"):

        client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

        prompt = f"""
        You are a financial credit risk expert.

        User question: {user_question}

        Answer clearly and professionally.
        """

        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are a credit risk expert."},
                {"role": "user", "content": prompt}
            ]
        )

        st.write(response.choices[0].message.content)
