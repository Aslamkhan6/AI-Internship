import os
import joblib
import streamlit as st
from sklearn.model_selection import train_test_split

from src.config import MODEL_DIR
from src.datasets import Emotiondataset
from src.Emotion_prediction import EmotionPredictor
from src.feature_extraction import FeatureExtractor
from src.preproces import Preprocessor
from src.train_model import Trainmodel

MODEL_PATH = os.path.join(MODEL_DIR, "emotion_model.joblib")
VECTORIZER_PATH = os.path.join(MODEL_DIR, "emotion_vectorizer.joblib")

st.set_page_config(page_title="Emotion Detector", page_icon="😊", layout="centered")

st.markdown(
    """
    <style>
    .block-container {
        padding-top: 1.5rem;
        padding-bottom: 2rem;
    }
    .title {
        font-size: 2.2rem;
        font-weight: 700;

        color: #124e8c;
        margin-bottom: 0.2rem;
    }
    .subtitle {
        font-size: 1rem;
        color: #4b5563;
        margin-bottom: 1rem;
    }
    .card {
        background: linear-gradient(135deg, #f8fafc, #eef2ff);
        padding: 1rem 1.2rem;
        border-radius: 14px;
        border: 1px solid #e5e7eb;
        box-shadow: 0 2px 8px rgba(0,0,0,0.04);
        color: #4b5563;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown('<div class="title">😊 Emotion Detector</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Type a sentence and discover the emotion behind it.</div>', unsafe_allow_html=True)

col1, col2 = st.columns([2, 1])
with col1:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    text = st.text_area(
        "Your text",
        
        placeholder="Example: I feel so happy today!",
        height=170,
    )
    st.markdown('</div>', unsafe_allow_html=True)

with col2:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown("### Quick Info" )
    st.write("- Fast text prediction")
    st.write("- Trained on emotion-text data")
    st.write("- Works with short sentences")
    st.markdown('</div>', unsafe_allow_html=True)


@st.cache_resource
def load_or_train_model():
    if os.path.exists(MODEL_PATH) and os.path.exists(VECTORIZER_PATH):
        return EmotionPredictor(MODEL_PATH, VECTORIZER_PATH)

    emotion_data = Emotiondataset()
    data = emotion_data.loaddata()
    texts = data["text"].astype(str).tolist()
    labels = data["emotion"]

    clean_text = []
    for sentence in texts:
        process = Preprocessor(sentence)
        clean_text.append(" ".join(process.preprocess()))

    feature = FeatureExtractor(clean_text)
    converted_data = feature.fit_transform()

    X_train, X_test, Y_train, Y_test = train_test_split(
        converted_data,
        labels,
        test_size=0.2,
        random_state=42,
    )

    trainer = Trainmodel()
    trainer.train(X_train, Y_train)
    accuracy = trainer.test(X_test, Y_test)
    trainer.save_model(MODEL_PATH)
    joblib.dump(feature.vectorizer, VECTORIZER_PATH)

    st.success(f"Model trained successfully with accuracy: {accuracy:.2%}")
    return EmotionPredictor(MODEL_PATH, VECTORIZER_PATH)


predictor = load_or_train_model()

if st.button("Predict Emotion", use_container_width=True):
    if text.strip():
        emotion = predictor.predict_emottion(text)
        st.markdown(
            f"""
            <div class="card" style="margin-top: 0.8rem; background: linear-gradient(135deg, #ecfeff, #eff6ff);">
                <h3 style="margin-bottom: 0.3rem;">Prediction</h3>
                <p style="font-size: 1.15rem; font-weight: 600; color: #1d4ed8; margin: 0;">{emotion}</p>
            </div>
            """,
            unsafe_allow_html=True,
        )
    else:
        st.warning("Please enter some text first.")
