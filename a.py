area = set()
def square():
    a, b, c, d = map(int, input().split())
    for x in range(a, c):
        for y in range(b, d):
            area.add(1000*x+y)
square()
square()
square()
square()

print(len(area))
