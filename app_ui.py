import streamlit as st
import pickle
import time

# Page configuration
st.set_page_config(
    page_title="House Price Predictor",
    page_icon="🏠",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for animations and styling
st.markdown("""
<style>
@keyframes fadeIn {
    from { opacity: 0; transform: translateY(20px); }
    to { opacity: 1; transform: translateY(0); }
}

@keyframes pulse {
    0% { transform: scale(1); }
    50% { transform: scale(1.05); }
    100% { transform: scale(1); }
}

.fade-in {
    animation: fadeIn 0.8s ease-out;
}

.pulse {
    animation: pulse 2s infinite;
}

.stButton>button {
    background: linear-gradient(45deg, #FF6B6B, #4ECDC4);
    color: white;
    border: none;
    padding: 12px 24px;
    border-radius: 25px;
    font-weight: bold;
    transition: all 0.3s ease;
}

.stButton>button:hover {
    transform: translateY(-2px);
    box-shadow: 0 8px 15px rgba(0,0,0,0.2);
}

.card {
    background: white;
    border-radius: 15px;
    padding: 20px;
    box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    margin: 10px 0;
    transition: transform 0.3s ease;
}

.card:hover {
    transform: translateY(-5px);
}

.sidebar .stNumberInput {
    margin-bottom: 20px;
}

.stSuccess {
    background: linear-gradient(45deg, #56ab2f, #a8e6cf);
    color: white;
    border-radius: 10px;
    padding: 15px;
    animation: fadeIn 0.5s ease-out;
}
</style>
""", unsafe_allow_html=True)

# Load trained model
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

# Title with animation
st.markdown('<h1 class="fade-in pulse">🏠 House Price Prediction App</h1>', unsafe_allow_html=True)
st.markdown('<p class="fade-in">Discover the estimated value of your dream home with our advanced AI model!</p>', unsafe_allow_html=True)

# Sidebar for inputs
with st.sidebar:
    st.header("📋 Property Details")
    st.markdown("Enter the specifications of the house:")

    col1, col2 = st.columns(2)
    with col1:
        area = st.number_input("Area (sq ft)", min_value=500, max_value=5000, step=100, value=1500)
    with col2:
        bedrooms = st.number_input("Bedrooms", min_value=1, max_value=10, step=1, value=3)

    bathrooms = st.number_input("Bathrooms", min_value=1, max_value=10, step=1, value=2)

    st.markdown("---")
    predict_button = st.button("🚀 Predict Price", use_container_width=True)

# Main content area
if predict_button:
    with st.spinner("Analyzing property data..."):
        progress_bar = st.progress(0)
        for i in range(100):
            time.sleep(0.01)
            progress_bar.progress(i + 1)

    prediction = model.predict([[area, bedrooms, bathrooms]])

    # Display result in a card-like container
    st.markdown(f"""
    <div class="card fade-in">
        <h2 style="color: #FF6B6B; text-align: center;">💰 Estimated Price</h2>
        <h1 style="color: #4ECDC4; text-align: center; font-size: 3em;">₹{prediction[0]:,.2f} lakhs</h1>
        <p style="text-align: center; color: #666;">Based on {area} sq ft, {bedrooms} bedrooms, and {bathrooms} bathrooms</p>
    </div>
    """, unsafe_allow_html=True)

    # Additional insights
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Area Factor", f"{area/1000:.1f}K sq ft")
    with col2:
        st.metric("Bedroom Impact", f"{bedrooms * 0.5:.1f} lakhs")
    with col3:
        st.metric("Bathroom Boost", f"{bathrooms * 0.3:.1f} lakhs")

else:
    # Welcome message
    st.markdown("""
    <div class="card fade-in">
        <h3>Welcome to House Price Predictor! 🏡</h3>
        <p>Enter your property details in the sidebar and click 'Predict Price' to get an instant estimate powered by machine learning.</p>
        <ul>
            <li>📊 Accurate predictions based on historical data</li>
            <li>⚡ Instant results with beautiful animations</li>
            <li>🎨 Modern, responsive design</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)