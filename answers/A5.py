mod = 998244353
fb = [[0]*101 for _ in range(101)]
cr = [[0]*101 for _ in range(101)]


def func1(n, r):
    if n == r or r == 1:
        fb[r][n] = 1
        return
    if n > 0 and r > 0 and n > r:
        fb[r][n] = (fb[r-1][n-1] % mod + (r*fb[r][n-1]) % mod) % mod
        return
    fb[r][n] = 0


def func2(n, r):
    if n == 0 and r == 0:
        cr[r][n] = 0
        return
    if n >= 2 and r == 1:
        cr[r][n] = 1
        return
    if r > 0 and n > 0 and n >= 2*r:
        cr[r][n] = ((r*cr[r][n-1]) % mod + ((n-1)*cr[r-1][n-2]) % mod) % mod
        return
    cr[r][n] = 0


for r in range(1,101):
    for n in range(1, 101):
        func1(n, r)
        func2(n, r)

for _ in range(int(input())):
    f, c, r = list(map(int, input().split()))
    ans = 0
    if f + (c//2) >= r:
        minv = min(f, r)
        for i in range(1, minv+1):
            if r-i <= c//2:
                ans = (ans + (fb[i][f] * cr[r-i][c]) % mod) % mod
    print(ans)
