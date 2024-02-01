student_count = int(input())
student_number = list(map(int, input().split()))
students = []
for i in range(1, student_count+1):
    students.insert(i - student_number[i-1] - 1, i)
print(*students)