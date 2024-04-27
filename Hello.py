import time

import streamlit as st
from datetime import datetime
import numpy as np

st.set_page_config(
    page_title="Hello",
    page_icon="👋",
)

st.write("# Welcome to Streamlit! 👋")

st.sidebar.success("Select a demo above.")

#
st.divider()

# st.code("""
# progress_bar = st.sidebar.progress(0)
# status_text = st.sidebar.empty()
# last_rows = np.random.randn(1, 1)
# chart = st.line_chart(last_rows)
#
# for i in range(1, 101):
#     new_rows = last_rows[-1, :] + np.random.randn(5, 1).cumsum(axis=0)
#     status_text.text("%i%% Complete" % i)
#     chart.add_rows(new_rows)
#     progress_bar.progress(i)
#     last_rows = new_rows
#     time.sleep(0.05)
#
# progress_bar.empty()
#     """
#         )


df = st.data_editor({'name': 'Peter', 'age': 30, 'gender': 'Male'})
if st.button('show result'):
    st.write(df)
else:
    st.write('what you input can be changed')

options = st.multiselect(
    'What are your favorite colors',
    ['Green', 'Yellow', 'Red', 'Blue'],
    ['Yellow', 'Red'])

st.write('You selected:', options)

start_time = st.slider(
    "When do you start?",
    value=datetime(2020, 1, 1, 9, 30),
    format="MM/DD/YY - hh:mm")
st.write("Start time:", start_time)

st.page_link('./pages/1_📈_Plotting_Demo.py', label='Plotting demo', icon="😁")

uploaded_files = st.file_uploader("Choose a CSV file", accept_multiple_files=True)
for uploaded_file in uploaded_files:
    bytes_data = uploaded_file.read()
    st.write("filename:", uploaded_file.name)
    with open(f'{uploaded_file.name}', 'wb') as f:
        f.write(bytes_data)

# picture = st.camera_input("Take a picture")
# if picture:
#     st.image(picture)

color = st.color_picker('Pick A Color', '#00f900')
st.write('The current color is', color)

audio_file = open('匆匆那年.mp3', 'rb')
audio_bytes = audio_file.read()

st.audio(audio_bytes, format='audio/ogg')


# with st.spinner('Wait for it...'):
#     time.sleep(5)
# st.success('Done!')

# with st.empty():
#     for seconds in range(10):
#         st.write(f"⏳ {seconds} seconds have passed")
#         time.sleep(1)
#     st.write("✔️ 1 minute over!")


def cook_breakfast():
    msg = st.toast('Gathering ingredients...')
    time.sleep(1)
    msg.toast('Cooking...')
    time.sleep(1)
    msg.toast('Ready!', icon="🥞")


if st.button('Cook breakfast'):
    cook_breakfast()


def stream_data(input_data):
    for word in input_data.split(" "):
        yield word + " "
        time.sleep(0.3)


with st.form("my_form"):
    submitted = st.form_submit_button("Submit")
    if submitted:
        st.write_stream(stream_data("streamlit.errors.StreamlitAPIException: `st.chat_input()` can't be used in a `st.form()`."))
