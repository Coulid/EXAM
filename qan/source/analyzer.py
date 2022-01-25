#Attempt to generate the tagged code

import numpy
import pandas
from PyPDF2 import PdfFileReader
import nltk
import string
 
def analyze(name):
    """A function to Read and tokenize and tag the PDF"""
    #use PdfFileReader to read the question PDF
    name =str(name)
    data= PdfFileReader(f"PDF/{name}")
    tagged=[]
    # use for loop to read page by page
    for a in range(data.getNumPages()):
        # extract text with data.getPage(a).extractText() function and  store as temp 
        temp=data.getPage(a).extractText();
        
        #use nltk lib to tokenize the extracted text and store as temp
        temp=nltk.tokenize.word_tokenize(temp)

        #use pos_tag function to tag the list of tokenized string
        temp=nltk.pos_tag(temp)

        #use for loop to drop the unnessary things like punctuation
        for b in temp:
            
            # not drop the "." and "?" because it can be useful in later states
            if b[1] in string.punctuation and b[1] not in ".?" :
                pass
            else:
                tagged.append(b);

    # return the tagged list of string
    return tagged;
