def reverse_in_place(arr):
    
   
    left = 0
    right = len(arr) - 1

   
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1



if __name__ == "__main__":
    numbers = [6,7,8,9,10]
    print("Original array:", numbers)

    reverse_in_place(numbers)

print("Reversed array:", numbers)

