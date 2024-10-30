import itertools

sum = 0
for code in itertools.product('АВГУСТ', repeat=5):
    if code.count('Т') == 1:
        sum = sum + 1
print("#1", sum)


sum = 0
for code in itertools.product('СТЕПАН', repeat=4):
    if code.count('С') + code.count('Т') + code.count('П') + code.count('Н') == 2:
        sum = sum + 1
print("#2", sum)




sum = 0
for code in itertools.permutations('РОСОМАХА'):
    wrong = False
    for i in range(8-1):
        if code[i] in 'ОА' and code[i+1] in 'ОА':
            wrong = True
            break
        if code[i] in 'РСМХ' and code[i+1] in 'РСМХ':
            wrong = True
            break
    if not wrong:
        sum += 1
print('#6-1', sum/4)




S = list(set(itertools.permutations('РОСОМАХА')))
sum = 0
for code in S:
    wrong = False
    for i in range(8-1):
        if code[i] in 'ОА' and code[i+1] in 'ОА':
            wrong = True
            break
        if code[i] in 'РСМХ' and code[i+1] in 'РСМХ':
            wrong = True
            break
    if not wrong:
        sum += 1
print('#6-2', sum)




sum = 0
for code in itertools.product('НАСТЯ', repeat=7):
    if code.count('Н') == 2 and code.count('А') >= 1:
        sum = sum + 1

print("#7", sum)

