# Movie-Recommender-System
A content-based movie recommendation system that recommends similar movies using movie data, cosine similarity, and the TMDB API.
# 🎬 Movie Recommendation System

A content-based Movie Recommendation System that recommends similar movies based on the selected movie. The application also fetches movie posters using the TMDB API.

## 🚀 Features

- Select a movie from the dropdown menu
- Get 5 similar movie recommendations
- Display movie posters
- Uses content-based recommendation
- Interactive web interface using Streamlit
- TMDB API integration for movie posters

## 🛠️ Technologies Used

- Python
- Streamlit
- Pandas
- Scikit-learn
- Requests
- TMDB API

## 📂 Project Structure

```text
Movie-Recommender-System/
│
├── app.py
├── train_model.py
├── requirements.txt
├── .gitignore
├── README.md
│
└── data/
    ├── tmdb_5000_movies.csv
    └── tmdb_5000_credits.csv
