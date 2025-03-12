
#Display numbers that appear multiple times.
numbers = []
    
print("Enter 10 numbers:")
for i in range(10):
    while True:
        try:
            num = int(input(f"Number {i + 1}: "))
            numbers.append(num)
            break
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    
# Count duplicates
count_dict = {}
for num in numbers:
    count_dict[num] = count_dict.get(num, 0) + 1
    


