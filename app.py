import streamlit as st
import pickle
import pandas as pd



def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)),reverse = True,key=lambda x:x[1])[1:6]

    recommended_movies = []
    for i in movies_list:
        movie_id = i[0]
        # fetch poster via api
        
        recommended_movies.append(movies.iloc[i[0]].title)
    return recommended_movies

movies_dict = pickle.load(open('movie_dict.pkl','rb'))
movies = pd.DataFrame(movies_dict)

similarity = pickle.load(open('similarity.pkl','rb'))
st.title('Movie Recommendation System')

selected_movie_name = st.selectbox(
    " Enter A movie name",
    movies['title'].values
)

if st.button('Recommend'):
    recommendations = recommend(selected_movie_name)
    for i in recommendations:
        st.write(i)




st.markdown(
    """<hr style="margin-top: 50px;">
    <div style='text-align: center;'>
        <medium> By Om Raut</medium>
        </br>
        <a href="https://github.com/Omraut31" target="_blank">GitHub</a> |
         <a href="https://linkedin.com/in/omraut31" target="_blank">LinkedIn</a> 
    </div>""",
    unsafe_allow_html=True
)
