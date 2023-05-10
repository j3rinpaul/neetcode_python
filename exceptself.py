array = [1,2,3,4]
res = [1]*len(array)#creating an array of elements 1 with length of the given array
#calculate the prefix
prefix  = 1
for i in range(len(array)):
    res[i] = prefix #storing the prefix value into the resultant array
    prefix *= array[i] #updating the prefix with multiplying with the elements before the num array

postfix = 1
for i in range(len(array)-1 ,-1,-1): #loop reverse order
    res[i] *= postfix #initially the postfix is 1 and it is multiplied with the last element of the resultant
    #the postfix is updated the multiplying the elements from back
    postfix *= array[i]

print(res)

'''
Given an integer array nums, return an array answer such that 
answer[i] is equal to the product of all the elements of nums except nums[i].

Algorithm

1. created an array result of length of the input array and fill it with 1
2. set prefix = 1 
3. for nums in the array insert the prefix into the result array and update the prefix
   by multiplying with the elements until that index

   the prefix is mul and inserted into the resultant array

4.set postfix = 1
5.for nums in the array multiply the elements in the array with the postfix and 
  insert it into the resultant update the postfix by multiplying it with the elements of the array(reverse order)

  initally the postfix is 1 so,1 is mul with the last element of the result and it is inserted into the last pos
  the postfix is then updated by mul with the element of the array from rev

  the postfix is mul with the elements of the result and inserted into the pos and postfix is updated

6.print the result array
  






'''