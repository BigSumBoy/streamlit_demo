import streamlit as st
import numpy as np
import pandas as pd
import time

DATE_COLUMN = 'date/time'
DATA_URL = ('https://s3-us-west-2.amazonaws.com/'
         'streamlit-demo-data/uber-raw-data-sep14.csv.gz')
# @st.cache_data
# def load_data(nrows):
#     data = pd.read_csv(DATA_URL, nrows=nrows)
#     lowercase = lambda x: str(x).lower()
#     data.rename(lowercase, axis='columns', inplace=True)
#     data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])
#     return data

st.title("Welcome to my app")

# data_load_state = st.text('Loading data...')
# data = load_data(10000)
# data_load_state.text('Loading data...done!')

# if st.checkbox('Show raw data'):
#     st.subheader('Raw data')
#     st.write(data)
#
# st.subheader('Number of pickups by hour')
# hist_values = np.histogram(
#     data[DATE_COLUMN].dt.hour, bins=24, range=(0,24))[0]
# st.bar_chart(hist_values)
#
# # st.subheader('Map of all pickups')
# # st.map(data)
# hour_to_filter = st.slider('hour', 0, 23, 17)
# filtered_data = data[data[DATE_COLUMN].dt.hour == hour_to_filter]
# st.subheader(f'Map of all pickups at {hour_to_filter}:00')
# st.map(filtered_data)

def get_user_name():
    return 'John'

with st.echo():
    def get_punctuation():
        return '!!!'

    greeting = "Hi there, "
    value = get_user_name()
    punctuation = get_punctuation()

    st.write(greeting, value, punctuation)

# And now we're back to _not_ printing to the screen
foo = 'bar'
st.write('Done!')
st.text_input("Your name", key="name")

# This exists now:
st.session_state
# st.balloons()
if st.button('Show me a snow!'):
    st.snow()
if st.button('Show me balloon!'):
    st.balloons()

apple = 2

st.write(f"{apple} + banana")
st.code("""
    add(*void(),)
    interface Apple {
        int add(int a, int num)
    }
    List a ={1,2,3,4}
    a.stream().map(Integer::toString) 
    (a,b) -> a + b
    auto add(int a, int b){
        return a + b; 
    }
""")

