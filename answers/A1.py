n, min_val, max_val = int(input('n=')), int(input('minimum=')), int(input('maximum='))
c = i = 0
while True:
    i, sq = i+1, i**n
    if sq in range(min_val, max_val+1): c += 1
    if sq > max_val: break
print(f'{c} values raised to the power {n} lie in the range {min_val}, {max_val}')
