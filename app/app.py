import streamlit as st
import pandas as pd
import numpy as np
import pickle
import plotly.graph_objects as go
import plotly.express as px
import shap


# ---------------- LOGIN STATE ---------------- #
import streamlit as st
import time

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

saved_data = pickle.load(open(model_path, "rb"))
model = saved_data["model"]
feature_names = saved_data["features"]



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
AI CREDIT ENGINE SCANNING
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

    col1,col2 = st.columns(2)

    with col1:
        age = st.slider("Age",18,75,30)
        loan_amount = st.number_input("Loan Amount",500,1000000,50000)
        duration = st.slider("Loan Duration",6,72,24)
        income_ratio = st.slider("Payment to Income Ratio",1,5,2)

    with col2:
        approval_threshold = st.slider("Approval Threshold",0,100,60)
        interest_rate = st.slider("Interest Rate",5,30,15)/100
        scenario = st.selectbox(
            "Macroeconomic Condition",
            ["Normal Economy","Mild Recession","Severe Recession"]
        )

    if st.button("Run Credit Risk Analysis"):

        data = pd.DataFrame({col:[0] for col in feature_names})

        data["age"] = age
        data["credit_amount"] = loan_amount
        data["month_duration"] = duration
        data["payment_to_income_ratio"] = income_ratio

        probability = model.predict_proba(data)[0][1]

        stress_factor = 1
        if scenario == "Mild Recession":
            stress_factor = 1.2
        if scenario == "Severe Recession":
            stress_factor = 1.5

        adjusted_probability = min(probability*stress_factor,1)
        risk_score = adjusted_probability*100
        credit_score = int(850-risk_score*5.5)

        col1,col2,col3 = st.columns(3)
        col1.metric("Default Probability",f"{adjusted_probability:.2%}")
        col2.metric("Risk Score",round(risk_score,2))
        col3.metric("AI Credit Score",credit_score)

        # Fraud Score

        fraud_score = np.random.uniform(0,100)

        fig = go.Figure(go.Indicator(
        mode="gauge+number",
        value=fraud_score,
        title={'text':"Fraud Risk"},
        gauge={'axis':{'range':[0,100]}}
        ))

        st.plotly_chart(fig,use_container_width=True)

        # Risk Meter

        fig = go.Figure(go.Indicator(
        mode="gauge+number",
        value=risk_score,
        title={'text':"AI Risk Meter"},
        gauge={'axis':{'range':[0,100]}}
        ))

        st.plotly_chart(fig,use_container_width=True)

        # Profit

        expected_profit=((1-adjusted_probability)*(loan_amount*interest_rate))-(adjusted_probability*loan_amount)

        st.subheader("Expected Profit")
        st.write(round(expected_profit,2))

        # Optimization

        st.subheader("Loan Optimization")

        optimal_amount = loan_amount
        if risk_score > approval_threshold:
            optimal_amount = loan_amount*0.6

        st.write("Recommended Loan Amount:",round(optimal_amount,2))

        # Decision

        st.subheader("Loan Decision")

        if risk_score < 30:
            st.success("Low Risk – Loan Approved")
        elif risk_score < approval_threshold:
            st.warning("Medium Risk – Manual Review")
        else:
            st.error("High Risk – Loan Rejected")

            alternatives = pd.DataFrame({
            "Option":["Micro Loan","Peer to Peer","Restructured Loan"],
            "Amount":[loan_amount*0.4,loan_amount*0.6,loan_amount*0.7],
            "Interest":[interest_rate+0.02,interest_rate+0.03,interest_rate],
            "Duration":[duration//2,duration,duration+12]
            })

            st.dataframe(alternatives)

        # Recommendation

        if risk_score < 30:
            recommendation="Offer premium loan"
        elif risk_score < 60:
            recommendation="Offer monitored loan"
        else:
            recommendation="Offer secured loan"

        st.info(recommendation)

        # Radar Chart

        categories=["Age","Loan","Duration","Income"]
        values=[age/75,loan_amount/1000000,duration/72,income_ratio/5]

        fig=go.Figure()
        fig.add_trace(go.Scatterpolar(r=values,theta=categories,fill="toself"))

        st.plotly_chart(fig,use_container_width=True)

        # SHAP Explainable AI
        st.subheader("Explainable AI (Model Explanation)")
        explainer = shap.Explainer(model)
        shap_values = explainer(data)

        impact = np.abs(shap_values.values).flatten()

# Ensure same length
        min_len = min(len(feature_names), len(impact))

        shap_df = pd.DataFrame({
            "Feature": feature_names[:min_len],
            "Impact": impact[:min_len]
            })

        fig = px.bar(
        shap_df,
        x="Impact",
        y="Feature",
        orientation="h",
        color="Impact",
        color_continuous_scale="Blues"
        )

        st.plotly_chart(fig,use_container_width=True)

# -------------------------------------------------
# LOAN SIMULATOR
# -------------------------------------------------

elif page == "Loan Simulator":

    st.title("Loan Profit Simulator")

    loan_amount = st.slider("Loan Amount",5000,200000,50000)
    interest_rate = st.slider("Interest Rate",5,30,15)/100
    default_prob = st.slider("Default Probability",0.0,1.0,0.1)

    loan_range = np.linspace(loan_amount*0.5,loan_amount*1.5,20)

    profits=[]

    for l in loan_range:
        p=((1-default_prob)*(l*interest_rate))-(default_prob*l)
        profits.append(p)

    strategy=pd.DataFrame({"LoanAmount":loan_range,"ExpectedProfit":profits})

    fig=px.line(strategy,x="LoanAmount",y="ExpectedProfit",color_discrete_sequence=["#00D4FF"])
    st.plotly_chart(fig,use_container_width=True)

# -------------------------------------------------
# PORTFOLIO ANALYTICS
# -------------------------------------------------
elif page == "Portfolio Analytics":

    st.title("Loan Portfolio Analytics")

    uploaded_file = st.file_uploader(
        "Upload Portfolio File (CSV or Excel)",
        type=["csv","xlsx"]
    )

    if uploaded_file:

        if uploaded_file.name.endswith(".csv"):
            portfolio = pd.read_csv(uploaded_file)

        else:
            portfolio = pd.read_excel(uploaded_file)

        st.subheader("Uploaded Portfolio Data")
        st.dataframe(portfolio)

    else:
        st.info("Upload a portfolio file to analyze.")

        # demo data
        portfolio = pd.DataFrame({
            "LoanSize": np.random.randint(5000,50000,300),
            "RiskScore": np.random.randint(10,90,300),
            "Duration": np.random.randint(6,72,300)
        })

    # scatter risk visualization
        numeric_cols = portfolio.select_dtypes(include=np.number).columns

        if len(numeric_cols) >= 2:
         fig = px.scatter(
        portfolio,
        x=numeric_cols[0],
        y=numeric_cols[1],
        color=numeric_cols[2] if len(numeric_cols) > 2 else None,
        color_continuous_scale="Blues"
    )

         st.plotly_chart(fig, use_container_width=True)
        else:
         st.warning("Not enough numeric columns for visualization")
         st.plotly_chart(fig,use_container_width=True)
         st.subheader("Portfolio Correlation Matrix")

        corr = portfolio.select_dtypes(include=np.number).corr()

        fig = px.imshow(
        corr,
    color_continuous_scale="Blues",
    text_auto=True
)

        st.plotly_chart(fig, use_container_width=True)

    # heatmap
        fig = px.density_heatmap(
        portfolio,
        x="LoanSize",
        y="RiskScore",
        nbinsx=20,
        nbinsy=20,
        color_continuous_scale="Blues"
    )

    st.plotly_chart(fig,use_container_width=True)

# -------------------------------------------------
# AI ASSISTANT
# -------------------------------------------------

elif page == "AI Loan Assistant":

    st.title("SmartCredit AI Loan Copilot")

    question = st.text_input("Ask anything about loans, risk or approval")

    if question:

        q = question.lower()

        if "risk" in q:
            st.write("Loan risk depends on borrower income ratio, loan size and macroeconomic conditions.")
        elif "profit" in q:
            st.write("Profit equals interest revenue minus expected default loss.")
        elif "approve" in q:
            st.write("Loans are approved when predicted risk stays below threshold.")
        elif "reduce risk" in q:
            st.write("Lower loan amount or shorten duration.")
        elif "best loan" in q:
            st.write("Optimal loans balance profit and manageable risk.")
        else:
            st.write("Ask about risk, approval, profit, or optimization.") 
