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

# Load and display logo


st.title("Body Position Analysis for BMX Riders")

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
