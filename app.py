import streamlit as st
import pickle
import pandas as pd
import requests


base="dark"
primaryColor="#fdf111"
secondaryBackgroundColor="#f5dd05"
font="serif"


st.header('Movie Recommendation Syatem')
movies = pickle.load(open('movies.pkl','rb'))
movie_list = movies['title'].values
similarity = pickle.load(open('similarity.pkl','rb'))
print(movie_list)

selected_movies = st.selectbox('Select the movie:-',(movie_list))

def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=e23145b38806e5c827304a547ecf3395".format(movie_id)
    data = requests.get(url)
    data = data.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path


def recommend(selected_movies):
     recommend_posters=[]
     recommend_movies =[]
     index = movies[movies['title'] == selected_movies].index[0]
     distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])

     for i in distances[1:6] :
          movies_id = movies.iloc[i[0]].movie_id
          recommend_movies.append(movies.iloc[i[0]].title)
          recommend_posters.append(fetch_poster(movies_id))

     return recommend_movies,recommend_posters

if st.button('Recommendation'):
    recommend_movies,recommend_posters = recommend(selected_movies)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(recommend_movies[0])
        st.image(recommend_posters[0])
    with col2:
         st.text(recommend_movies[1])
         st.image(recommend_posters[1])
    with col3:
         st.text(recommend_movies[2])
         st.image(recommend_posters[2])
    with col4:
         st.text(recommend_movies[3])
         st.image(recommend_posters[3])
    with col5:
         st.text(recommend_movies[4])
         st.image(recommend_posters[4])