import streamlit as st

st.title('Hello World!')
st.write('This is a Streamlit app.')
st.info('This is an info message.')

input = st.text_input('Please enter your name:')

if input:
     st.write('Hello', input)

button = st.button('display message')
datainput=st.date_input('##Please enter your date:')
if datainput:
    st.write('Data:',datainput)
if button:
    st.write('Streamlit is great!')     




# toggle

isToggle=st.toggle('Hide download button', True)
if isToggle:
    st.header('Download latest file')
    downloadbtn=st.download_button('Download', 'Hello World!', 'a.txt', 'text/plain')