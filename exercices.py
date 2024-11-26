
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


# Reverse a string without using built-in reverse
def reverse_string(s):
    return s[::-1]  # or use a loop for more basic approach

# Check if string is palindrome
def is_palindrome(s):
    s = s.lower().replace(" ", "")  # Remove spaces and convert to lowercase
    return s == s[::-1]

def word_frequency(sentence):
    words = sentence.lower().split()
    frequency = {}
    for word in words:
        frequency[word] = frequency.get(word, 0) + 1
    return frequency

# Test it
text = "the cat and the dog and the bird"
print(word_frequency(text))

# Solution 1 - Simple for loop (recommended for interviews)
def sum_list(numbers):
    total = 0
    for num in numbers:
        total += num    # same as: total = total + num
    return total

def find_min_max(numbers):
    if not numbers:
        return None
    
    min_num = numbers[0]
    max_num = numbers[0]
    
    for num in numbers:  # Only one loop!
        if num < min_num:
            min_num = num
        if num > max_num:
            max_num = num
            
    return (min_num, max_num)

def count_numbers(numbers):
    frequency = {}
    for num in numbers:
        frequency[num] = frequency.get(num, 0) + 1
    return frequency  # You were missing the return statement

# Test it
test_numbers = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
print(count_numbers(test_numbers))  # {1: 1, 2: 2, 3: 3, 4: 4}

# Find missing number in array of 1 to n
def find_missing(nums):
    n = len(nums) + 1
    expected_sum = (n * (n + 1)) // 2
    actual_sum = sum(nums)
    return expected_sum - actual_sum

# Find duplicate elements
def find_duplicates(nums):
    duplicates = []
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] == nums[j] and nums[i] not in duplicates:
                duplicates.append(nums[i])
    return duplicates

# Find missing number in array of 1 to n
def find_missing(nums):
    n = len(nums) + 1
    expected_sum = (n * (n + 1)) // 2
    actual_sum = sum(nums)
    return expected_sum - actual_sum

# Find duplicate elements
def find_duplicates(nums):
    duplicates = []
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] == nums[j] and nums[i] not in duplicates:
                duplicates.append(nums[i])
    return duplicates

# Bubble Sort implementation
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

# Binary Search (for sorted arrays)
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

# Find first non-repeating character
def first_non_repeating(string):
    char_count = {}
    
    # Count occurrences
    for char in string:
        char_count[char] = char_count.get(char, 0) + 1
    
    # Find first char with count 1
    for char in string:
        if char_count[char] == 1:
            return char
    return None


def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    # Split the list in half
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    # Recursively sort each half
    left_sorted = merge_sort(left_half)
    right_sorted = merge_sort(right_half)

    # Merge the sorted halves
    return merge(left_sorted, right_sorted)

def merge(left, right):
    sorted_array = []
    while left and right:
        if left[0] < right[0]:
            sorted_array.append(left.pop(0))
        else:
            sorted_array.append(right.pop(0))

    # Append remaining elements (if any)
    sorted_array.extend(left)
    sorted_array.extend(right)
    
    return sorted_array

# Example Usage
arr = [38, 27, 43, 3, 9, 82, 10]
sorted_arr = merge_sort(arr)
print("Sorted array:", sorted_arr)

def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        # Check if the target is at the middle
        if arr[mid] == target:
            return mid
        # If target is smaller, search the left half
        elif arr[mid] > target:
            high = mid - 1
        # If target is larger, search the right half
        else:
            low = mid + 1

    return -1  # Target not found

# Example Usage
arr = [2, 5, 10, 15, 20, 25, 30]
target = 15
position = binary_search(arr, target)
print(f"Element {target} found at index:", position)

def are_anagrams(str1, str2):
    # Remove spaces and convert to lowercase for case-insensitivity
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()

    # Check if the sorted versions of both strings are equal
    return sorted(str1) == sorted(str2)

# Example Usage
str1 = "listen"
str2 = "silent"
result = are_anagrams(str1, str2)
print(f"Are '{str1}' and '{str2}' anagrams?", result)

def is_valid_brackets(s):
    # Stack to keep track of opening brackets
    stack = []
    
    # Dictionary to map closing brackets to opening brackets
    brackets_map = {
        ')': '(',
        '}': '{',
        ']': '['
    }
    
    # Iterate through each character in the string
    for char in s:
        # If it's a closing bracket
        if char in brackets_map:
            # Stack is empty or top element doesn't match
            if not stack or stack.pop() != brackets_map[char]:
                return False
        # If it's an opening bracket
        else:
            stack.append(char)
    
    # Check if all brackets were closed
    return len(stack) == 0

