s, f, l = input('String='), input('First Letter='), input('Second Letter=')
for i in range(1):
    f_in, l_in = s.rindex(f), s.index(l)
    if f_in == -1 or l_in == -1 or f_in > l_in: print(False)
    else: print(True)
