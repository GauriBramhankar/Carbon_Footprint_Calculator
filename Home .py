
import streamlit as st

# --- App Config ---
st.set_page_config(
    page_title="Green Tomorrow",
    page_icon="🌿",
    layout="centered"
)

# --- Custom Sidebar Logo + Background ---
st.sidebar.markdown(
    """
    <style>
        [data-testid="stSidebar"]::before {
            content: "";
            display: block;
            background-image: url('https://github.com/GauriBramhankar/Carbon_Footprint_Calculator/blob/main/GreenPrint_logo.png');
            background-size: 90% auto;
            background-repeat: no-repeat;
            background-position: center;
            height: 140px;
            margin: 1.5rem auto -4rem auto;
        }
        section[data-testid="stSidebar"] {
            background-color: #d6f5ec;
        }
        .stApp {
            background-color: white;
        }
    </style>
    """,
    unsafe_allow_html=True
)
# --- Page Title ---
st.title("Welcome to GreenPrint")
st.subheader("Your Personal Carbon Footprint Tracker")

# --- Intro Content ---
st.markdown("""

**GreenPrint** is a user-friendly tool that empowers you to measure the environmental impact of your daily activities
by calculating the carbon emissions associated with your lifestyle. It helps you understand how your choices contribute 
to greenhouse gas emissions. With this insight, GreenPrint offers a pathway to make more sustainable decisions and reduce 
your overall carbon footprint.

<br>

Whether you're just curious or committed to climate action, **GreenPrint** is here to support your journey.

---

### 🔍 What is a Carbon Footprint?

Your **carbon footprint** is the total amount of **greenhouse gases** released into the air because of your everyday activities.

Common activities like:

- 🏠 **Using energy at home** (heating, electricity)
- 🚗 **Getting around** (cars, buses, flights)
- 🍔 **What you eat** (especially meat and dairy)
- 🛍️ **What you buy and throw away** (clothes, electronics, waste)

Your footprint shows how much your actions contribute to climate change. By understanding your footprint, you can take steps to reduce it and make more sustainable choices!

---

### 🚨 Why It Matters

At **GreenPrint**, we believe that our planet is finite, and sustainability is crucial for our future. The consumption of resources leads to greenhouse gas emissions, which are responsible for global warming. These emissions contribute to environmental challenges such as:

- 🌊 Floods
- 🔥 Forest fires
- 🌵 Droughts
- ⚔️ Conflict
- 🌍 Ecological damage

<be>

The higher your carbon footprint, the more you contribute to these issues. By understanding your emissions, you can:

- 🌍 **Reduce your environmental impact**
- 💰 **Save money** through efficient choices
- 🌱 **Join the global effort** to fight climate change and protect the planet 


---

### 🛠️ How This App Works

1. Go to the **Profile** page and create your profile
2. Use the **Calculator** to enter details about your daily habits, get an estimate of your **annual carbon footprint**, and compare your score to **national and global averages**.  
3. Go to **Breakdown** page to see more details about your carbon footprint and receive personalized suggestions on how to **reduce** it.
4. Ask your questions from **GreenPrint AI** for real-time advice on reducing your carbon footprint.

---

### 🌿 Ready to make a difference?

Let's get started! **Click Next →** to begin creating your profile and take the first step in reducing your carbon footprint.
""", unsafe_allow_html=True)

# --- Simulated Redirect to Profile using query param ---
col1, col2, col3 = st.columns([1, 6, 1])
with col2:
    if st.button("Next →", use_container_width=False):
        st.experimental_set_query_params(page="Profile")
        st.markdown('<meta http-equiv="refresh" content="0;url=./Profile">', unsafe_allow_html=True)
