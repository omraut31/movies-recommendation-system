# 🎬 Movie Recommendation System

This is a **content-based movie recommendation system** built using **Python** and **Streamlit**, which suggests similar movies based on your selection. It uses pre-processed movie metadata and machine learning techniques to recommend top 5 similar movies.

---

## 🚀 Features

- Simple and interactive **Streamlit UI**
- Dropdown to select any movie
- Recommends 5 similar movies
- Clean layout with dark theme
- GitHub and LinkedIn profile integration

---

## 📸 Screenshots

### 🔍 Homepage
![Homepage](https://github.com/omraut31/movies-recommendation-system/blob/main/screenshots/Screenshot%202025-06-26%20113039.png)

### ✅ Recommendations Displayed
![Recommendations](https://github.com/omraut31/movies-recommendation-system/blob/main/screenshots/Screenshot%202025-06-26%20113109.png)

---

## 📂 Project Structure

```bash
movies-recommendation-system/
│
├── app.py                  # Streamlit app code
├── movies.csv              # Dataset with metadata
├── similarity.pkl          # Precomputed similarity matrix
├── screenshots/            # Screenshots for README
└── README.md               # You're here!

🧠 How It Works
1. Loads movie metadata from a CSV file

2. Computes a cosine similarity matrix using TF-IDF or CountVectorizer on movie tags

3.When a movie is selected, the system:

     a) Finds its index

     b) Fetches similarity scores

     c) Sorts and returns the top 5 similar movies
💻 Installation & Usage
1) Clone the repository:

bash
Copy
Edit
git clone https://github.com/omraut31/movies-recommendation-system.git
cd movies-recommendation-system
2) Install the required packages:

bash
Copy
Edit
pip install -r requirements.txt
3) Run the app:

bash
Copy
Edit
streamlit run app.py

🔗 Links
📂 https://github.com/omraut31/movies-recommendation-system

👨‍💻 Developer: Om Raut

🛠️ Tech Stack
Python

Pandas

Scikit-learn

Streamlit
