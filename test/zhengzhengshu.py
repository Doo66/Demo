# 正整数的反转

num = int(input('num = '))
reverse_num = 0
while num > 0:
    reverse_num = reverse_num * 10 + num % 10
    num //= 10
print(reverse_num)