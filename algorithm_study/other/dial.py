A = str(input())
time = 0
for i in A:
    if i in ['A','B','C']:
        time += 3
    if i in ['D','E','F']:
        time += 4
    if i in ['G','H','I']:
        time += 5
    if i in ['J','K','L']:
        time += 6
    if i in ['M','N','O']:
        time += 7
    if i in ['P','Q','R','S']:
        time += 8
    if i in ['T','U','V']:
        time += 9
    if i in ['W','X','Y','Z']:
        time += 10
print(time)