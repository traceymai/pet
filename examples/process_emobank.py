import pandas as pd
df = pd.read_csv("valence_scores.txt", header=None, encoding="utf8", sep="^([^,]+),", engine="python")
df=df.loc[:,1:]
df.columns = ["Valence", "Phrase"]
min_val_col = min(df.groupby("Valence").size())
new_df = df.groupby("Valence").apply(lambda x: x.sample(min_val_col)).reset_index(drop=True)
with open("valence_scores_fin.txt", encoding="utf8", mode="r+") as f:
    f.truncate(0)
    f.close()
with open("valence_scores_fin.txt", mode="a", encoding="utf8") as f:
    for index, row in new_df.iterrows():
        f.write(str(row[0]) + ", " + row[1] + "\n")
    f.close()
print("FINISH")