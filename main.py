import random

s = "Yeah baby I like it like that You gotta believe me when I tell you I said I like it like that"

def train(s):
    poss_words = dict()
    sample = s.split()
    for x in range(len(sample)-1):
        if sample[x] not in poss_words:
            poss_words[sample[x]] = [sample[x+1]]
        else:
            poss_words[sample[x]].append(sample[x+1])
    return poss_words

#print(train(s))

def generate(model, firstWord, numWords):
    custom_song = firstWord
    prevWord = firstWord
    for i in range(numWords-1):
        nextWord = random.choice(model[prevWord])
        custom_song += " " + nextWord
        prevWord = nextWord
    return custom_song

cardiB = train(s)
print(generate(cardiB, "I", 210))

