import sys
sys.stdin = open('input.txt')

icp = {'+':1,'*':2}

for tc in range(1, 11):
    N = int(input())
    formula = input()
    post = []
    stack = []
    for i in formula:
        
