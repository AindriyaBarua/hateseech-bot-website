import re
import emoji
import json


filename = 'ipc_dict.json'
with open(filename, 'r', encoding='utf8') as f:

  data = json.load(f)
  for i in data['data']:
    pass

def get_comment(comment):
    print(comment)
    ipc = analyse(comment)
    return ipc


def preprocess_texts(sent):
    sent = sent.strip()
    sent = sent.lower()
    sent = re.sub('^@[0-9a-z_\.]+','',sent) # username 
    sent = re.sub(' @[0-9a-z_\.]+','',sent)
    sent = re.sub( r'\\x[0-9a-z][0-9a-z]*', ' ', sent) # remove \x09    
    sent = re.sub(r"http\S+", "", sent)
    # not removing hash, star, exclamation from mid of word
    sent = re.sub(r"[,;\(\)\\.:\-_/|](!$)*", " ", sent)
    sent = sent.replace('"', ' ')
    sent = sent.replace("'", ' ')
    
    emojis = emoji.emoji_list(sent)

    if len(emojis)>0:
      for item in emojis:
        for emo in item['emoji']:
          sent = re.sub(emo, " " + emo + " " , sent)
    
    sent = re.sub('\n', ' ', sent)
    sent = re.sub(' +', ' ', sent)
    sent = sent.strip()
    return sent


def custom_lemmatize(tokens):
    lemmatized_tokens =  []
    for token in tokens:
      
      new = token[0]
      count = 1
      for ch in token[1:]:
        
        if ch == new[len(new)-1]:
          count = count + 1
          if count <= 2:
             new = new + ch
        else:
          count = 1
          new = new + ch
      lemmatized_tokens.append(new)
    return lemmatized_tokens

def tokenize(sentence):
    tokens = sentence.split()
    return tokens


def analyse(comment):
    
    sent = preprocess_texts(comment)
    tokens = tokenize(sent)
    print(sent)
    lemmatized_tokens = custom_lemmatize(tokens)
    sent = " ".join(lemmatized_tokens)
    response = []
    words = sent.split()
    hate_type_list = []
    ipc_list = []
    for i in data['data']:
        if [j for j in words if j in i['words']]:
            print(i['hate_type'], i['ipc'])
            hate_type_list.append(i['hate_type'])
            ipc_list= ipc_list + i['ipc']
    hate_type = ", ".join(list(set(hate_type_list)))
    return {"hate_type":hate_type, "ipc":list(set(ipc_list))}


analyse("Saale randi aukath")