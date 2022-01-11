#this is the code for pull the questions
import pandas as pd
import PyPDF2                                #import pypdf2 module
name="QUESTIONS.txt"                        #name of the pdf in PDF folder
x=open(f"PDF/{name}","r").read()
tmp="";
questions=[]
for a in x:
    if a in '.1234567890\n':
        if tmp != "":
            questions.append(tmp.lower())
        tmp=""
    
    else:
        tmp +=a




x=pd.Series(questions)
n=x.sort_values()
n.to_csv("q.csv",index=False)








"""
x=PyPDF2.PdfFileReader(f"PDF/{name}");
k=x.numPages

for a in range(k):
    x.getPage(a).extractText()
    #for b in x.getPage(a).extractText()
"""
