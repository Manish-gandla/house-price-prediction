import pickle

# Load model
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

print("🏠 House Price Prediction")

# Take input
area = float(input("Enter area: "))
bedrooms = int(input("Enter bedrooms: "))
bathrooms = int(input("Enter bathrooms: "))

# Predict
prediction = model.predict([[area, bedrooms, bathrooms]])

print(f"💰 Predicted Price: {prediction[0]:.2f} lakhs")