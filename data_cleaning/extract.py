import pandas as pd

df = pd.read_csv("train.csv",encoding="utf-8")

summ_texts = df["SUMM"].dropna().astype(str).tolist()

corpus = " ".join(summ_texts)

with open("marathi_corpus.txt","w",encoding="utf-8") as f:
    f.write(corpus)
    
print("saved")
# print(corpus[:500])