import numpy as np
import pickle


def UCB(session):
    if 'user_history_dict' not in session:
        session['user_history_dict'] = {}
    user_history_dict = session['user_history_dict']
    round_no = session['round_no']
    ucb_values = {}
    for i in range(3):
        t = user_history_dict[f'arm{i+1}']['t']
        ratings = user_history_dict[f'arm{i+1}']['rating']
        average_rating = sum(ratings) / len(ratings)
        exploration_term = np.sqrt(2*(np.log(round_no))/t)
        ucb_values[i+1] = average_rating + exploration_term
    
    arm = max(ucb_values, key=ucb_values.get)
    recommendations = recommend(session, arm)
    round_no += 1
    user_history_dict[f'arm{arm}']['t'] += 1
    user_history_dict['already_recommended'].extend(recommendations)


    session['user_history_dict'] = user_history_dict
    session['round_no'] = round_no
    session['previous_arm'] = arm

    return recommendations



def recommend(session, arm):
    with open(r'similarity_matrix.pkl', 'rb') as f:
        similarity_matrix = pickle.load(f)
    user_history_dict = session['user_history_dict']
    similar_anime = []
    anime_list = []

    arm_shows = user_history_dict[f'arm{arm}']['anime']
    same_shows = len(arm_shows)

    for shown in arm_shows:
        distances = similarity_matrix[shown]
        similar_anime.extend(sorted(list(enumerate(distances)), reverse=True, key = lambda x:x[1])[same_shows:100])
    
    anime_list.extend([i[0] for i in similar_anime])
    recommendations = [i for i in anime_list if i not in user_history_dict['already_recommended']][:3]

    user_history_dict[f'arm{arm}']['anime'].extend(recommendations)

    return recommendations
