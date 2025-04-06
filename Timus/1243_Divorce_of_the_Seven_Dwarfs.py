string_num = input()
result = 0
for c in string_num:
    result = ((result % 7) * 3 + (int(c) % 7)) % 7
print(result)