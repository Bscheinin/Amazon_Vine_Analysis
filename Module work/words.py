import nltk
from nltk import word_tokenize
text = word_tokenize("I would rather be day drinking.")
output = nltk.pos_tag(text)
print(output)