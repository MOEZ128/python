
def removeDuplicates(nums):
    if not nums:
        return 0
    
    i = 0
    for j in range(1, len(nums)):
        if nums[j] != nums[i]:
            i += 1
            nums[i] = nums[j]
    
    return i + 1
    
    Example: nums = [1, 1, 2, 2, 3]

Initial: i = 0
         j = 1
[1, 1, 2, 2, 3]
 i  j

When j=1: nums[j]==nums[i], so skip
[1, 1, 2, 2, 3]
 i     j

When j=2: nums[j]!=nums[i], so i++ and copy
[1, 2, 2, 2, 3]
    i     j

When j=3: nums[j]==nums[i], so skip
[1, 2, 2, 2, 3]
    i        j

When j=4: nums[j]!=nums[i], so i++ and copy
[1, 2, 3, 2, 3]
       i        j

Final result: return i+1 = 3
First three elements: [1, 2, 3]

 def find_max(numbers):
    if not numbers:  # Check if list is empty
        return None
    max_num = numbers[0]
    for num in numbers:
        if num > max_num:
            max_num = num
    return max_num

# Test it
numbers = [4, 2, 9, 7, 5, 1]
print(find_max(numbers))  # Should print 9
