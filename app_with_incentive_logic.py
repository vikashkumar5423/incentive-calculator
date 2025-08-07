
import streamlit as st

st.set_page_config(page_title="Incentive Calculator", layout="centered")

# Custom CSS for compact layout and smaller fonts
st.markdown("""
<style>
    html, body, [class*="css"]  {
        font-size: 13px !important;
    }
    .stNumberInput, .stTextInput {
        margin-bottom: 0.5rem !important;
    }
    .stSlider {
        padding-top: 0 !important;
        margin-bottom: 1rem !important;
    }
    .card {
        padding: 1rem;
        border-radius: 10px;
        background-color: #f0f2f6;
        border-left: 6px solid #4CAF50;
        margin-top: 1rem;
    }
</style>
""", unsafe_allow_html=True)

st.title("📱 Mobile Incentive Calculator")

# All inputs in one page, minimal layout

col1, col2 = st.columns(2)
name = col1.text_input("Name")
month = col2.selectbox("Month", [
    "Jan", "Feb", "Mar", "Apr", "May", "Jun",
    "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"
])

col3, col4 = st.columns(2)
nb_target = col3.number_input("NB Target (₹)", min_value=0, step=1000)
nb_achieved = col4.number_input("NB Achieved (₹)", min_value=0, step=1000)

col5, col6 = st.columns(2)
collectible = col5.number_input("Persistency Collectible (₹)", min_value=0)
collected = col6.number_input("Persistency Collected (₹)", min_value=0)

col7, col8 = st.columns(2)
mml_contribution = col7.number_input("MMLI (₹)", min_value=0)
activation = col8.slider("Activation %", 0, 100, 50)

col9, col10, col11 = st.columns(3)
stp = col9.number_input("STP TAT", min_value=0)
non_stp = col10.number_input("Non-STP TAT", min_value=0)
medical = col11.number_input("Medical TAT", min_value=0)

policies = st.number_input("Policies Done", min_value=0)

# Product inputs in a tight loop
st.markdown("**Product-wise Achievement (₹):**")
product_achievements = []
cols = st.columns(5)
for i in range(10):
    val = cols[i % 5].number_input(f"P{i+1}", min_value=0, key=f"p{i}")
    product_achievements.append(val)

# Summary and Incentive Logic
st.markdown("---")
nb_percent = (nb_achieved / nb_target) * 100 if nb_target > 0 else 0
persistency = (collected / collectible) * 100 if collectible > 0 else 0

st.markdown(f"- NB % Achieved: `{nb_percent:.2f}%`")
st.markdown(f"- Persistency: `{persistency:.2f}%`")
st.markdown(f"- Total Products: ₹{sum(product_achievements):,.0f}")
st.markdown(f"- MMLI Contribution: ₹{mml_contribution:,.0f}")
st.markdown(f"- Activation: {activation}%")
st.markdown(f"- Policies: {policies}")

# Logic
incentive = 0
message = ""
color = "gray"

if collectible == 0 or persistency < 70:
    message = "❌ Persistency below 70%. No incentive."
    color = "#f44336"
elif nb_percent < 70:
    message = "⚠️ NB Achievement < 70%. No incentive."
    color = "#f57c00"
elif 70 <= nb_percent < 80:
    incentive = nb_achieved * 0.03
    message = f"✅ 3% Incentive: ₹{incentive:,.0f}"
    color = "#ffb300"
elif 80 <= nb_percent < 90:
    incentive = nb_achieved * 0.04
    message = f"✅ 4% Incentive: ₹{incentive:,.0f}"
    color = "#4caf50"
elif 90 <= nb_percent < 100:
    incentive = nb_achieved * 0.05
    message = f"✅ 5% Incentive: ₹{incentive:,.0f}"
    color = "#388e3c"
else:
    incentive = nb_achieved * 0.06
    message = f"🎉 Superstar! 6% Incentive: ₹{incentive:,.0f}"
    color = "#2e7d32"
    st.balloons()

st.markdown(f'''
<div class="card" style="border-left-color: {color};">
  <strong>{message}</strong>
</div>
''', unsafe_allow_html=True)
