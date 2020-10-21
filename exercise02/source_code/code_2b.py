# import numpy as np
# from numpy.random import choice
from random import choices
from collections import Counter
from scipy import stats

# c=0
# aa_milne_arr = ['a', 'b', 'c', 'd']
# rng = np.random.default_rng()
# values = rng.choice(aa_milne_arr, (250, 2), p=[0.5, 0.1, 0.1, 0.3])
# for value in values:
#     ans = ''.join(map(str, value))
#     c = c +1
#     print(ans)
# print("Total count : ", c)


def generate_cdf(corpus):
    chars = list(corpus) #changing corpus string to list
    total_length = len(chars)
    chars_count = Counter(chars) #get character wise count
    chars, probability = [], []
    for char in chars_count:
        chars.append(char)
        probability.append(chars_count[char] / total_length)
    return probability, chars


def generate_random_text(length, language):
    path = language + "_processed.txt"
    corpus = ""

    f = open(path, 'r')
    corpus = corpus + f.read()
    f.close()
    corpus = corpus.translate(str.maketrans('','','一■–ー\n\t'))


    prob, chars = generate_cdf(corpus)
    ans = ""
    val = choices(chars, prob, k=int(length))
    for value in val:
        ans = ans + value
    print(ans)
    return ans

lang = input("Input language for corpos (en, de, es, hu, tr): ")
leng = input("Input length of text required: ")
random_text = generate_random_text(leng, lang)
print("Random generated text is: ")
print(random_text)
