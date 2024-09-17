import streamlit as st
import pandas as pd
from src.pipeline.predict_pipeline import PredictPipeline, CustomData
from src.components.data_ingestion import DataIngestion

# Enhanced custom styling
st.markdown(
    """
    <style>
    .main {
        background-color: #f8f9fa;
        color: #212529;
    }
    .stButton>button {
        background-color: #007bff;
        color: white;
        border-radius: 5px;
        font-size: 16px;
        padding: 10px 24px;
        transition: all 0.3s;
    }
    .stButton>button:hover {
        background-color: #0056b3;
    }
    h1 {
        font-family: 'Helvetica Neue', sans-serif;
        font-size: 36px;
        font-weight: 700;
        color: #007bff;
        text-align: center;
        margin-bottom: 30px;
    }
    h2 {
        color: #007bff;
        font-family: 'Helvetica Neue', sans-serif;
        font-weight: 600;
    }
    .stExpander {
        background-color: #e9ecef;
        border-radius: 5px;
        margin-bottom: 20px;
    }
    footer {
        background-color: #f8f9fa;
        text-align: center;
        padding: 20px 0;
        font-size: 14px;
        color: #6c757d;
        border-top: 1px solid #dee2e6;
    }
    .feature-info {
        font-size: 14px;
        color: #6c757d;
        margin-top: 5px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Initialize DataIngestion and load feature statistics
data_ingestion = DataIngestion()
stats = data_ingestion.get_feature_statistics()

# App title and description
st.title("🚀 Software Defects Prediction App")
st.markdown("""
    This app predicts the likelihood of software defects based on various code metrics.
    Adjust the sliders below to input your code's characteristics and get a prediction.
""")

# Use columns for better layout
st.header("Enter the feature values using sliders:")

# Distribute sliders into 3 columns for better organization
col1, col2, col3 = st.columns(3)

with col1:
    loc = st.slider("loc (Lines of Code)", 
                    min_value=float(stats.loc['loc', 'min']), 
                    max_value=float(stats.loc['loc', 'max']), 
                    value=float(stats.loc['loc', 'midrange']))
    st.markdown('<p class="feature-info">Lines of Code: Total number of lines in the source code.</p>', unsafe_allow_html=True)
    vg = st.slider("v(g) (Cyclomatic Complexity)", 
                   min_value=float(stats.loc['v(g)', 'min']), 
                   max_value=float(stats.loc['v(g)', 'max']), 
                   value=float(stats.loc['v(g)', 'midrange']))
    st.markdown('<p class="feature-info">Cyclomatic Complexity: Measure of the code\'s structural complexity.</p>', unsafe_allow_html=True)
    evg = st.slider("ev(g) (Essential Complexity)", 
                    min_value=float(stats.loc['ev(g)', 'min']), 
                    max_value=float(stats.loc['ev(g)', 'max']), 
                    value=float(stats.loc['ev(g)', 'midrange']))
    st.markdown('<p class="feature-info">Essential Complexity: Measure of the code\'s unstructuredness.</p>', unsafe_allow_html=True)

with col2:
    ivg = st.slider("iv(g) (Design Complexity)", 
                    min_value=float(stats.loc['iv(g)', 'min']), 
                    max_value=float(stats.loc['iv(g)', 'max']), 
                    value=float(stats.loc['iv(g)', 'midrange']))
    n = st.slider("n (Halstead Length)", 
                  min_value=float(stats.loc['n', 'min']), 
                  max_value=float(stats.loc['n', 'max']), 
                  value=float(stats.loc['n', 'midrange']))
    v = st.slider("v (Halstead Volume)", 
                  min_value=float(stats.loc['v', 'min']), 
                  max_value=float(stats.loc['v', 'max']), 
                  value=float(stats.loc['v', 'midrange']))
    l = st.slider("l (Halstead Level)", 
                  min_value=float(stats.loc['l', 'min']), 
                  max_value=float(stats.loc['l', 'max']), 
                  value=float(stats.loc['l', 'midrange']))

with col3:
    d = st.slider("d (Halstead Difficulty)", 
                  min_value=float(stats.loc['d', 'min']), 
                  max_value=float(stats.loc['d', 'max']), 
                  value=float(stats.loc['d', 'midrange']))
    i = st.slider("i (Halstead Intelligence)", 
                  min_value=float(stats.loc['i', 'min']), 
                  max_value=float(stats.loc['i', 'max']), 
                  value=float(stats.loc['i', 'midrange']))
    e = st.slider("e (Halstead Effort)", 
                  min_value=float(stats.loc['e', 'min']), 
                  max_value=float(stats.loc['e', 'max']), 
                  value=float(stats.loc['e', 'midrange']))

# More sliders organized under an expander for better layout
with st.expander("Advanced Features"):
    lOCode = st.slider("lOCode (Logical lines of code)", 
                       min_value=float(stats.loc['lOCode', 'min']), 
                       max_value=float(stats.loc['lOCode', 'max']), 
                       value=float(stats.loc['lOCode', 'midrange']))
    lOComment = st.slider("lOComment (Lines of comments)", 
                          min_value=float(stats.loc['lOComment', 'min']), 
                          max_value=float(stats.loc['lOComment', 'max']), 
                          value=float(stats.loc['lOComment', 'midrange']))
    lOBlank = st.slider("lOBlank (Blank lines)", 
                        min_value=float(stats.loc['lOBlank', 'min']), 
                        max_value=float(stats.loc['lOBlank', 'max']), 
                        value=float(stats.loc['lOBlank', 'midrange']))
    locCodeAndComment = st.slider("locCodeAndComment (Lines of code and comments)", 
                                  min_value=float(stats.loc['locCodeAndComment', 'min']), 
                                  max_value=float(stats.loc['locCodeAndComment', 'max']), 
                                  value=float(stats.loc['locCodeAndComment', 'midrange']))
    uniq_Op = st.slider("uniq_Op (Unique Operators)", 
                        min_value=float(stats.loc['uniq_Op', 'min']), 
                        max_value=float(stats.loc['uniq_Op', 'max']), 
                        value=float(stats.loc['uniq_Op', 'midrange']))
    uniq_Opnd = st.slider("uniq_Opnd (Unique Operands)", 
                          min_value=float(stats.loc['uniq_Opnd', 'min']), 
                          max_value=float(stats.loc['uniq_Opnd', 'max']), 
                          value=float(stats.loc['uniq_Opnd', 'midrange']))
    total_Op = st.slider("total_Op (Total Operators)", 
                         min_value=float(stats.loc['total_Op', 'min']), 
                         max_value=float(stats.loc['total_Op', 'max']), 
                         value=float(stats.loc['total_Op', 'midrange']))
    total_Opnd = st.slider("total_Opnd (Total Operands)", 
                           min_value=float(stats.loc['total_Opnd', 'min']), 
                           max_value=float(stats.loc['total_Opnd', 'max']), 
                           value=float(stats.loc['total_Opnd', 'midrange']))
    branchCount = st.slider("branchCount (Branches Count)", 
                            min_value=float(stats.loc['branchCount', 'min']), 
                            max_value=float(stats.loc['branchCount', 'max']), 
                            value=float(stats.loc['branchCount', 'midrange']))
    b = st.slider("b (Halstead Bugs)", 
                  min_value=float(stats.loc['b', 'min']), 
                  max_value=float(stats.loc['b', 'max']), 
                  value=float(stats.loc['b', 'midrange']))
    t = st.slider("t (Halstead Time)", 
                  min_value=float(stats.loc['t', 'min']), 
                  max_value=float(stats.loc['t', 'max']), 
                  value=float(stats.loc['t', 'midrange']))

# Prediction section
st.header("Make a Prediction")
st.markdown("Click the button below to predict the likelihood of software defects based on the input values.")

if st.button("Predict Defects"):
    # Create a CustomData instance
    custom_data = CustomData(
        loc=loc,
        vg=vg,
        evg=evg,
        ivg=ivg,
        n=n,
        v=v,
        l=l,
        d=d,
        i=i,
        e=e,
        b=b,  # Added b (Halstead Bugs)
        t=t,  # Added t (Halstead Time)
        lOCode=lOCode,
        lOComment=lOComment,
        lOBlank=lOBlank,
        locCodeAndComment=locCodeAndComment,
        uniq_Op=uniq_Op,
        uniq_Opnd=uniq_Opnd,
        total_Op=total_Op,
        total_Opnd=total_Opnd,
        branchCount=branchCount
    )


    # Get the data as a DataFrame
    data = custom_data.get_data_as_data_frame()

    # Initialize PredictPipeline
    predict_pipeline = PredictPipeline()

    # Make the prediction
    try:
        prediction = predict_pipeline.predict(data)
        if prediction[0] == 1:
            st.error("⚠️ High likelihood of defects detected!")
            st.markdown("Consider reviewing and refactoring the code to reduce complexity and improve maintainability.")
        else:
            st.success("✅ Low likelihood of defects detected.")
            st.markdown("The code appears to be well-structured, but continuous monitoring is recommended.")
    except Exception as e:
        st.error(f"Error: {e}")

# Add an information section
st.header("About Software Defect Prediction")
st.markdown("""
    Software defect prediction is a crucial aspect of quality assurance in software development. 
    It helps identify potential issues early in the development process, saving time and resources.
    This model uses various code metrics to estimate the likelihood of defects in a given piece of software.
""")

# Enhanced footer
st.markdown("""
    <footer>
    <p>Developed by Theodoros Eleftheriou | <a href="https://github.com/yourusername">GitHub</a> | <a href="https://linkedin.com/in/yourusername">LinkedIn</a></p>
    <p>© 2023 Software Defects Prediction App. All rights reserved.</p>
    </footer>
    """, unsafe_allow_html=True)