import pandas as pd
path= "../resources/spotify_dataset.csv"
dataset = pd.read_csv(path)
genres={}
for line in dataset['Genre']:
    if line in genres:
        genres[line]+=1
    else:
        genres[line]=1
print(genres)

#print(weird_emotions['song'],end="")
#print(weird_emotions['emotion'])


