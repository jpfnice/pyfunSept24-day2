"""
Exercise 5:
    
Given a list like this one:
    
words=["He", "does", "confess", "he", "feels", 
       "himself","distracted", "but", 
       "from", "what", "cause", "he", "will", 
       "by","no", "means", "speak"]

Create a dict like the following:
  {
  2 :['He', 'he', 'he', 'by', 'no'],
  3 :['but'],
  4 :['does', 'from', 'what', 'will'],
  5 :['feels', 'cause', 'means', 'speak'],
  7 :['confess', 'himself'],
 10 :['distracted']
  }

"""

words=["He", "does", "confess", "he", "feels", 
       "himself","distracted", "but", 
       "from", "what", "cause", "he", "will", 
       "by","no", "means", "speak"]

aDict=dict() # an empty dict

# This loop is used to analyse each element of the list 
# words in turn:
    
for w in words: 
    
    if len(w) in aDict: # There is already an element in the dict with this length
        aDict[len(w)].append(w)
    else: # A new pair needs to be added to the dict
        aDict[len(w)]=[w]

# Let see what the dict looks like:
        
for k,v in aDict.items():
    print(k, v)

print("-"*30)    

# or, to obtain a sorted list of pairs:

for k in sorted(aDict.keys()):
    print(k, aDict[k])
