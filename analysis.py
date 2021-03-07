def run(background, news):
    import pandas as pd
    import os, os.path
    import re
    import nltk
    import numpy as np
    from nltk.corpus import stopwords
    from nltk.stem.porter import PorterStemmer
    from nltk.tokenize import RegexpTokenizer
    from nltk.stem.wordnet import WordNetLemmatizer
    from nltk.sentiment import SentimentIntensityAnalyzer
    from collections import Counter
    from sklearn.feature_extraction.text import CountVectorizer
    from sklearn.metrics.pairwise import cosine_similarity
    from sklearn.feature_extraction.text import TfidfTransformer
    from scipy.sparse import coo_matrix
    from numpy import mean

    # import the kaggle news_ref
    news_ref = pd.read_csv(background)

    # rename the text column, shorten
    news_ref = news_ref.rename(columns={"content":'text'})
    news_ref = news_ref.head(1000)

    # get the API-obtained news articles (here it's just kaggle)
#     news = pd.read_csv(filename)
#     news = news.rename(columns={"content":'text'})
#     news = news.head(10)

    # get the word count for each article
    news_ref['word_count'] = news_ref['text'].apply(lambda x: len(x.split(" ")))
    news['word_count'] = news['text'].apply(lambda x: len(x.split(" ")))

    # creating a list of stopwords and adding custom stopwords
    stop_words = set(stopwords.words("english"))
    new_words = []
    stop_words = stop_words.union(new_words)

    # create a corpus to store the words in
    corpus_ref = []
    corpus = []

    # clean the text (reference)
    for i in range(len(news_ref)):

        # remove punctutation
        text = re.sub('[^a-zA-Z]',' ', news_ref['text'][i])

        # convert to lowercase
        text = text.lower()

        # remove tags
        text = re.sub("&lt;/?.*?&gt;"," &lt;&gt; ",text)

        # remove special characters and digits
        text = re.sub("(\\d|\\W)+"," ",text)

        # convert to list from string
        text = text.split()

        # stem
        ps = PorterStemmer()

        # Lemmatisation
        lem = WordNetLemmatizer()
        text = [lem.lemmatize(word) for word in text if not word in stop_words]
        text = " ".join(text)
        corpus_ref.append(text)

    # clean the text (API)
    for i in range(len(news)):

        # remove punctutation
        text = re.sub('[^a-zA-Z]',' ', news['text'][i])

        # convert to lowercase
        text = text.lower()

        # remove tags
        text = re.sub("&lt;/?.*?&gt;"," &lt;&gt; ",text)

        # remove special characters and digits
        text = re.sub("(\\d|\\W)+"," ",text)

        # convert to list from string
        text = text.split()

        text = [lem.lemmatize(word) for word in text if not word in stop_words]
        text = " ".join(text)
        corpus.append(text)

    # get the vocabulary keys, set tf-idf parameters
    cv = CountVectorizer(max_df = .8,stop_words=stop_words,max_features=10000, ngram_range=(1,3))
    X = cv.fit_transform(corpus+corpus_ref)

    # start tf-idf
    tfidf_transformer=TfidfTransformer(smooth_idf=True,use_idf=True)
    tfidf_transformer.fit(X)

    # get feature names from the kaggle news_ref
    feature_names=cv.get_feature_names()



    def checkForRepeats(keywords,conf):
        words = []
        confs = []
        repeat = 0
        for i in range(len(keywords)):
            for j in range(len(keywords)):
                if (i != j) and (keywords[i] in keywords[j]):
                    repeat = 1
            if repeat == 0:
                words.append(keywords[i])
                confs.append(conf[i])
            repeat = 0
        return [words, confs]

    # set number of articles
    n_articles = len(news)

    # set number of keywords
    n_keywords = 5

    # cosine similarity of the articles we want to look at
    def get_cosine_sim(*strs): 
        vectors = [t for t in get_vectors(*strs)]
        return cosine_similarity(vectors)

    def get_vectors(*strs):
        text = [t for t in strs]
        vectorizer = CountVectorizer(text)
        vectorizer.fit(text)
        return vectorizer.transform(text).toarray()

    # do the cosine sim for 9 articles (the max we'd be doing)
    sims = get_cosine_sim(*corpus[:n_articles])
    sim = []
    for i in range(n_articles):
        sim.append(np.mean(sims[i][np.arange(len(sims[i]))!=i]))

    # initialize the sentiment analyzer
    sia = SentimentIntensityAnalyzer()

    # function for sorting tf_idf in descending order
    def sort_coo(coo_matrix):
        tuples = zip(coo_matrix.col, coo_matrix.data)
        return sorted(tuples, key=lambda x: (x[1], x[0]), reverse=True)

    # get the feature names and tf-idf score of top n items
    def extract_topn_from_vector(feature_names, sorted_items, topn=10):

        # use only top n items from vector
        sorted_items = sorted_items[:topn]

        score_vals = []
        feature_vals = []

        # word index and corresponding tf-idf score
        for idx, score in sorted_items:

            # keep track of feature name and its corresponding score
            score_vals.append(round(score, 3))
            feature_vals.append(feature_names[idx])

        # create a tuples of feature,score
        # results = zip(feature_vals,score_vals)
        results= {}
        for idx in range(len(feature_vals)):
            results[feature_vals[idx]]=score_vals[idx]

        return results

    # create lists to return results
    words = []
    sentiments = []
    confs = []

    # iterate through the articles to get keywords and sentiment
    for i in range(n_articles):

        # fetch document for which keywords needs to be extracted
        doc=corpus[i]

        #generate tf-idf for the given document
        tf_idf_vector=tfidf_transformer.transform(cv.transform([doc]))

        # sort the tf-idf vectors by descending order of scores
        sorted_items=sort_coo(tf_idf_vector.tocoo())

        # extract only the top n; n here is 10
        keywords=extract_topn_from_vector(feature_names,sorted_items,n_keywords)

        # convert keywords to format, check for repeats
        keys = list(keywords.items())
        conf = [i[1] for i in keys]
        keys = [i[0] for i in keys]
        [keys, conf] = checkForRepeats(keys,conf)

        # gets the sentiment
        sent = sia.polarity_scores(corpus[i])
        sent = sent.get('compound')

        # add to lists
        words.append(keys)
        sentiments.append(sent)
        confs.append(conf)

        #print
    #     print("\nArticle: ",i)
    #     print("\nSentiment: ",sent)
    #     print("\nKeywords: ")
    #     for i in range(len(keys)):
    #         print(keys[i],conf[i])

    # print(len(sentiments))
    # print(keys)
    # print(len(words))
    # print(confs)
    # print(len(confs))
    # print(len(sim))

    # add outputs to pandas database    
    outputs = pd.DataFrame({'sentiment': sentiments, 'keywords': words,'conf':confs,'similarity':sim})
    return pd.concat([news,outputs],axis=1)