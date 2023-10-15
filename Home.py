import streamlit as st
import pandas

st.set_page_config(layout="wide")
col1,col2 = st.columns(2)

with col1:
    st.image("images/photo.png", width=400)

with col2:
    st.title("Syed Asad Ali")
    content = """I ,Syed Asad Ali,am a dedicated and results-driven DevOps engineer with a passion for bridging the gap between development and operations to create efficient and reliable software delivery pipelines. With 1.5 years of experience in the field, I have honed my skills in several key areas."""
    st.info(content)

content2 = """Below you can find some of the apps that I built in Python. feel free to contact me at shezu30@gmail.com."""
st.write(content2)

col3,empty_col,col4 = st.columns([1.5,0.5,1.5])
df = pandas.read_csv("data.csv", sep=";")
with col3:
    for index,column in df[:10].iterrows():
        st.header(column["title"])
        st.write(column["description"])
        st.image("images/" + column["image"])
        st.write(f"[source code]({column['url']})")
with col4:
    for index,column in df[10:].iterrows():
        st.header(column["title"])
        st.write(column["description"])
        st.image("images/" + column["image"])
        st.write(f"[source code]({column['url']})")