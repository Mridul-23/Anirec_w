import numpy as np
import pickle
import pandas as pd

anidf = pd.read_csv(r"C:\Users\HP\Desktop\Projects\Anirec (Cli)\Anirec\data\preprocessed_ani_data.csv")
with open(r'similarity_matrix.pkl', 'rb') as f:
    similarity_matrix = pickle.load(f)

round_no = 0
user_history_dict = {
    'already_recommended': [],
    'arm1': {'anime': [], 'rating': [], 't': 1},
    'arm2': {'anime': [], 'rating': [], 't': 1},
    'arm3': {'anime': [], 'rating': [], 't': 1}
}

def user_history(temp_dict, arm):
    """Update user history with anime and ratings."""
    global user_history_dict, round_no
    round_no += 1
    if 'anime' in temp_dict:
        user_history_dict['already_recommended'].extend(temp_dict['anime'])
        user_history_dict[f'arm{arm}']['anime'].extend(temp_dict['anime'])
        user_history_dict[f'arm{arm}']['rating'].extend(temp_dict['rating'])
    else:
        for i in range(3):
            user_history_dict['already_recommended'].extend(temp_dict[f'arm{i+1}']['anime'])
            user_history_dict[f'arm{i+1}']['anime'].extend(temp_dict[f'arm{i+1}']['anime'])
            user_history_dict[f'arm{i+1}']['rating'].extend(temp_dict[f'arm{i+1}']['rating'])

def UCB():
    """Use UCB algorithm to choose the best arm."""
    global user_history_dict, round_no
    ucb_values = []
    for i in range(3):
        t = user_history_dict[f'arm{i+1}']['t']
        ratings = user_history_dict[f'arm{i+1}']['rating']
        avg_rating = sum(ratings) / len(ratings) if ratings else 0
        exploration_term = np.sqrt(2 * np.log(round_no) / t)
        ucb_values.append((i+1, avg_rating + exploration_term))
    return max(ucb_values, key=lambda x: x[1])[0]

def recommend(arm):
    """Recommend anime based on user history and similarity matrix."""
    global user_history_dict
    similar_anime = []
    anime_list = []

    for shown in user_history_dict[f'arm{arm}']['anime']:
        distances = similarity_matrix[shown]
        anime_list.extend(sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:10])

    similar_anime.extend(sorted(anime_list, reverse=True, key=lambda x:x[1]))
    anime_list = [i[0] for i in similar_anime]
    recommendations = [i for i in anime_list if i not in user_history_dict['already_recommended']][:3]
    
    return recommendations
