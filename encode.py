

# def encode(strs):
#     res = ""
#     for s in strs:
#         res += str(len(s)) + "#" + s
#     return res

# '''
# for every word in the string the length followed by a hash is added(#) 
# that is the encoding we used right here

# '''
   

# def decode(s):
#     res, i = [], 0

#     while i < len(s):
#         j = i
#         while s[j] != "#":
#             j += 1
#         length = int(s[i:j])
#         res.append(s[j + 1 : j + 1 + length])
#         i = j + 1 + length
#     return res

# '''
# in decoding the encoded element is passed
# the first integer followed by the hash is the lenght of the following string

# initally the i =0
# while the length of the string is not equal to i
# j is assigned to i
# while the letter in the string is not equal to "#"
# increment j
# when the hash is encountered another variable to store the value of the length
# the result array is appended with the letters after the hash until the length of the string which is given before

# '''

# print(encode(["hemmo","this","is"]))
# #5#hemmo4#this2#is
# print(decode("5#hemmo4#this2#is"))
# ['hemmo', 'this', 'is']



def encode(st):
    res= " "
    for s in st:
        res += str(len(s))+"#"+s
    return res


print(encode(['hellow','world']))

def decode(st):
    res,i = [],0
    
    while i < len(st):
        j = i
        while st[j] != "#":
            j += 1
        length = int(st[i:j])

