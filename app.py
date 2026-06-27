import streamlit as st
import pickle
import requests

movies_df = pickle.load(open('model/movies.pkl', 'rb'))
movies_list = movies_df['title'].values

similarity = pickle.load(open('model/similarity.pkl', 'rb'))

API_KEY='8e6bd9d99d5ba1d6e98eead9e92602ff'

def features_fetch(movie_id):
    response = requests.get(f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={API_KEY}")
    data = response.json()
    return 'https://image.tmdb.org/t/p/w500/' + data['poster_path']

def reccomend(movie):
    movie_index = movies_df[movies_df['title'] == movie].index[0]
    distances = similarity[movie_index]
    movie_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x:x[1])[1:6]

    recommended_movies=[]
    recommended_poster = []

    for i in movie_list:
        movie_id = movies_df.iloc[i[0]].id
        recommended_movies.append(movies_df.iloc[i[0]].title)
        recommended_poster.append(features_fetch(movie_id))

    return recommended_movies, recommended_poster

st.title("Movie Recommendation System")

option = st.selectbox(
    "How would you like to be contacted?",
    movies_list,
)

st.subheader(f"You selected: {option}")

import streamlit as st

if st.button("Recommend"):
    st.subheader(f"Recommending {option}...")
    names, posters = reccomend(option)
    
    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        st.text(names[0])
        st.image(posters[0])
    
    with col2:
        st.text(names[1])
        st.image(posters[1])

    with col3:
        st.text(names[2])
        st.image(posters[2])

    with col4:
        st.text(names[3])
        st.image(posters[3])

    with col5:
        st.text(names[4])
        st.image(posters[4])