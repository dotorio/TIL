rounds = int(input())
for i in range(rounds):
    a, *scab_a = map(int, input().split())
    b, *scab_b = map(int, input().split())
    if scab_a.count(4) > scab_b.count(4):
        print('A')
    elif scab_a.count(4) == scab_b.count(4):
        if scab_a.count(3) > scab_b.count(3):
            print('A')
        elif scab_a.count(3) == scab_b.count(3):
            if scab_a.count(2) > scab_b.count(2):
                print('A')
            elif scab_a.count(2) == scab_b.count(2):
                if scab_a.count(1) > scab_b.count(1):
                    print('A')
                elif scab_a.count(1) == scab_b.count(1):
                    print('D')
                else:
                    print('B')
            else:
                print('B')
        else:
            print('B')
    else:
        print('B')
