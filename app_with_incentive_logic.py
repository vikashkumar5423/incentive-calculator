
import streamlit as st

st.set_page_config(page_title="Incentive Calculator", layout="centered")

st.title("🎯 Incentive Input Form")

# Salesperson Info
with st.container():
    col1, col2 = st.columns(2)
    name = col1.text_input("Name")
    month = col2.selectbox("Month", [
        "Jan", "Feb", "Mar", "Apr", "May", "Jun",
        "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"
    ])

# New Business & Persistency
with st.container():
    st.subheader("📈 Performance Metrics")
    col1, col2 = st.columns(2)
    nb_target = col1.number_input("NB Target", min_value=0, step=1000)
    nb_achieved = col2.number_input("NB Achieved", min_value=0, step=1000)

    col3, col4 = st.columns(2)
    collectible = col3.number_input("Collectible", min_value=0)
    collected = col4.number_input("Collected", min_value=0)

# Boosters
with st.container():
    st.subheader("🔧 Booster")
    col1, col2 = st.columns(2)
    mml_contribution = col1.number_input("Lead MM (₹)", min_value=0)
    activation = col2.slider("Branch Activation %", 0, 100, 50)

    col3, col4, col5 = st.columns(3)
    stp = col3.number_input("STP TAT", min_value=0)
    non_stp = col4.number_input("Non-STP TAT", min_value=0)
    medical = col5.number_input("Medical TAT", min_value=0)

# Policies Done
policies = st.number_input("No. of Policies", min_value=0)

# Product Achievements
with st.expander("📦 Product-wise Achievement (Optional)", expanded=False):
    product_achievements = []
    for i in range(1, 11):
        val = st.number_input(f"Product {i}", min_value=0, key=f"p{i}")
        product_achievements.append(val)

# Summary + Logic
st.subheader("📊 Summary")

nb_percent = (nb_achieved / nb_target) * 100 if nb_target > 0 else 0
persistency = (collected / collectible) * 100 if collectible > 0 else 0

st.write(f"**NB % Achieved:** {nb_percent:.2f}%")
st.write(f"**Persistency:** {persistency:.2f}%")
st.write(f"**Total Product Achievement:** ₹{sum(product_achievements):,.0f}")
st.write(f"**MMLI Contribution:** ₹{mml_contribution:,.0f}")
st.write(f"**Activation:** {activation}%")
st.write(f"**Policies:** {policies}")

# Incentive Logic
st.subheader("💰 Incentive Eligibility")

if collectible == 0 or persistency < 70:
    st.error("❌ Persistency below 70%. Not eligible for incentive.")
    incentive = 0
else:
    if nb_percent < 70:
        incentive = 0
        st.warning("⚠️ Achievement < 70%. No incentive.")
    elif 70 <= nb_percent < 80:
        incentive = nb_achieved * 0.03
        st.success(f"✅ Eligible: 3% of NB = ₹{incentive:,.0f}")
    elif 80 <= nb_percent < 90:
        incentive = nb_achieved * 0.04
        st.success(f"✅ Eligible: 4% of NB = ₹{incentive:,.0f}")
    elif 90 <= nb_percent < 100:
        incentive = nb_achieved * 0.05
        st.success(f"✅ Eligible: 5% of NB = ₹{incentive:,.0f}")
    else:
        incentive = nb_achieved * 0.06
        st.balloons()
        st.success(f"🎉 Superstar! Eligible: 6% of NB = ₹{incentive:,.0f}")
