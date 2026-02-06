# Lab 04: Loops and Functions Practice
# Student Name: [Your Name]
# Date: [Date]

# ============================================
# Question 1: Robot Return to Origin
# ============================================
print("\n" + "=" * 50)
print("Question 1: Robot Return to Origin")
print("=" * 50)
def robot_returns_to_origin(moves): # Atklass: U86R
    # Initialize starting position https://youtu.be/NZqufmO_YfQ
    x = 0
    y = 0
    for move in moves:
        if move == "U":
            y = y + 1 # y += 1
        elif move == "D":            
            y = y - 1 # y -= 1
        elif move == "R":
            x = x + 1 # x += 1
        elif move == "L":
            x = x - 1 # x -= 1                    
    return x == 0 and y == 0 

# Test cases
test_moves = ["UD", "LL", "UDLR", "LDRRLRUULR"]

for moves in test_moves:
    result = robot_returns_to_origin(moves)
    print("Moves '" + moves + "': Returns to origin? " + str(result))
print("=" * 50)
# ============================================
# Question 2: Two Sum
# ============================================
print("\n" + "=" * 50)
print("Question 2: Two Sum")
print("=" * 50)
# Part A: Brute Force with Nested Loops. # https://www.youtube.com/watch?v=NZqufmO_YfQ
def two_sum_brute_force(numbers, target):
    for i in range(len(numbers)):
        for j in range(i +1, len(numbers)):
            if numbers[i] + numbers[j] == target:
                return (i, j)
    return None

# Part B: Optimized with Dictionary
def two_sum_optimized(numbers, target):
    seen = {}  # Dictionary to store {number: index}
    for i in range(len(numbers)):
        needed = target - numbers[i]
        if needed in seen:
            return (seen[needed], i)
        seen[numbers[i]] = i
    return None

# Test cases
test_cases = [
    ([11, 15, 2, 7], 8),
    ([11, 15, 2, 7], 9),
    ([2, 7, 11, 15], 9),
    ([3, 2, 4], 6),
    ([3, 3], 6),
    ([1, 5, 3, 8, 2], 10)
]

print("=== Part A: Brute Force (Nested Loops) ===")
for numbers, target in test_cases:
    result = two_sum_brute_force(numbers, target)
    print("Numbers: " + str(numbers) + ", Target: " + str(target))
    print("Result: " + str(result))
    print()

print("=== Part B: Optimized (Dictionary) ===")
for numbers, target in test_cases:
    result = two_sum_optimized(numbers, target)
    print("Numbers: " + str(numbers) + ", Target: " + str(target))
    print("Result: " + str(result))
    print()

# ============================================
# Question 3: Shuffle the Array
# ============================================
print("\n" + "=" * 50)
print("Question 3: Shuffle the Array")
print("=" * 50)
def shuffle_array(nums, n):
    # Step 1: Split into two halves using slicing
    first_half = nums[:n]    # TODO: slice from start to n
    second_half = nums[n:]   # TODO: slice from n to end

    # Step 2: Create empty result list
    result = []
    # Step 3: Interleave using a for loop
    for i in range(n):
        result.append(first_half[i])
        result.append(second_half[i])

    

    return result

# Test cases
test_cases = [
    ([2, 5, 1, 3, 4, 7], 3),
    ([1, 2, 3, 4, 4, 3, 2, 1], 4),
    ([1, 1, 2, 2], 2)
]

for nums, n in test_cases:
    print("Original: " + str(nums))
    print("n = " + str(n))

    # Show the slices
    print("First half (nums[:" + str(n) + "]): " + str(nums[:n]))
    print("Second half (nums[" + str(n) + ":]): " + str(nums[n:]))

    # Get result
    result = shuffle_array(nums, n)
    print("Shuffled: " + str(result))
    print()

# ============================================
# Question 4: First Unique Character
# ============================================
print("\n" + "=" * 50)
print("Question 4: First Unique Character")
print("=" * 50)
# Helper function: Count all characters in a string
def count_characters(s): #leetcode. e=3
    counts = {}
    for char in s:
        if char in counts:
            counts[char] += 1
        else:
            counts[char] = 1
    return counts

# Main function: Find first unique character
def first_unique_character(s): #llove
    char_counts = count_characters(s)
    for i in range(len(s)):
        if char_counts[s[i]] == 1:
            return i
    return -1

# Test cases
test_strings = ["leetcode", "loveleetcode", "aabb", "python", "aabbcc"]

for s in test_strings:
    index = first_unique_character(s)

    if index != -1:
        print("First unique character in '" + s + "': index " + str(index) + " (character: '" + s[index] + "')")
    else:
        print("First unique character in '" + s + "': index -1 (no unique character)")

    # Show the character counts for understanding
    counts = count_characters(s)
    print("  Character counts: " + str(counts))
    print()