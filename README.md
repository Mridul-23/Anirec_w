# ANIREC Web

> A Django server-side rendered anime discovery and personalized recommendation platform powered by content-based similarity and a UCB multi-armed bandit recommender.

ANIREC Web is the web version of the original ANIREC anime recommender system. It combines an anime catalog, search and discovery features, user accounts, favorites, anime similarity recommendations, and an interactive personalized recommendation workflow.

The application is built with **Django SSR, HTML templates, CSS, and JavaScript**, while the recommendation engine uses a precomputed similarity matrix and an **Upper Confidence Bound (UCB)** multi-armed bandit algorithm.

---

## ✨ Features

* 🔎 **Anime Discovery** — Browse, search, filter, and explore anime with detailed metadata and similar-anime recommendations.
* 🤖 **Personalized Recommendations** — Rate three anime and receive adaptive recommendations using a UCB multi-armed bandit.
* 👤 **User Accounts** — Registration, login/logout, dashboard, and saved/favorite anime.
* 🎨 **Web Interface** — Django SSR application with custom HTML, CSS, and JavaScript.

---

## 🧠 Recommendation System

ANIREC combines **content-based similarity** with a **UCB multi-armed bandit**.

* **Content-Based Similarity:** Uses the precomputed `similarity_matrix.pkl` to find similar anime.
* **UCB Bandit:** Maintains three recommendation arms and uses user ratings to balance **exploration** and **exploitation**.
* Each round selects the highest-scoring arm, generates three recommendations, and uses the user's ratings as feedback for future rounds.

```text
User Ratings → UCB Arm Selection → Similarity Search
      ↑                                  │
      └────── Rate Recommendations ──────┘
```

---

## 🚀 Installation

### 1. Clone the repository

```bash
git clone https://github.com/Mridul-23/Anirec_w.git
cd Anirec_w
```

### 2. Create a virtual environment

Windows:

```bash
python -m venv venv
venv\Scripts\activate
```

macOS/Linux:

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Apply migrations

```bash
python manage.py migrate
```

### 5. Start the development server

```bash
python manage.py runserver
```

Open:

```text
http://127.0.0.1:8000/
```

---

## 📦 Required Data / Model Files

The web application relies on a precomputed similarity matrix:

```text
similarity_matrix.pkl
```

This file is loaded by the recommendation code to retrieve anime similarity values.

---

## ⚙️ Data Import

The `anime` application includes custom Django management commands for importing anime data and images:

```text
anime/management/commands/
├── import_anime.py
└── import_images.py
```

If the repository includes the source data required by these commands, the commands can be used to populate the Django database and associated anime images.

---

## 🖥️ Screenshots

### Landing Page

The landing page introduces ANIREC and provides entry points for anime discovery and the recommendation experience.

![ANIREC Landing Page](docs/screenshots/landing.png)

### Anime Search

Search anime by title and browse results using sorting/filtering controls.

![Anime Search](docs/screenshots/search.png)

### Anime Details

Anime detail pages present metadata, synopsis, poster artwork, and similar anime.

![Anime Details](docs/screenshots/anime-details.png)

### User Dashboard

Authenticated users can view their profile information and saved anime.

![User Dashboard](docs/screenshots/dashboard.png)

### Personalized Recommender

The recommendation workflow collects initial preferences and uses user ratings as feedback for subsequent recommendations.

![ANIREC Recommender](docs/screenshots/recommender.png)

> **Screenshot setup:** create `docs/screenshots/` in the repository and place the corresponding screenshots there using the filenames shown above.

---

## 📄 License

This project is licensed under the **MIT License**.

See the [LICENSE](LICENSE) file for details.

---

## 👨‍💻 Author

**Mridul Narula**

Original ANIREC project:

`https://github.com/Mridul-23/Anirec`
