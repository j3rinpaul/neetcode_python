nums = [2,4,3,7]
target = 9
'''
algorithm

a dictionary is created
using enumerate function: index and the element is returned
calculating the complement 
"the base idea is sum of two number from the array should be of the target"
so we do is take the complement by sub element from that target
and check whether the complement is in the dict
and if yes then return the index of the complement and the index of the element
else it returns none

dictionary is used cause while finding the element is whether inside the array
it takes another loop so inorder to decrease the complexity the hashmap ds is used
'''
seen = {}
for index, num in enumerate(nums):
    print(seen)
    complement = target - num
    print(complement)
    if complement in seen:
        print( [seen[complement], index])
    seen[num] = index
   


print("None") 
'''
during the first iteration the dict is null so it is returned
{} 
the complement 9-2
7 
 as the complement is not found in the dict the num and index is added to the dict
{2: 0}
 the next complement
5 
as the next complement is also not found on the dict so the num and index is added to the dict
{2: 0, 4: 1}
next complement
6
not found added to the dict
{2: 0, 4: 1, 3: 2}
next complement
2
the complement is found in the dict so the index of complement and the element(found on the for loop) is returned
[0, 3]

'''