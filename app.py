import streamlit as st 
import pickle
import pandas as pd
import requests

def fetch_poster(movie_title):
    try:
        url = f"https://api.themoviedb.org/3/search/movie?api_key=d84f77d370aefc3683bf3937527bf843&query={movie_title}"
        data = requests.get(url).json()

        if len(data["results"]) > 0 and data["results"][0]["poster_path"]:
            poster_path = data["results"][0]["poster_path"]
            return "https://image.tmdb.org/t/p/w500" + poster_path
        else:
            return "https://via.placeholder.com/300x450?text=No+Poster"

    except:
        return "https://via.placeholder.com/300x450?text=Error"


# Recommendation function
def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]

    movies_list = sorted(list(enumerate(distances)),
                         reverse=True,
                         key=lambda x: x[1])[1:6]

    recommended_movies = []
    recommended_posters = []

    for i in movies_list:
        movie_index = i[0]
        movie_title = movies.iloc[movie_index].title  # ✅ FIX

        recommended_movies.append(movie_title)  # ✅ FIX
        recommended_posters.append(fetch_poster(movie_title))  # ✅ FIX

    return recommended_movies, recommended_posters


# UI Title
st.title("🎬 Movie Recommendation System")

# Load data
movies_dict = pickle.load(open('movie_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)

similarity = pickle.load(open('similarity.pkl', 'rb'))

# Dropdown menu
selected_movie_name = st.selectbox(
    "Select a movie",
    movies['title'].values
)

# Button
if st.button("Recommend"):

    names, posters = recommend(selected_movie_name)

    col1, col2, col3, col4, col5 = st.columns(5)

    cols = [col1, col2, col3, col4, col5]

    for i in range(5):
        with cols[i]:
            st.caption(names[i])
            st.image(posters[i])