# import streamlit as st
# import joblib
# import numpy as np

# # Load the trained model
# model = joblib.load('/home/bench/Documents/projects/Ad_Clickthrough_rate/Prediction/model/xgboost_model.pkl')

# # Title of the app
# st.title("Machine Learning Prediction App")

# # Instructions
# st.write("""
# ### Enter the features for prediction:
# Provide the required numerical input values.
# """)

# # Create input fields for features
# # Modify the number of inputs based on your model's expected input dimensions
# feature_inputs = []
# for i in range(5):  # Adjust '5' to the number of features your model expects
#     feature_value = st.number_input(f"Feature {i + 1}", step=0.1, format="%.2f")
#     feature_inputs.append(feature_value)

# # Prediction button
# if st.button("Predict"):
#     # Convert inputs into a NumPy array
#     features = np.array(feature_inputs).reshape(1, -1)

#     # Make prediction
#     try:
#         prediction = model.predict(features)
#         st.success(f"Prediction: {int(prediction[0])}")
#     except Exception as e:
#         st.error(f"An error occurred: {e}")
