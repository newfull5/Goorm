import math

a,b = map(int, input().split())

n = int(input())

if (n >= 2):
    for _ in range(n//2):
        a,b = int(a/2), b+math.ceil(a/2)
        a,b = a+math.ceil(b/2), int(b/2)
        
if n % 2 == 1:
    a,b = a/2, b+math.ceil(a/2)

print("{} {}".format(int(a),int(b)))
