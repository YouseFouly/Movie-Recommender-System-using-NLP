import streamlit as st
import requests
import json
from streamlit_lottie import st_lottie
from recommend import df, recommend_movies
from omdb_utils import get_movie_details

# -------------------- Page Configuration --------------------
st.set_page_config(
    page_title="Movie Recommender",
    page_icon="🎬",
    layout="wide"
)

# -------------------- Load Lottie Animation --------------------
def load_lottie_url(url: str):
    response = requests.get(url)
    try:
        return response.json()
    except requests.exceptions.JSONDecodeError:
        print("❌ Failed to parse JSON from URL.")
        print("Response content:", response.text[:200])
        return None

lottie_json = load_lottie_url("https://lottie.host/6a3c20ab-7269-4d62-a63d-978f8561129b/0LG3Uiq3SJ.json")
lottie_json2 = load_lottie_url("https://lottie.host/494b0d88-2f40-47a8-9893-b870cb38deab/7dxstn7pDf.json")

# -------------------- Layout: Columns --------------------
left_col, right_col = st.columns([2, 1])

# -------- Left Column: App Functionality --------
with left_col:
    st.title("🎬 Movie Recommender")

    movie_list = sorted(df['title'].dropna().unique())
    selected_movie = st.selectbox("🎞️ Select a movie:", movie_list)


    if st.button("🚀 Recommend Similar Movies"):
        with st.spinner("Finding similar movies..."):
            recommendations = recommend_movies(selected_movie)

            if recommendations is None or recommendations.empty:
                st.warning("Sorry, no recommendations found.")
            else:
                st.success("🎯 Top similar movies:")
                for _, row in recommendations.iterrows():
                    movie_title = row['title']
                    plot, poster = get_movie_details(movie_title, json.load(open("config.json"))["OMDB_API_KEY"])

                    with st.container():
                        col1, col2 = st.columns([1, 3])
                        with col1:
                            if poster != "N/A":
                                st.image(poster, width=100)
                            else:
                                st.write("❌ No Poster Found")
                        with col2:
                            st.markdown(f"### {movie_title}")
                            st.markdown(f"*{plot}*" if plot != "N/A" else "_Plot not available_")
    if lottie_json2:
        st_lottie(lottie_json2, speed=1, loop=True, height=250)
    else:
       st.error("❌ Failed to load Lottie animation.")

# -------- Right Column: Lottie Animation --------
with right_col:
    if lottie_json:
        st_lottie(lottie_json, speed=1, loop=True, height=300)
    else:
        st.error("❌ Failed to load Lottie animation.")
