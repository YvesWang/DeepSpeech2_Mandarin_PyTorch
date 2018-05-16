import pickle
import Levenshtein as Lev

pinyin = pickle.load(open("word_dic.pickle", "rb"))

def correct_pinyin(word):
    inton = word[-1]
    word = word[:-1]
    dis = 0xffff
    for py in pinyin:
        cdis = Lev.distance(py, word)
        if cdis <= dis:
            dis = cdis
            cword = py
    return cword + inton

def correct_sentence(sentence):
    csentence = ""
    for word in sentence.split(" "):
        csentence += correct_pinyin(word) + " "
    return csentence[:-1]
