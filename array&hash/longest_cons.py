def longestConsecutive(nums):

    #convert the nums array into a set to avoid duplicate elements
    numSet = set(nums) 
    longest = 0

    for n in nums:
            #checking if that element is the starting of the sequence 
            #if n-1 is in the set then the starting of the sequence is some other element
            if (n-1) not in numSet:
                length = 0
                #checking whether the consecutive element is found in the set
                #initally the length is 0 so the same element is taken
                # on the second iteration the next consecutive  element is taken and checcking whether it is found or not
                #if it is not found the loop exits
                while (n+length) in numSet:
                    length += 1
                #the longest is stored
                longest = max(length,longest)

    return longest

nums = [1,87,2,3,76,4,77]

print(longestConsecutive(nums=nums))


#same with lower complexities

# num_set = set(nums)
#         longest_seq = 0
#         for loop in num_set: //here the set is taken for every operation
#             if loop - 1 not in num_set:
#                 current_seq = 1
#                 while loop + current_seq in num_set:
#                     current_seq += 1
#                 longest_seq = max(longest_seq, current_seq)
#         return longest_seq




#  #convert the nums array into a set
#         longest = 0
#         nums = set(nums)
#         for num in nums:
#             if num - 1 not in nums:
#                 # we are at start of sequence
#                 next_num = num + 1
#                 while next_num in nums:
#                     next_num += 1
#                 longest = max(longest, next_num - num)
#                 #next_num - num returns the difference that is the size 
#         return longest