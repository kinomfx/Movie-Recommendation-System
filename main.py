import pandas as pd
import streamlit as st
import pickle

new_df = pickle.load(open('movies2.pkl' , 'rb'))
similarity = pickle.load(open('similarity.pkl','rb'))
new_df = pd.DataFrame(new_df)
st.title('Movie Recommender System')

def recommend(movie):
    index = new_df[new_df['title']==movie].index[0]
    distances = similarity[index]
    movies = []
    movies_list = sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])[1:6]
    for i in movies_list:

        movies.append(new_df.iloc[i[0]].title)
    return movies
option = st.selectbox(
    "what movie did you just watch",
    new_df['title'].values)

if st.button("Recommend"):
    for i in recommend(option):
        st.write(i)