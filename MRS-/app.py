import streamlit as st
import pickle

movies_list=pickle.load(open('movies.pkl','rb'))   #movies list ma hamro new_df basxa
movies_list=movies_list['title'].values

st.title('Movie Recommender System -MRS')

selected_movie_name = st.selectbox(
'We Recommend',
movies_list)


if st.button('Recommend'):
    st.write('Dhantanana')
