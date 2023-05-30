import collections
strs =['eat', 'tea','tim','mit','can', 'tan', 'ate', 'nat', 'bat']
# creating a dictionary using collections method
ans = collections.defaultdict(list)

for s in strs:  # for each strings in the list we are making a list of size 26
    count = [0] * 26
    for c in s:  # for each letter in the string that is element of the list
        # we take the ascii value of the letter and sub it with the ascii value of the a so that it can be mapped into the correct position of the array
        count[ord(c) - ord("a")] += 1
        # eg: if the c is "b" which has ascii of 81 it should be mapped to the position of 1 in the list so inorder to map that into the correct position we need to sub it with the ascii value of a (80) that would result in position 1 of the list
    ans[tuple(count)].append(s)
    #print(ans)
    # the list that has the elements is taken as key and the words that contain the same letters are taken as the value pair for that key
print(ans.values())

'''
the keys are the array that contains the 26 zeros
where for anagram the letters are same so if we get the elements of the word then we can map it to the corresponding
ie bat and tab has got equal letters so in the key array(tuple) the part of "b",'a','t' are turned into the number of times it has repeated
so after bat has been encountered tab has the same pattern so if the key of bat matches with the key of tab then the value array is appended 
with that particular word
 {
    (1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0): ['bat']}

 {
    (1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0): ['bat', 'tab']
    }

 {
    (1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0): ['bat', 'tab'],
   (1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0): ['mat']
   }
 {
    (1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0): ['bat', 'tab'], 
    (1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0): ['mat', 'tam']
    }
 {
    (1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0): ['bat', 'tab'],
      (1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0): ['mat', 'tam'],
        (1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0): ['rat']
        }
 {
    (1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0): ['bat', 'tab'],
      (1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0): ['mat', 'tam'],
        (1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0): ['rat', 'tar']
        }
'''
