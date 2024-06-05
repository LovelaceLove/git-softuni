n = int(input())

for num in range (1, n+1):
    is_special = False
    num_as_string = str(num)
    digits_sum = 0

for ch in num_as_string:
    digits_sum += int(ch)

if digits_sum == 5 or digits_sum == 7 or digits_sum == 11:
    is_special = True 

print(f'{num} -> {is_special}')


      