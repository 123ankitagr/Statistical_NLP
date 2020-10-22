import string

#
# def unigram(corpus):
#     unigram_frequencies = dict()
#     corpus_length = 0
#     for token in corpus:
#         unigram_frequencies[token] = unigram_frequencies.get(token, 0) + 1
#         corpus_length += 1
#     unique_words = len(unigram_frequencies)


def preprocess_text(filename):
    # filename = "English_train.txt"
    corpus = ""
    f = open(filename, 'r', encoding='utf8')
    corpus = corpus + f.read()
    f.close()
    # preprocessed = preprocess_text(corpus)
    corpus = corpus.translate(str.maketrans('', '', string.punctuation))
    corpus = corpus.translate(str.maketrans('','', '一■–ー'))
    corpus = corpus.lower()
    corpus = corpus.strip()
    corpus = corpus.split()
    return corpus


def unigram_cp(corpus):
    wordprob = {}
    for token in corpus():
        if token not in wordprob:
            wordprob[token] = [corpus.count(token) / len(corpus)]
    return wordprob


def bigram_cp(corpus):
    wordprob = unigram_cp(corpus)
    prev = 0
    for token in corpus[1:]:
        if len(wordprob[token]) == 1:
            wordprob[token].append({})
        if corpus[prev] in wordprob[token][1]:
            wordprob[token][1][corpus[prev]] += 1 / (wordprob[corpus[prev]][0] * len(corpus))
        else:
            wordprob[token][1][corpus[prev]] = 1 / (wordprob[corpus[prev]][0] * len(corpus))

        prev += 1
    return wordprob


def calculate_perplexity(prob, test_words, train_words):
    return


train_corpus = preprocess_text("English_train.txt")
test_corpus = preprocess_text("English_test.txt")

word_prob = bigram_cp(train_corpus)
pp = calculate_perplexity(word_prob,test_corpus,train_corpus)
print(pp)
