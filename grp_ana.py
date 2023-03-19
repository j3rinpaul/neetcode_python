words = ['eat', 'tea','tim','mit','can', 'tan', 'ate', 'nat', 'bat']
groups = {}
for word in words:
    sorted_word = ''.join(sorted(word)) #here each word is sorted and taken as a key
    if sorted_word in groups:
        groups[sorted_word].append(word)
    else:
        groups[sorted_word] = [word]
print(list(groups.values()))

'''
algorithm
declare a dictionary 
sort the words inside the given list if sorted words in ley of dictionary 
then append the value list with the word got 
after the dictionary ends print the values as a list
'''