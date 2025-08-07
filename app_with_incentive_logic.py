
import streamlit as st

st.set_page_config(page_title="Incentive Calculator", layout="centered")

# Title with emoji and subtitle
st.markdown("""
<style>
    .big-font {
        font-size: 28px !important;
        font-weight: 600;
    }
    .subtle {
        color: gray;
        font-size: 14px;
        margin-bottom: 10px;
    }
    .card {
        padding: 1rem;
        border-radius: 10px;
        background-color: #f0f2f6;
        border-left: 6px solid #4CAF50;
    }
</style>
""", unsafe_allow_html=True)

st.markdown('<p class="big-font">🎯 Incentive Goal-Setting Calculator</p>', unsafe_allow_html=True)
st.markdown('<p class="subtle">Plan your month and estimate your earnings based on inputs. Persistency must be ≥ 70% to qualify.</p>', unsafe_allow_html=True)

# Salesperson Info
with st.container():
    with st.expander("👤 Salesperson Details", expanded=True):
        col1, col2 = st.columns(2)
        name = col1.text_input("Name")
        month = col2.selectbox("Month", [
            "Jan", "Feb", "Mar", "Apr", "May", "Jun",
            "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"
        ])

# New Business & Persistency
with st.container():
    with st.expander("📈 Key Performance Metrics", expanded=True):
        col1, col2 = st.columns(2)
        nb_target = col1.number_input("NB Target (₹)", min_value=0, step=1000)
        nb_achieved = col2.number_input("NB Achieved (₹)", min_value=0, step=1000)

        col3, col4 = st.columns(2)
        collectible = col3.number_input("Collectible (₹)", min_value=0)
        collected = col4.number_input("Collected (₹)", min_value=0)

# MMLI + TAT + Activation
with st.container():
    with st.expander("🔧 Operational Metrics", expanded=False):
        col1, col2 = st.columns(2)
        mml_contribution = col1.number_input("MMLI (₹)", min_value=0)
        activation = col2.slider("Branch Activation %", 0, 100, 50)

        col3, col4, col5 = st.columns(3)
        stp = col3.number_input("STP TAT (days)", min_value=0)
        non_stp = col4.number_input("Non-STP TAT (days)", min_value=0)
        medical = col5.number_input("Medical TAT (days)", min_value=0)

# Policies Done
with st.container():
    policies = st.number_input("📑 No. of Policies Done", min_value=0)

# Product Achievements
with st.expander("📦 Product-wise Achievement (Optional)", expanded=False):
    product_achievements = []
    for i in range(1, 11):
        val = st.number_input(f"Product {i} (₹)", min_value=0, key=f"p{i}")
        product_achievements.append(val)

# Summary + Logic
st.markdown("---")
st.subheader("📊 Summary & Incentive")

nb_percent = (nb_achieved / nb_target) * 100 if nb_target > 0 else 0
persistency = (collected / collectible) * 100 if collectible > 0 else 0

st.markdown(f"- **NB % Achieved**: `{nb_percent:.2f}%`")
st.markdown(f"- **Persistency**: `{persistency:.2f}%`")
st.markdown(f"- **Total Product Achievement**: ₹{sum(product_achievements):,.0f}")
st.markdown(f"- **MMLI Contribution**: ₹{mml_contribution:,.0f}")
st.markdown(f"- **Activation**: `{activation}%`")
st.markdown(f"- **Policies Done**: `{policies}`")

# Incentive Logic
incentive = 0
message = ""
color = "gray"

if collectible == 0 or persistency < 70:
    message = "❌ Persistency below 70%. Not eligible for incentive."
    color = "#f44336"
elif nb_percent < 70:
    message = "⚠️ NB Achievement < 70%. No incentive."
    color = "#f57c00"
elif 70 <= nb_percent < 80:
    incentive = nb_achieved * 0.03
    message = f"✅ Eligible for 3% incentive = ₹{incentive:,.0f}"
    color = "#ffb300"
elif 80 <= nb_percent < 90:
    incentive = nb_achieved * 0.04
    message = f"✅ Eligible for 4% incentive = ₹{incentive:,.0f}"
    color = "#4caf50"
elif 90 <= nb_percent < 100:
    incentive = nb_achieved * 0.05
    message = f"✅ Eligible for 5% incentive = ₹{incentive:,.0f}"
    color = "#388e3c"
else:
    incentive = nb_achieved * 0.06
    message = f"🎉 Superstar! 6% incentive = ₹{incentive:,.0f}"
    color = "#2e7d32"
    st.balloons()

# Display Incentive Box
st.markdown(f'''
<div class="card" style="border-left-color: {color};">
  <strong>{message}</strong>
</div>
''', unsafe_allow_html=True)
