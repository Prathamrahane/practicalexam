def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        guess = arr[mid]

        if guess == target:
            return mid
        elif guess < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1  # Target not found


# Example usage
numbers = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
target_number = 23

result = binary_search(numbers, target_number)

if result != -1:
    print("Target found at index", result)
else:
    print("Target not found")
