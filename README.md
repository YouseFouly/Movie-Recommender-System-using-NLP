# 🎬 Movie Recommender System using NLP

Welcome to the **Movie Recommender System**, a content-based recommendation engine that suggests movies similar to a user-selected title based on Natural Language Processing (NLP) techniques. This project uses `NLTK`, `TF-IDF`, and `cosine similarity` to analyze and compare movie metadata, and is presented through an interactive **Streamlit** web app.

---

## 📌 Table of Contents

- Demo
- Features
- Tech Stack
- How It Works
- Installation
- Project Structure
- Usage
- Contact

---

## 🚀 Demo


https://github.com/user-attachments/assets/62ee11e3-e136-482e-b248-b716467da80e



---

## ✅ Features

- Interactive **Streamlit UI** with movie search and recommendation.
- Movie poster & plot summary fetched live using **OMDb API**.
- Content-based filtering using:
  - Genres
  - Keywords
  - Overview
- Text preprocessing using **NLTK**.
- Vectorization with **TF-IDF** and similarity scoring using **cosine similarity**.
- Lightweight and fast with **joblib** for serialization.
- Animated UI using **Lottie animations**.

---

## 🛠️ Tech Stack

| Component        | Technology             |
|------------------|-------------------------|
| Programming      | Python 3.x              |
| Web Framework    | Streamlit               |
| NLP Tools        | NLTK                    |
| Vectorization    | TF-IDF (Scikit-learn)   |
| Similarity Metric| Cosine Similarity       |
| Data Serialization | Joblib                |
| External API     | OMDb API (Movie details)|
| UI Enhancements  | Lottie Animations       |

---

## ⚙️ How It Works

1. **Data Preprocessing** (`preprocess.py`)
   - Loads `movies.csv` file.
   - Cleans and tokenizes movie metadata using `NLTK`.
   - Combines relevant columns: genres, keywords, and overview.
   - Vectorizes cleaned text using `TF-IDF`.
   - Computes **cosine similarity** between all movies.
   - Saves processed data (`df_cleaned.pkl`, `cosine_sim.pkl`) using `joblib`.
  
     <img width="790" height="427" alt="image" src="https://github.com/user-attachments/assets/553e35b1-a506-4457-9d63-bcc9d099e93a" />


2. **Recommendation Logic** (`recommend.py`)
   - Loads preprocessed data.
   - Finds the index of the selected movie.
   - Computes similarity scores and selects the top N similar movies.
   - Returns a cleaned and indexed recommendation DataFrame.

3. **Web Interface** (`main.py`)
   - Built using **Streamlit**.
   - Lets users select a movie from a dropdown list.
   - Displays top similar movie titles with posters and plot summaries.
   - Uses **OMDb API** to fetch real-time poster and plot data.
   - Adds animated visuals via **Lottie** for improved UX.

     <img width="1910" height="961" alt="image" src="https://github.com/user-attachments/assets/4475ff71-5daa-4464-8f8f-2cc440c6660d" />


---

## 🧪 Installation

1. **Clone the repository**
   git clone https://github.com/yourusername/movie-recommender-nlp.git
   cd movie-recommender-nlp

2. **Create a virtual environment**
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate

3. **Install dependencies**
   pip install -r requirements.txt

4. **Download NLTK resources (only once)**
   import nltk
   nltk.download('punkt')
   nltk.download('stopwords')
   
5. **Run the app**
  streamlit run main.py


## 📁 Project Structure

├── main.py               # Streamlit front-end
 
├── recommend.py          # Recommendation logic

├── preprocess.py         # Data cleaning, NLP, and vectorization

├── config.json           # API key config for OMDb

├── movies.csv            # Dataset file

├── requirements.txt      # Required libraries

├── df_cleaned.pkl        # Preprocessed movie dataframe

├── cosine_sim.pkl        # Cosine similarity matrix

├── tfidf_matrix.pkl      # TF-IDF vectors


## ▶️ Usage

- Launch the Streamlit app using the command above.
- Choose a movie title from the dropdown menu.
- Click on "🚀 Recommend Similar Movies".
- View top similar movies along with their poster and plot.

## 📬 Contact

Made by Yousef El-Fouly
💼 LinkedIn: www.linkedin.com/in/youssef-el-fouly-667600205

📧 Email: yousefelfouly2020@gmail.com 











