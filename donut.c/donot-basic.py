import time
import sys

A = 0
B = 0
j = 0
i = 0
z[1760]
b[1760]
print("\x1b[2J")
while True:
    # memset(b,32,1760);
    # memset(z,0,7040);
    while (j < 6.28):
        j += 0.07
        while (i < 6.28):
            i += 0.02
            c = sin(i)
            d = cos(j)
            e = sin(A)
            f = sin(j)
            g = cos(A)
            h = d + 2
            D = 1 / (c * h * e + f * g + 5)
            l = cos(i)
            m = cos(B)
            n = sin(B)
            t = c * h * g - f * e
            x = 40 + 30 * D * (l * h * m - t * n)
            y = 12 + 15 * D * (l * h * n + t * m)
            o = x + 80 * y
            N = 8 * ((f * e - c * d * g) * m - c * d * e - f * g - l * d * n)
            if(22 > y and y > 0 and x > 0 and 80 > x and D > z[o]):
                z[o] = D
                b[o] = ".,-~:;=!*#$@"[N if N > 0 else 0]
                # [N > 0 ? N: 0]

    print("\x1b[H")
    k = 0
    while (k < 1761):
        k += 1
        sys.stdout.write(b[k] if k % 80 else 10)
        sys.stdout.flush()
        # putchar(k % 80 ? b[k]: 10)
        A += 0.00004
        B += 0.00002

    time.sleep(30000)