# Test cases
print(is_valid_brackets("()[]{}"))  # True
print(is_valid_brackets("([)]"))    # False
print(is_valid_brackets("{[]}"))    # True



class Book:
    def __init__(self, title, author, isbn, copies=1):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.available_copies = copies

    def __str__(self):
        return f"{self.title} by {self.author} (ISBN: {self.isbn})"


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        """Add a new book to the library"""
        self.books.append(book)
        return f"Added: {book}"

    def remove_book(self, isbn):
        """Remove a book using ISBN"""
        for book in self.books:
            if book.isbn == isbn:
                self.books.remove(book)
                return f"Removed: {book}"
        return "Book not found"

    def search_by_title(self, title):
        """Search books by title"""
        return [book for book in self.books if title.lower() in book.title.lower()]

    def search_by_author(self, author):
        """Search books by author"""
        return [book for book in self.books if author.lower() in book.author.lower()]

    def borrow_book(self, isbn):
        """Borrow a book"""
        for book in self.books:
            if book.isbn == isbn:
                if book.available_copies > 0:
                    book.available_copies -= 1
                    return f"Successfully borrowed: {book}"
                return "No copies available"
        return "Book not found"

    def return_book(self, isbn):
        """Return a book"""
        for book in self.books:
            if book.isbn == isbn:
                book.available_copies += 1
                return f"Successfully returned: {book}"
        return "Book not found"


# Test the implementation
def test_library():
    # Create library instance
    library = Library()

    # Create some books
    book1 = Book("Python Programming", "John Smith", "123-456", 2)
    book2 = Book("Web Development", "Jane Doe", "456-789", 1)

    # Add books
    print(library.add_book(book1))
    print(library.add_book(book2))

    # Search books
    print("\nSearching for 'Python':")
    for book in library.search_by_title("Python"):
        print(book)

    # Borrow and return books
    print("\nBorrowing book:")
    print(library.borrow_book("123-456"))
    print(library.borrow_book("123-456"))
    print(library.borrow_book("123-456"))  # Should show no copies available

    print("\nReturning book:")
    print(library.return_book("123-456"))

# Run the test
test_library()

def is_valid_brackets(s):
    # Initialize an empty stack to track opening brackets
    stack = []
    
    # Create a mapping of closing brackets to their corresponding opening brackets
    brackets_map = {
        ')': '(',   # Closing parenthesis maps to opening parenthesis
        '}': '{',   # Closing curly brace maps to opening curly brace
        ']': '['    # Closing square bracket maps to opening square bracket
    }
    
    # Iterate through each character in the input string
    for char in s:
        # Check if the current character is a closing bracket
        if char in brackets_map:
            # Two conditions for an invalid bracket sequence:
            # 1. Stack is empty (no opening brackets to match)
            # 2. The last opening bracket doesn't match the current closing bracket
            if not stack or stack.pop() != brackets_map[char]:
                return False
        else:
            # If it's an opening bracket, push it onto the stack
            stack.append(char)
    
    # After processing all characters, 
    # stack should be empty if all brackets are properly matched
    return len(stack) == 0


def countPrefixes(words, s):
    """
    Count the number of strings in words that are prefixes of string s.
    
    Args:
        words: List[str] - array of strings to check
        s: str - target string to check prefixes against
    
    Returns:
        int - count of strings in words that are prefixes of s
    """
    count = 0
    
    # Check each word in words array
    for word in words:
        # If word length is greater than s, it can't be a prefix
        if len(word) > len(s):
            continue
            
        # Check if word matches the beginning of s
        if s.startswith(word):
            count += 1
    
    return count


def find_second_largest(numbers):
    # Handle edge cases
    if len(numbers) < 2:
        return None
    
    # Remove duplicates and sort in descending order
    unique_sorted = sorted(set(numbers), reverse=True)
    
    # Return second element if exists
    return unique_sorted[1] if len(unique_sorted) > 1 else None

def common_chars(words):
    # Initialize the set of common characters with the first word
    common = set(words[0])
    
    # Iterate through the rest of the words
    for word in words[1:]:
        # Update common by intersecting with the current word's characters
        common &= set(word)
    
    # Convert the set back to a list to match the required output format
    return list(common)

# Example 1
words1 = ["Anypli", "Monastir", "Tunis"]
print(common_chars(words1))  # Output: ['n', 'i']

# Example 2
words2 = ["Anypli"]
print(common_chars(words2))  # Output: ['A', 'n', 'y', 'p', 'l', 'i']

