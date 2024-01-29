a, b = map(int, input().split())

gcd_a = a
gcd_b = b
lcm_a = a
lcm_b = b

while gcd_a != 0 and gcd_b != 0:
    if gcd_a > gcd_b:
        gcd_a -= gcd_b
    else:
        gcd_b -= gcd_a
if gcd_a == 0:
    gcd = gcd_b
else:
    gcd = gcd_a

while lcm_a != lcm_b:
    if lcm_a > lcm_b:
        lcm_b += b
    else:
        lcm_a += a
        
print(gcd)
print(lcm_a)