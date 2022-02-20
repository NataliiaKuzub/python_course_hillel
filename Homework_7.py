text = input("Please, enter your text here: ")
text = text.lower()

symbol_list = list(text.strip(''))
for i in symbol_list:
    if i == '.' or i == ',' or i == '?' or i == '!' or i == ':' or i ==';':
        symbol_list.remove(i)
text = ''.join(symbol_list)

word_list = text.split(" ")
word_set = set(word_list)

occurences = {}

for i in word_set:
    occurences[i] = ''

for i in occurences:
    occurences[i] = word_list.count(i)
print(occurences)

