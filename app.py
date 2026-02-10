import streamlit as st
import pandas as pd

st.title("startup Dashboard")
st.header("I am Learning Streamlit")
st.subheader("I am loving It")
st.write("This is a normal Text")

st.markdown("""
    - Munazza Zaidi
    - Ashar Abbas
    - Ashab Abbas

""")

st.code("""
    def Greetings(greet):
        return greet
    Greetings("hello")
    
""")

st.latex("(x+y)^2 = x^2 + y^2 + 2xy")

students = pd.DataFrame(
    {
        'Name': ["Munazza", "Ashar", "Ashab"],
        'Marks' : [95, 98, 99],
        'Package': [10,11,12]
    }
)

st.dataframe(students)
col1, col2, col3 = st.columns(3)

with col1:
    st.metric('Revenue', '3L', '3%')
with col2:
    st.metric('Registrations', '100', '-20%')
with col3:
    st.metric('Visitors', '1000', '+50%')


st.json(
{
        'Name': ["Munazza", "Ashar", "Ashab"],
        'Marks' : [95, 98, 99],
        'Package': [10,11,12]
    }

)
st.sidebar.title("Sidebar's title")

st.success("Login Succesful")
st.info("it's getting better")
st.warning("Login failed")
st.error("Don't click this button")
email=st.text_input("Enter Email")
date= st.date_input("Enter date")
st.toggle("enable This")

email= st.text_input("Enter Your registered email")
password = st.text_input("Enter your password")
Gender= st.selectbox("Select Your gender", ["Male", "Female", "Others"])

btn=st.button("Login Karo Yaar!")

if btn:
    if email== "mzaidi604@gmail.com" and password == '1234':
        st.write("you are", Gender)
        st.balloons()
    else:
        st.error("Either email or password is incorrect")
file = st.file_uploader("Upload Your csv File")
if file is not None:
    df=pd.read_csv(file)
    st.dataframe(df.describe())