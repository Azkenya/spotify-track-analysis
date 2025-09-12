import pandas as pd

def split_dataset(dataset):
    number_of_rows = dataset.shape[0]
    keep_rows = int(number_of_rows * 0.3)
    return dataset.iloc[:keep_rows]
def save_smaller_dataset(dataset):
    dataset.to_csv("resources/small_spotify_dataset.csv",index=False)


path= "resources/spotify_dataset.csv"
dataset = pd.read_csv(path)
dataset["Genre"] = dataset["Genre"].str.split(",")
dataset = dataset.explode("Genre")
genres = dataset["Genre"].value_counts()
with pd.option_context('display.max_rows', None, 'display.max_columns', None):  # more options can be specified also
    print(genres)
genre_families = {
    "rock": ["rock", "alternative rock", "pop rock", "hard rock", "classic rock",
             "progressive rock", "punk rock", "psychedelic rock", "garage rock", "math rock",
             "grunge", "shoegaze", "post-punk", "post-hardcore"],
    
    "pop": ["pop", "electropop", "synthpop", "indie pop", "pop punk", "dance", "dream pop",
            "chillwave", "disco", "electro", "rnb", "k-pop", "j-pop", "latin", "reggaeton",
            "worship", "chillout"],
    
    "hip hop": ["hip hop", "hip-hop", "rap", "trap", "emo rap", "cloud rap", "grime"],
    
    "metal": ["metal", "heavy metal", "death metal", "melodic death metal", "doom metal",
              "black metal", "nu metal", "power metal", "progressive metal", "metalcore",
              "thrash metal", "deathcore"],
    
    "jazz & soul": ["jazz", "soul", "funk", "blues", "swing", "gospel", "ambient"],
    
    "electronic": ["electronic", "house", "trance", "techno", "trip-hop", "dancehall",
                   "dubstep", "chillwave"],
    
    "country & folk": ["country", "folk", "alt-country", "acoustic"],
    
    "classical": ["classical", "soundtrack"],
    
    "punk": ["punk", "post-punk", "screamo", "hardcore", "emo"],
    
    "other": ["comedy", "experimental", "industrial", "psychedelic", "garage rock", "christian"]
}

def map_to_family(genre):
    for family, genres in genre_families.items():
        if genre.lower() in genres:
            return family
    return "other"
dataset["Genre_family"] = dataset["Genre"].apply(map_to_family)
family_counts = dataset["Genre_family"].value_counts()

print(family_counts)
#print(weird_emotions['song'],end="")
#print(weird_emotions['emotion'])


