import PyPDF2
import re
import pandas as pd

name ="2010Apr_FE_AM_Questions.pdf"
x=PyPDF2.PdfFileReader(f"PDF/{name}");
numPages=x.numPages
count=0
temp=''
sentences=[]
start=0
st=0
while count<numPages:
    for a in x.getPage(count).extractText():
        if a == "Q":
            st=1
        if st==1 and a in "1234567890":
            start=1

        elif a == "?":
            if temp != '' or temp != " ":
                if temp[-1] == " ":
                    temp += "?"
                else:
                    temp +=" ?"
                sentences.append(temp)
            print(temp) 
            temp=''
            start=0
            st=0


        if start==1:
            if ord("a")<=ord(a)<=ord("z") or ord("A")<=ord(a)<=ord("Z") or ord("0")<=ord(a)<=ord("9") or a in " " :
                if len(temp)==0 and a in "1234567890 ":
                    pass


                else:
                    temp += a

    count +=1




cleanned =  pd.Series(sentences)

cleanned.to_csv(f"{name}C.csv",index=False)
