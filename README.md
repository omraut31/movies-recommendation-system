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
![image](https://github.com/user-attachments/assets/db08c8f1-946e-46b1-b3cb-a285f1685c33)


### ✅ Recommendations Displayed
![image](https://github.com/user-attachments/assets/0d5fe25d-f842-4688-84b4-4695b239aa91)


---

## 📂 Project Structure

```bash
movies-recommendation-system/
│
├── app.py                  
├── movies.csv              
├── similarity.pkl          
├── screenshots/            
└── README.md               
```

---

## 🧠 How It Works

1. Load movie metadata (`movies.csv`).  
2. **Vectorize** movie tags (TF-IDF / CountVectorizer).  
3. Build a **cosine-similarity matrix** (saved as `similarity.pkl`).  
4. On selection:  
   - Locate the movie’s index.  
   - Retrieve & sort similarity scores.  
   - Display the top five matches.

---

## 💻 Quickstart

Clone & run locally:

~~~bash
git clone https://github.com/omraut31/movies-recommendation-system.git
cd movies-recommendation-system
pip install -r requirements.txt
streamlit run app.py
~~~

---

## 🛠️ Tech Stack

- **Python 3.x**  
- **Pandas** & **Scikit-learn** for data prep / ML  
- **Streamlit** for the web interface

---

## 🔗 Links

- **Repository:** <https://github.com/omraut31/movies-recommendation-system>  
- **Author:** [Om Raut](https://www.linkedin.com/in/omraut31)

---
