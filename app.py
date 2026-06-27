import streamlit as st
import pickle

movies_list = pickle.load(open('model/movies.pkl', 'rb'))
movies_list = movies_list['title'].values

st.title("Movie Recommendation System")

option = st.selectbox(
    "How would you like to be contacted?",
    movies_list,
)

st.write("You selected:", option)

import streamlit as st

if st.button("Recommend"):
    st.write(f"Recommending {option}...")
