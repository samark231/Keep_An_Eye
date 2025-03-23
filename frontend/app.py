import streamlit as st
import requests
import matplotlib.pyplot as plt
from gtts import gTTS
import os

# Streamlit UI
st.title("Company Sentiment Analysis")

# Input field for company name
company_name = st.text_input("Enter company name:", "")
BASE_URL = "http://127.0.0.1:5000/company"

# Initialize session state variables
if "final_sentiment" not in st.session_state:
    st.session_state.final_sentiment = None
if "audio_path" not in st.session_state:
    st.session_state.audio_path = None

# Function to fetch data from backend
def fetch_data(company):
    api_url = f"{BASE_URL}?company={company}"
    response = requests.get(api_url)
    
    if response.status_code == 200:
        return response.json()
    else:
        st.error("Failed to fetch data from the backend. Sometimes it happens. Please refresh.")
        return None

# Button to fetch data
if st.button("Analyze"):
    if company_name:
        data = fetch_data(company_name)

        if data:
            # Store final sentiment in session state
            st.session_state.final_sentiment = data['Final Sentiment Analysis']

            # Generate TTS audio only once
            tts = gTTS(st.session_state.final_sentiment)
            audio_file = "sentiment.mp3"
            tts.save(audio_file)
            st.session_state.audio_path = audio_file  # Store audio file path

            # Display final sentiment
            st.markdown("### Final Sentiment")
            st.markdown(f"**{st.session_state.final_sentiment}**")

            # Pie Chart for Sentiment Distribution
            st.markdown("### Sentiment Distribution")
            sentiment_data = data["Comparative Sentiment Score"]["Sentiment Distribution Score"]
            labels = list(sentiment_data.keys())
            sizes = list(sentiment_data.values())
            colors = ["red", "green", "yellow"]
            
            fig, ax = plt.subplots()
            ax.pie(sizes, labels=labels, autopct='%1.1f%%', colors=colors, startangle=90)
            ax.axis('equal')
            st.pyplot(fig)

            # Display Articles
            st.markdown("### News Articles")
            for article in data["Articles"]:
                with st.expander(f"{article['Title']}"):
                    st.markdown(f"**Source:** {article['Source']}")
                    st.markdown(f"**Summary:** {article['Summary']}")
                    st.markdown(f"[Read More]({article['Link']})")

    else:
        st.warning("Please enter a company name.")

# Read Sentiment button (keeps working even after analysis)
if st.session_state.final_sentiment and st.session_state.audio_path:
    if st.button("🔊 Read Sentiment"):
        st.audio(st.session_state.audio_path, format="audio/mp3")
