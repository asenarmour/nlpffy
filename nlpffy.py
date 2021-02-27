import streamlit as st
import os
import nltk
# nltk.download('punkt')
#nlp pakages
from textblob import TextBlob
import spacy


def text_analyzer(my_text):
    nlp=spacy.load("en")
    docx=nlp(my_text)
    all_data=[('"token":{},\n "Lemma":{}'.format(token.text,token.lemma_)) for token in docx ]
    return all_data

def entity_analyser(my_text):
    nlp=spacy.load("en")
    docx=nlp(my_text)
    tokens=[token.text for token in docx]
    entities = [(entity.text,entity.label_)for entity in docx.ents]
    allData = ['"Token":{},\n"Entities":{}'.format(tokens,entities)]
    return allData
def main():
    """ NLP BASED APP"""
    #title
    st.title("NLP WITH STREAMLIT")
    st.subheader("Natural Language processing ")
    st.markdown("""
    #### Description
    + This is Natural Language Processing (NLP) Based App Useful for 
    basis nlp tasks like Tokenization, Sentiment Analysis and Summarization
    """)

    #Tokenization
    if st.checkbox("Show Tokens and Lemma"):
        st.subheader("Tokenize your text")
        message=st.text_area("Enter Text","Type Here....")
        if st.button("Analyze"):
            nlp_result=text_analyzer(message)
            st.json(nlp_result)
    
    if st.checkbox("Show Named Entities"):
        st.subheader("Analyse your Text")
        message=st.text_area("enter_text","type Here..")
        if st.button("Extract"):
            entity_result=entity_analyser(message)
            st.json(entity_result)
    if st.checkbox("Show Sentiment Analysis"):
        st.subheader("Analyse Your Text")
        message=st.text_area("Enter_Text","Type Here..")
        if st.button("Analyse"):
            blob=TextBlob(message)
            result_sentiment=blob.sentiment
            st.success(result_sentiment)

if __name__ == "__main__":
    main()
    