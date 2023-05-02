import sys
if len(sys.argv) > 1 :
    print(*[i[::-1].swapcase() for i in sys.argv[:0:-1]], sep=" ")