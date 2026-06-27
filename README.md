<div align="center">
   ## 🎬 Machine Learning Movie Recommendation Engine
</div>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.8+-blue.svg?logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/Streamlit-Web_App-FF4B4B.svg?logo=streamlit&logoColor=white" alt="Streamlit">
  <img src="https://img.shields.io/badge/Scikit--Learn-Machine_Learning-orange.svg?logo=scikit-learn&logoColor=white" alt="Scikit-Learn">
  <img src="https://img.shields.io/badge/Pandas-Data_Processing-150458.svg?logo=pandas&logoColor=white" alt="Pandas">
  <img src="https://img.shields.io/badge/NLTK-NLP-154f5b.svg?logo=python&logoColor=white" alt="NLTK">
  <img src="https://img.shields.io/badge/TMDB_API-Data_Source-01b4e4.svg?logo=themoviedb&logoColor=white" alt="TMDB API">
</p>

## 📌 What is this Project?
In an era of information overload, finding the right content can be overwhelming for users. Recommendation systems are information filtering algorithms designed to predict user preferences and surface highly relevant items. 

This project is an end-to-end Machine Learning pipeline and interactive web dashboard designed to solve the content discovery problem. It utilizes a **Content-Based Filtering** approach, analyzing unstructured metadata (genres, keywords, cast, and crew) to evaluate mathematical similarities between movies and generate accurate recommendations.

---

## 🎥 Live Demo & Visual Proof

### System in Action (Screen Recording)
Watch the full recommendation engine in action, including live API fetching of movie posters and instantaneous similarity calculations.

<video src="images_and_videos/movie_recommendation_system_video.mp4" width="100%" controls></video>

---

## 📸 Proof of Concept: Recommendations
Below are actual outputs from the engine when querying highly popular cinematic franchises. The model successfully clusters mathematically similar movies based on semantic metadata.

### 🦸‍♂️ Avengers Movie Query

<img src="images_and_videos/avengers_movie_recommendations.png" alt="Avengers Recommendations" width="800"/>

### 🦇 Batman Movie Query

<img src="images_and_videos/batman_movie_recommendation.png" alt="Batman Recommendations" width="800"/>

### 🕷️ Spiderman Movie Query

<img src="images_and_videos/spiderman_movie_recommendation.png" alt="Spiderman Recommendations" width="800"/>

---

## 🛠️ Tech Stack & Tools Used
* **Programming Language:** Python
* **Web Framework & UI:** Streamlit
* **External API & Image Fetching:** TMDB API (The Movie Database)
* **Data Manipulation & Analysis:** Pandas, NumPy
* **Natural Language Processing (NLP):** NLTK (Natural Language Toolkit)
* **Machine Learning Engine:** Scikit-Learn (`CountVectorizer`, `cosine_similarity`)
* **Serialization:** Pickle (for model deployment)

### Applying Vector Space Modeling (Bag of Words)
To allow the machine learning model to understand text, the textual data (tags) was converted into numerical vectors. Using a maximum of 5,000 frequent features, the algorithm maps out every movie into a high-dimensional vector space, establishing mathematical coordinates for each film based on its characteristics.

---

## 🧠 Machine Learning Architecture & Engineering
To accurately capture the nuanced similarities between thousands of films, I deployed a strict data engineering and NLP pipeline:

1. **Feature Engineering (Tag Aggregation):** Standard datasets contain fragmented columns. The data was engineered by merging `overview`, `genres`, `keywords`, `cast` (top 3 actors), and `crew` (Director) into a single, comprehensive `tags` corpus.
2. **NLP Stemming:** Text data varies wildly in suffix forms (e.g., "action", "actions"). Using the PorterStemmer algorithm, all words were reduced to their root semantic forms to ensure computational efficiency and prevent redundant feature extraction.
3. **Cosine Similarity Matrix:** Rather than measuring the Euclidean distance between movie vectors (which is susceptible to document length variations), the engine calculates the cosine of the angle between vectors. This strictly measures the directional similarity, outputting a strict `0` to `1` similarity score.

---

## 📊 Evaluation Criteria & Model Judgment
In content-based recommendation engines, success is measured by the semantic relevance of the outputted items relative to the input item. The model was evaluated based on the following:
* **Cosine Similarity Score Distribution:** Ensuring the model can confidently distinguish between a highly relevant match (score > 0.6) and a poor match.
* **Contextual Alignment:** How accurately the model maintains the genre, director style, and thematic elements of the source movie.

### Comparative Analysis: The "Content Bubble" Reality Check
Rather than claiming this engine perfectly understands human emotion, this project documents the mathematical reality of Content-Based Filtering. As visualized in the dashboard, the model successfully learns the metadata profile and returns highly accurate, context-aware suggestions. However, it exhibits the classic **"Content Bubble"** limitation—it strictly recommends items highly similar to what the user already knows, lacking the serendipitous discovery provided by Collaborative Filtering (which analyzes diverse user behavior).

---

## 🚀 Installation & Usage
Want to run this recommendation engine on your local machine?

### 1. Clone the repository & enter the directory:
```bash
git clone [https://github.com/your-username/movie-recommendation-system.git](https://github.com/your-username/movie-recommendation-system.git)
cd movie-recommendation-system
