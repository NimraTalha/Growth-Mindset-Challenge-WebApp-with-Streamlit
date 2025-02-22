import streamlit as st  
import random  

# Page Configuration  
st.set_page_config(page_title="Growth Mindset Project", page_icon="🌱", layout="centered")  

# Title Section  
st.title("🚀 Growth Mindset AI Project")  
st.header("Welcome to Your Growth Journey! 🌟")  
st.write("Embrace challenges, learn from mistakes, and unlock your full potential. "
         "This AI-powered app helps you build a growth mindset with reflection, challenges, and achievements! 💡")  

st.divider()  

# Random Quote Generator  
quotes = [
    "Success is not final, failure is not fatal: it is the courage to continue that counts. – Winston Churchill",
    "You are never too old to set another goal or to dream a new dream. – C.S. Lewis",
    "Mistakes are proof that you are trying. – Unknown",
    "Believe you can and you’re halfway there. – Theodore Roosevelt",
    "The only limit to our realization of tomorrow is our doubts of today. – Franklin D. Roosevelt",
    "Strive for progress, not perfection. – Unknown"
]

st.subheader("📖 Today's Growth Mindset Quote")
st.info(random.choice(quotes))

st.divider()

# Challenge Input  
st.subheader("🎯 What's Your Challenge Today?")
user_input = st.text_input("Describe a challenge you're facing:")

if user_input:  
    st.success(f"You are facing: **{user_input}**. Keep pushing towards your goal! 💪")  
else:  
    st.warning("Tell us about your challenge to get started!")  

st.divider()

# Reflection Section  
st.subheader("📝 Reflect On Your Learning")  
reflection = st.text_area("Write your reflections here")  

if reflection:  
    st.balloons()  # Fun animation  
    st.success(f"🌟 Insight from your reflection: {reflection}")  
else:  
    st.info("Great! Reflecting on your experiences helps you grow. 🌱")  

st.divider()

# Achievement Section  
st.subheader("🏆 Your Achievements")  
achievements = st.text_area("Write about what you've accomplished today!")  

if achievements:  
    st.snow()  # Fun animation  
    st.success(f"🎉 Awesome! You achieved: {achievements} 🚀 Keep it up!")  

st.divider()

# Encouragement Section  
st.subheader("💡 Daily Encouragement")  
st.write("**Remember:** Every challenge you overcome makes you stronger! 💪🚀")  

st.divider()

# Stylish Sticky Footer  
st.markdown("""
    <style>
        .footer {
            position: fixed;
            bottom: 0;
            width: 100%;
            background-color: #262730;
            color: white;
            text-align: center;
            padding: 10px;
        }
    </style>
    <div class="footer">
        🌟 Made with ❤️ by <b>Nimra Talha</b> | Stay motivated and keep growing! 🚀
    </div>
""", unsafe_allow_html=True)
