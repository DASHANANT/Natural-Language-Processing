Word-sense disambiguation (WSD)
=====================================
Word-sense disambiguation (WSD) is an open problem in computational linguistics concerned with identifying which sense of a word is used in a sentence. The solution to this issue impacts other computer-related writing, such as discourse, improving relevance of search engines, anaphora resolution, coherence, and inference

Disambiguation requires two strict inputs: a dictionary to specify the senses which are to be disambiguated and a corpus of language data to be disambiguated (in some methods, a training corpus of language examples is also required). WSD task has two variants: "lexical sample" (disambiguating the occurrences of a small sample of target words which were previously selected) and "all words" task (disambiguation of all the words in a running text). "All words" task is generally consider a more realistic form of evaluation, but the corpus is more expensive to produce because human annotators have to read the definitions for each word in the sequence every time they need to make a tagging judgement, rather than once for a block of instances for the same target word.


Approaches and methods
====================
There are two main approaches to WSD – deep approaches and shallow approaches.

There are four conventional approaches to WSD:
----------------------------------------------------
- *Dictionary- and knowledge-based methods*: These rely primarily on dictionaries, thesauri, and lexical knowledge bases, without using any corpus evidence.
- *Semi-supervised or minimally supervised methods*: These make use of a secondary source of knowledge such as a small annotated corpus as seed data in a bootstrapping process, or a word-aligned bilingual corpus.
- *Supervised methods*: These make use of sense-annotated corpora to train from.
- *Unsupervised methods*: These eschew (almost) completely external information and work directly from raw unannotated corpora. These methods are also known under the name of word sense discrimination.


Mainly My implementatio focus on follwing Algorithms
------------------------------
- Lesk algorithm (Dictionary- and knowledge-based methods)
- Naive bayes (Supervised methods)
- Sense rank (Graph-based methods)
- yarrowsky decision list (Unsupervised methods) 
