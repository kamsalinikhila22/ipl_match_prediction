
import streamlit as st
from catboost import CatBoostClassifier
import joblib

# Load the trained CatBoost model
model = CatBoostClassifier()
model.load_model("catboost_model.cbm")

def predict_match(features):
    # Perform prediction
    prediction = model.predict([features])[0]
    return prediction


def main():
    st.title("IPL Match Prediction")
    html_temp = """
    <div style="background-image: url('http://www.aajkikhabar.com/en/wp-content/uploads/2019/02/IPL-Tournament-1-1.jpg'); 
                background-size: cover; 
                padding: 10px; 
                height: 100vh;">
        <h2 style="color:white;text-align:center;">TATA IPL MATCH PREDICTION</h2>
    </div>
    """
    st.markdown(html_temp, unsafe_allow_html=True)


   
    
    # Add input fields for each feature
    features = {}
    for column in ['city', 'team1', 'team2', 'toss_winner', 'toss_decision', 'result',
       'venue']:
        features[column] = st.text_input(column)


    if st.button("Predict"):
        # Perform prediction
        input_features = list(features.values())
        prediction = predict_match(input_features)
        st.write(f"The winner of this match is: {prediction}")

if __name__ == "__main__":
    main()
