import re
import emoji
import json


filename = 'ipc_dict.json'
with open(filename, 'r', encoding='utf8') as f:

  data = json.load(f)
  for i in data['data']:
    #print(i)
    pass

def get_comment(comment):
    ipc = analyse(comment)
    return ipc


def preprocess_texts(sent):
    print("1", sent)
    sent = sent.strip()
    sent = sent.lower()
    print("2", sent)
    sent = re.sub('^@[0-9a-z_\.]+','',sent) # username 
    # print("3",sent)
    sent = re.sub(' @[0-9a-z_\.]+','',sent)
    # print("3.1",sent)
    sent = re.sub( r'\\x[0-9a-z][0-9a-z]*', ' ', sent) # remove \x09    
    # print("4",sent)
    sent = re.sub(r"http\S+", "", sent)
    # print("5",sent)
    # not removing hash, star, exclamation from mid of word
    sent = re.sub(r"[,;\(\)\\.:\-_/|](!$)*", " ", sent)
    # print("6",sent)
    sent = sent.replace('"', ' ')
    # print("7",sent)
    sent = sent.replace("'", ' ')
    # print("8",sent)
    
    emojis = emoji.emoji_list(sent)
    # print("8",emojis)

    if len(emojis)>0:
      # print(sent)
      for item in emojis:
        for emo in item['emoji']:
          sent = re.sub(emo, " " + emo + " " , sent)
        # print(sent)
    
    sent = re.sub('\n', ' ', sent)
    # print# ("9",sent)
    sent = re.sub(' +', ' ', sent)
    sent = sent.strip()
    # print("10",sent)
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
    lemmatized_tokens = custom_lemmatize(tokens)
    sent = " ".join(lemmatized_tokens)
    print(sent)
    words = sent.split()
    for i in data['data']:
        if [j for j in words if j in i['words']]:
            print(i['ipc'])
        


analyse("Meetha sala")