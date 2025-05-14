import pickle

import streamlit as st
import pandas as pd

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movie_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    for i in movie_list:
        movie_id = i[0]
        recommended_movies.append(movies.iloc[i[0]].title)
    return recommended_movies

movies_list  = pickle.load(open('movies.pkl','rb'))
movies = pd.DataFrame(movies_list)

similarity = pickle.load(open('similarity.pkl','rb'))

#title
st.title("Movie Recommender Agent")

#selection box
movie_name = st.selectbox(
'Enter Movie Name',
movies['title'].values)

#recommend button
if st.button('Recommend'):
    recommendations = recommend(movie_name)
    st.title("Top five(5) movies are Recommended")
    for i in recommendations:

        st.write(i)