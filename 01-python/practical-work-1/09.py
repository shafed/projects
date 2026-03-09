a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())

bricks = sorted([a, b, c])
hole = sorted([d, e])

if bricks[0] <= hole[0] and bricks[1] <= hole[1]:
    print("YES")
else:
    print("NO")
