import gensim.downloader as api
# api.info('word2vec-google-news-300')
wv=api.load('word2vec-google-news-300')

print(wv.most_similar('king'))