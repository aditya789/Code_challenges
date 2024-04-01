'''Challenge 3

Given the dictionary of words:
albums
barely
befoul
convex
hereby
jigsaw
tailor
weaver

And this collection of word “pieces”:
al
bums
bar
ely
be
foul
con
vex
here
by
jig
saw
tail
or
we
aver

Find all six letter words from the dictionary using the collection of pieces. In other words, iterate through the pieces to find the wholes:
al + bums => albums
bar + ely => barely
be + foul => befoul
etc …

Print the attempts used to find the whole:
albar != albums
alely != albums
albe != albums
etc …


Python Version :: Python 3.11.3'''


def matchedWords(words, pieces,length):
    matched = []
    for i in range(len(pieces)):
        for j in range(i+1,len(words)):
            word = pieces[i] + pieces[j]
            if len(word) == length and word in words.keys():
                matched.append(pieces[i] + pieces[j])
                words[word]+=1
            else:
                # Print the attempts used to find the whole:
                print(f'{pieces[i] + pieces[j]}')
    return words,matched

# calling the function and here words taken in a dictionary as requested
words = {'albums':0,'barely':0,'befoul':0,'convex' :0,'hereby' :0,'jigsaw':0 ,'tailor':0 ,'weaver':0}
pieces = ['al','bums','bar','ely','be','foul','con','vex','here','by','jig','saw','tail','or','we','aver',]
words,matched = matchedWords(words,pieces,6)
print(f'Words dictionary with count {words} and matched words in list format are {matched}')
