import streamlit as st
import tempfile
import cv2
import mediapipe as mp
import os

st.title("GateSnap AI – Pose Analysis")

uploaded_file = st.file_uploader("Upload your 6-second iPhone video", type=["mp4", "mov", "avi"])

if uploaded_file is not None:
    tfile = tempfile.NamedTemporaryFile(delete=False)
    tfile.write(uploaded_file.read())

    st.video(tfile.name)

    st.write("Analyzing...")

    mp_pose = mp.solutions.pose
    pose = mp_pose.Pose(static_image_mode=False, min_detection_confidence=0.5)

    cap = cv2.VideoCapture(tfile.name)
    frame_count = 0

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = pose.process(frame_rgb)

        if results.pose_landmarks:
            mp.solutions.drawing_utils.draw_landmarks(
                frame, results.pose_landmarks, mp_pose.POSE_CONNECTIONS)

        if frame_count < 3:
            st.image(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB), caption=f"Frame {frame_count + 1}")

        frame_count += 1

    cap.release()
    pose.close()
    os.remove(tfile.name)
    st.success("Analysis complete.")
