class Solution(object):
    def containsDuplicate(self, nums):
        return (len(nums)!= len(set(nums)))
        #if the set contains duplicate elements then the no of elements in the {set}would not be equal to the number of given list

        #Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

        #Input: nums = [1,2,3,1]
        #Output: true

        # the most optimal solution