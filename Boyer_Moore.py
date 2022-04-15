mot = input("Le mot à chercher : ")

def traitement(mot: str, dic: dict = {}) -> dict:
    for i in range(len(mot)-1):
        dic[mot[i]] = len(mot)-i-1
    return dic

def comp(text: str, mot: str) -> tuple:
    long_mot = len(mot)
    for i in range(long_mot):
        if text[long_mot-i-1] != mot[long_mot-i-1]:
            return False, i, text[long_mot-i-1]
    return True, 0, ''

def word_search(text: str, mot: str) -> int:
    dic = traitement(mot)
    i = 0
    long_mot = len(mot)
    while i+long_mot < len(text):
        txt = text[i:i+long_mot]
        tupl = comp(txt, mot)
        if tupl[0]:
            return i
        else:
            if tupl[2] in dic:
                i = max(i+1, i+dic[tupl[2]]-tupl[1])
            else:
                i = i+long_mot-tupl[1]
    return -1

rep = word_search(fich, mot)
print(f"Le rang du mot '{mot}' est {rep}")
