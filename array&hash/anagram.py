class Solution(object):
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False
        
        count = {}
        
        for char in s:
            count[char] = count.get(char, 0) + 1
            #this updates the count dictionary with the char as key and if there already exists 
            # that char then the count is being updated else the char is added as key and the value 0            is returned and that value is added with 1

            #{"a":1} there was no n
            # when n is encountered then 0 is returned from the get method
            # the char "n" is added to the dict count as key and the 1 is added as the value  
        
        for char in t:
            if char not in count or count[char] == 0:
                return False
            count[char] -= 1
            #dict is simillar to hashmaps so inorder to decrease the time complextiy it is used insted of lists
        
        return True
        
        #Description
        
        #Given two strings s and t, return true if t is an anagram of s, and false otherwise.
        #An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
        
        #Input: s = "anagram", t = "nagaram"
        #Output: true
