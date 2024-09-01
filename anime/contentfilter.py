import re
import pickle
import pandas as pd

anidf = pd.read_csv(r"C:\Users\HP\Desktop\Projects\Anirec (Cli)\Anirec\data\preprocessed_ani_data.csv")
with open(r'similarity_matrix.pkl', 'rb') as f:
    similarity_matrix = pickle.load(f)


def recommend(anime, top=3):
    """
    Recommend top N similar anime titles based on content similarity.

    :param anime: The name of the anime to base recommendations on.
    :param top: The number of top recommendations to return.
    :return: A list of recommended anime titles.
    """
    if anime not in anidf['name_english'].values:
        return f"Anime '{anime}' not found in the dataset."
    
    anime_index = anidf[anidf['name_english'] == anime].index[0]
    
    distances = similarity_matrix[anime_index]
    
    anime_list = [(i, dist) for i, dist in enumerate(distances) if anidf.iloc[i].name_english != anime]
    
    anime_list = sorted(anime_list, key=lambda x: x[1], reverse=True)[:top+10]
    
    recommended_animes = [anidf.iloc[i[0]].name_english for i in anime_list]

    recommended_animes = list(set(recommended_animes))
    
    pattern = r'\b' + re.escape(anime) + r'\b'
    recommended_animes = [title for title in recommended_animes if not re.search(pattern, title, re.IGNORECASE)]
    
    return recommended_animes[:top] if len(recommended_animes) >= top else recommended_animes

if __name__=="__main__":
    def test_recommend(anime):
        similar_animes = recommend(anime)
        print(f"Top {len(similar_animes)} anime similar to '{anime}':\n")
        counter = 1
        for anime in similar_animes:
            print(f"{counter}. {anime}")
            counter += 1

    test_recommend("One Piece")