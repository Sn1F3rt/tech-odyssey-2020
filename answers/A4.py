def move_rod(rod_first, rod_second, rod_mid, n):
    if n == 1: return print(f'Move ring 1 from source {rod_first} to destination {rod_second}')
    move_rod(rod_first, rod_mid, rod_second, n-1)
    print(f'Move ring {n} from source {rod_first} to destination {rod_second}')
    move_rod(rod_mid, rod_second, rod_first, n-1)
    
    
move_rod('A', 'B', 'C', int(input('Number of rings (n) =')))
