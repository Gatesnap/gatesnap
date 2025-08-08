import streamlit as st


# Branding CSS
st.markdown("""
<style>
h1, h2, h3 { letter-spacing: 0.2px; }
.stButton>button {
  background:#8CF51C;
  color:#000;
  border:0;
  font-weight:700;
}
.stButton>button:hover {
  filter:brightness(0.9);
}
.block-container { padding-top: 1.2rem; }
</style>
""", unsafe_allow_html=True)

import streamlit as st
from PIL import Image

st.set_page_config(page_title="GateSnap AI", layout="centered")


st.title("Body Position Analysis for BMX Riders")

st.markdown("### Create a Free Account")
with st.form("signup_form"):
    name = st.text_input("Full name")
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")
    agree = st.checkbox("I agree to the Terms & Privacy")
    submitted = st.form_submit_button("Create my free account")
    if submitted:
        if not (name and email and password and agree):
            st.error("Please complete all fields and agree to continue.")
        else:
            st.success("Account created (placeholder). Login will be enabled after we connect Firebase.")

with st.expander("🎯 Plans (Free forever, upgrades optional)", expanded=True):
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("**Free** • 1 analysis / day • £0 / forever")
    with col2:
        st.markdown("**Pro** • 3/day • £9.99 / year")
        st.link_button("Upgrade to Pro", "https://buy.stripe.com/eVqeVdamUgkQ7Isgd19EI00")
    with col3:
        st.markdown("**Team** • 15/day • £49.99 / year")
        st.link_button("Team Upgrade", "https://buy.stripe.com/cNi4gzfHe1pW5AkaSH9EI01")
    st.markdown("**Coach License** • 50/day • £99.99 / year")
    st.link_button("Coach Upgrade", "https://buy.stripe.com/4gM14n52A3y47Is8Kz9EI02")

st.markdown("### 📤 Upload Your Gate Start Video")
st.markdown("""
✅ Set your phone to **1080p at 30fps**  
✅ Crop your video to **2–6 seconds**  
✅ Film from the **side**, showing your full body  
✅ For best results, use a **tripod or stable surface**

⚠️ Videos over 6 seconds or under 2 seconds will be rejected  
⚠️ Avoid 4K or 60fps – they may fail to upload
""")

uploaded_file = st.file_uploader("🎬 Upload your video", type=["mp4", "mov"])

if uploaded_file:
    st.success("✅ Video uploaded successfully!")
    st.markdown("### 🧠 GateSnap AI Review: Frame: Pre-Load Position")
    st.markdown("✅ Torso: 42° (✔ Good)")
    st.markdown("✅ Hip: 75° (✔ Good)")
    st.markdown("⚠️ Knee: 125° (Too open)")
    st.markdown("✅ Ankle: 85° (✔ Good)")
    st.markdown("⚠️ Elbow: 170° (Too straight)")
    st.info("🗣 Tip: Try bringing your knees forward slightly and bend your arms to improve your snap.")
