from anime.models import GeneralData


def initialize_user_history(session, data):
    if 'user_history_dict' not in session:
        show1 = data.get('show1')
        show2 = data.get('show2')
        show3 = data.get('show3')
        show1_rating = int(data.get('show1_rating'))
        show2_rating = int(data.get('show2_rating'))
        show3_rating = int(data.get('show3_rating'))

        # Ensure that these shows exist
        show1_obj = GeneralData.objects.filter(name_english=show1).first()
        show2_obj = GeneralData.objects.filter(name_english=show2).first()
        show3_obj = GeneralData.objects.filter(name_english=show3).first()
        
        show1 = show1_obj.unique_id
        show2 = show2_obj.unique_id
        show3 = show3_obj.unique_id

        session['round_no'] = 1
        session['previos_arm'] = 0
        session['user_history_dict'] = {
            'already_recommended': [],
            'arm1': {'anime': [], 'rating': [], 't': 1},
            'arm2': {'anime': [], 'rating': [], 't': 1},
            'arm3': {'anime': [], 'rating': [], 't': 1}
        }
        user_history_dict = session['user_history_dict']
        user_history_dict['arm1']['anime'].append(show1)
        user_history_dict['arm2']['anime'].append(show2)
        user_history_dict['arm3']['anime'].append(show3)
        user_history_dict['arm1']['rating'].append(show1_rating)
        user_history_dict['arm2']['rating'].append(show2_rating)
        user_history_dict['arm3']['rating'].append(show3_rating)
        user_history_dict['already_recommended'].extend([show1, show2, show3])

        session['user_history_dict'] = user_history_dict

def update_user_history(session, show1_rating, show2_rating, show3_rating):
    user_history_dict = session['user_history_dict']
    arm = session['previous_arm']
    user_history_dict[f'arm{arm}']['rating'].extend([show1_rating, show2_rating, show3_rating])

    session['user_history_dict'] = user_history_dict