import streamlit as st

st.set_page_config(layout="wide")
col1,col2 = st.columns(2)

with col1:
    st.image("images/photo.png", width=400)

with col2:
    st.title("Syed Asad Ali")
    content = """I ,Syed Asad Ali,am a dedicated and results-driven DevOps engineer with a passion for bridging the gap between development and operations to create efficient and reliable software delivery pipelines. With 1.5 years of experience in the field, I have honed my skills in several key areas."""
    st.info(content)