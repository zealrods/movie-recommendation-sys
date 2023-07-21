import streamlit as st
import pickle
import pandas as pd
import requests

def fetch_poster(movie_id):
    response = requests.get('https://api.themoviedb.org/3/movie/{}/images?api_key=b423f60c5046e017d433070342b0f2e7'.format(movie_id))
    data = response.json()
    st.text(data)
    return "https://image.tmdb.org/t/p/original" + data['backdrops'][i]['file_path']
def fetch_poster(movie_id):
    response = requests.get('https://api.themoviedb.org/3/movie/{}/images?api_key=b423f60c5046e017d433070342b0f2e7'.format(movie_id))
    data = response.json()
    return "https://image.tmdb.org/t/p/original" + data['backdrops'][0]['file_path']

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    movies_list = sorted(list(enumerate(similarity[movie_index])), reverse=True, key=lambda x: x[1])[1:6]
    recommended_movies = []
    recommended_movies_posters = []

    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_movies_posters.append(fetch_poster(movie_id))

    return recommended_movies, recommended_movies_posters

movies_dict=pickle.load(open('movie_dict.pkl','rb'))
movies=pd.DataFrame(movies_dict)
similarity=pickle.load(open('similarity.pkl','rb'))
st.title('Movie Recommender System')

selected_movie_name=st.selectbox(
'Which movie which you would like to see?',
 movies['title'].values
)

if st.button('Recommend'):
    names, posters = recommend(selected_movie_name)
    cols = st.columns(5)

    for i, name in enumerate(names):
        with cols[i]:
            # st.text(name)
            # # st.image(posters[i])
            # st.image(posters[i], caption=name, use_column_width=True)
            # st.markdown(f"<h3 style='text-align: center;'>{name}</h3>", unsafe_allow_html=True)
            # Display the image with a fixed height and centered
            st.image(posters[i], use_column_width=True, caption=name)