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

