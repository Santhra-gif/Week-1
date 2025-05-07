total_words = 0

# Function to count the words
def word_count(line):
    global total_words
    total_words = len(line.split()) + total_words

# To open a text file
f = open('Sample.txt','r')

for x in f:
    word_count(x)
 
print(total_words)