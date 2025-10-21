
with open("marathi_corpus.txt","r",encoding="utf-8") as f:
    text = f.read()
    tokens = text.split()
   
import regex as re
 
def keep_only_marathi(words):
    marathi_words = []
    for word in words:
        if re.search(r"[\u0900-\u097F]",word):
            marathi_words.append(word)
    return marathi_words

clean_tokens_arr = keep_only_marathi(tokens)

def clean_tokens(tokens):
    cleaned = []
    for word in tokens:
        if re.search(r'[\u0900-\u097F]',word):
            word = re.sub(r'[^ \u0900-\u097F]','',word)
            if word.strip() != "":
                cleaned.append(word)
                
    return cleaned

clean_tokens_arr = clean_tokens(clean_tokens_arr)

data = " ".join(clean_tokens_arr)
with open("Clean_corpus.txt",'w',encoding="utf-8") as f:
    f.write(data)
    
print("saved")
# print(len(clean_tokens_arr))
