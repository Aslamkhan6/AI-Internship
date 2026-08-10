import streamlit as st

from src.predictor import Predictor


# ==========================================
# Page Configuration
# ==========================================

st.set_page_config(

    page_title="AI Fake News Detector",

    page_icon="📰",

    layout="wide"

)

# ==========================================
# Load Predictor
# ==========================================

predictor = Predictor()

# ==========================================
# Custom CSS
# ==========================================

st.markdown("""
<style>

.main{
    padding-top:20px;
}

.title{
    text-align:center;
    font-size:42px;
    font-weight:bold;
    color:#1f77b4;
}

.subtitle{
    text-align:center;
    font-size:18px;
    color:gray;
    margin-bottom:25px;
}

.real{
    background:#d4edda;
    color:#155724;
    padding:18px;
    border-radius:10px;
    font-size:22px;
    font-weight:bold;
}

.fake{
    background:#f8d7da;
    color:#721c24;
    padding:18px;
    border-radius:10px;
    font-size:22px;
    font-weight:bold;
}

.confidence{
    font-size:18px;
    color:#444;
    margin-top:10px;
}

</style>
""", unsafe_allow_html=True)

# ==========================================
# Sidebar
# ==========================================

st.sidebar.title("📌 Project")

st.sidebar.info("""

### AI Fake News Detection

This application predicts whether a news article is:

✅ Real News

❌ Fake News

Built Using:

- Python
- Scikit-Learn
- TF-IDF
- LinearSVC
- Streamlit

""")

# ==========================================
# Title
# ==========================================

st.markdown(
    '<div class="title">📰 AI Fake News Detection</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">Paste a news article below and let AI determine whether it is Real or Fake.</div>',
    unsafe_allow_html=True
)

# ==========================================
# Input
# ==========================================

article = st.text_area(

    "Enter News Article",

    height=300,

    placeholder="Paste the complete news article here..."

)

# ==========================================
# Buttons
# ==========================================

col1, col2 = st.columns(2)

with col1:

    predict_btn = st.button(
        "🔍 Analyze News",
        use_container_width=True
    )

with col2:

    clear_btn = st.button(
        "🗑 Clear",
        use_container_width=True
    )

if clear_btn:

    st.rerun()

# ==========================================
# Prediction
# ==========================================

if predict_btn:

    if article.strip() == "":

        st.warning("Please enter a news article.")

    else:

        with st.spinner("Analyzing..."):

            result = predictor.predict(article)

        prediction = result["prediction"]

        confidence = result["confidence"]

        if prediction.lower() == "real":

            st.markdown(

                f"""
                <div class="real">

                ✅ REAL NEWS

                </div>

                """,

                unsafe_allow_html=True

            )

        else:

            st.markdown(

                f"""

                <div class="fake">

                ❌ FAKE NEWS

                </div>

                """,

                unsafe_allow_html=True

            )

        st.markdown(

            f"""

            <div class="confidence">

            Confidence : <b>{confidence:.2f}%</b>

            </div>

            """,

            unsafe_allow_html=True

        )

# ==========================================
# Footer
# ==========================================

st.divider()

st.caption("AI Fake News Detection | Internship Project | Built with Streamlit")