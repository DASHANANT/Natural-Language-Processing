# Libraries used for Summarization
---------------------------------------------------------------------------
- *nltk*
- *sumy* pypi package

Two different approaches are used for Text Summarization
---------------------------------
- Extractive Summarization 
- Abstractive Summarization

Extractive Summarization
----------------------------
In Extractive Summarization, we are identifying important phrases or sentences from the original text and extract only these phrases from the text. 
These extracted sentences would be the summary.

Abstractive Summarization
---------------------------
In the Abstractive Summarization approach, we work on generating new sentences from the original text. 
The abstractive method is in contrast to the approach that was described above. The sentences generated through this approach might not even be present in the original text.
We are going to focus on using extractive methods.
This method functions by identifying important sentences or excerpts from the text and reproducing them as part of the summary. 
In this approach, no new text is generated, only the existing text is used in the summarization process. 

Steps for Implementation
-----------------------------
There are two NLTK libraries that are necessary for building an efficient text summarizer.
Step 1: The first step is to import the required libraries. 
----------------------------------------------------------------
- from nltk.corpus import stopwords
- from nltk.tokenize import word_tokenize, sent_tokenize



TFIDF
----------------------------
Short form for Term Frequency – Inverse Document Frequency, It is used to represent how important a given word is to a document on a complete collection relatively.
