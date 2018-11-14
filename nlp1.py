import random
text="""Global warming is the term used to describe a gradual increase in the average temperature of the Earth's atmosphere and its oceans, a change that is believed to be permanently changing the Earth’s climate. There is great debate among many people, and sometimes in the news, on whether global warming is real (some call it a hoax). But climate scientists looking at the data and facts agree the planet is warming.
"""
n=3
ngrams = {}
        
for i in range (len(text)-n):
   gram=text[i:i+n]
   if gram not in ngrams.keys():
     ngrams[gram]=[]
   ngrams[gram].append(text[i+n])
            
currentGram =text[0:n]
result=currentGram
for i in range(100):
    if currentGram not in ngrams.keys():
        break
    possibilities= ngrams[currentGram]
    nextItem= possibilities[random.randrange(len(possibilities))]
    result +=nextItem
    currentGram =result[len(result)-n:len(result)]
    