
class Solution:
    def topKFrequent(self, nums, k):
        count = {} 
        freq = [[] for i in range(len(nums) + 1)]

        for n in nums:
            count[n] = 1 + count.get(n, 0)
        for n, c in count.items():
            freq[c].append(n)

        res = []
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res
                    
                    
'''
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

Input: nums = [1,1,1,2,2,3], k = 2
the k no of elements that are most frequent
Output: [1,2]
'''
'''
Code Explanation
a dictionary is created with default length
the freq array is created with empty array of length nums+1
[[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]

for every element in nums:
    key to the dict is added and if it is a new entry then 0 is the value else incremented
from the dict key value pair is obtained with the items method (python default)
and it is appended to the position of the key of the dict 

{1:3,3:3}

1   |   2   |   3   |
    |       |  [1,3]|

the c is taken as the index
that is 1 repeats 3 times and 3 too repeats 3 times
so the 3 is taken as the index and the elements (key) having the same values is appended into the array in that index

another array for return the top k frequent 
as the highest freq element is found at the last of the freq array
so we loop from the last till 0

for each element(n) of array which the element(child array of the)of the freq
that n is appended into the res array
and when the res reaches the element k 
the program stops

'''

'''
Algorithm - BucketSort
Data Structures : Heap,Dictionary

an array to store the number 
and every element in the array is another array that stores the elements having that count

 1   |   2   |   3   |   4   |   5   |
[1,2]| [4,5] |       |       |       |

in the above example the elements 1 and 2 repeats once 
and 4,5 repeats twice so the elements are mapped onto that position

neetcode
'''
