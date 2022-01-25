import nltk
import random
import numpy
import pandas as pd
data = pd.read_table("questions/S08_question_answer_pairs.txt")
Tagged = []
for a in data.Question:
    if a is not numpy.nan:
        temp  = nltk.tokenize.word_tokenize(a)
        temp2 = []
        temp3 = nltk.pos_tag(temp)
        print(temp3)
        for b in temp3:
            temp1 = 0
            for c in b[1]:
                temp1 += ord(c)
            temp2.append(temp1)    
        print(temp2)
        Tagged.append(temp2)

print(data.shape)
random.shuffle(Tagged)

