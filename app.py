import streamlit as st
import pickle


movies=pickle.load(open("movies.pkl",'rb'))

similarity=pickle.load(open("similarity.pkl",'rb'))
movie_list=movies['title'].values
def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movie_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    l=[]
  #  poster=[]
    for i in movie_list:
        l.append(movies.iloc[i[0]].title)
        #poster.append(fetch_poster(movie_id))
    return l



st.title("MOVIE RECOMMENDER SYSTEM")
movie = st.selectbox('Select a movie of your interest',(movie_list))
if st.button("Recommend"):
    recommendations=recommend(movie)
    for i in recommendations:
        st.write(i)