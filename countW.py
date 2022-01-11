import PyPDF2
import pandas as pd


name="2010Apr_FE_AM_Questions.pdf"
reader=PyPDF2.PdfFileReader(name)
a=str()
txt=str()
words=dict()
k=reader.numPages
for x in range(k):
    txt=reader.getPage(x).extractText()
    for y in txt: 
        if (y in " \n.\t({[]})><-_!@#$^%*()_+="):
            if a !="":
                if a.lower() in words:
                    words[a.lower()] +=1;
                else:
                    words[a.lower()]=1;
            a=""
           


        if (97<=ord(y)<=122) or (65<=ord(y)<=(90)) or (48<=ord(y)<=57):
            a += y




df=pd.Series(words)
words=dict()
for a in df.keys():
    if df[a] in words.keys():
        words[df[a]].append(a)
    else:
        words[df[a]]=[a]


x=pd.Series(words)

x.to_csv(name[0:-4]+"A.csv")
#df.to_csv(name[0:-4]+".csv")

