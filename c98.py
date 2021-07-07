def count(file):

    sentence = open(file,'r')
    sentence = sentence.read()
    print(sentence)
    words=1
    characters=0
    for i in sentence:
        if(i==' '):
            words=words+1
        else:
            characters= characters+1
    
    print(words)
    print(characters)

count('text.txt')   