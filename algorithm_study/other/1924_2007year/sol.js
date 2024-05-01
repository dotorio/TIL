const fs = require('fs')
const input = fs.readFileSync('input.txt').toString().split(' ')
const month = Number(input[0])
const day = Number(input[1])
const monthList = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30]
const dayList = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']
let dayConut = 0
// 지난 달만큼 날수를 더하고
for (let i = 0; i < month-1; i++) {
  dayConut += monthList[i]
}
// 지난 일-1만큼 날수를 더해서
dayConut += day-1
// 7로 나눈 나머지를 리스트 인덱스에 대응해서 출력한다
console.log(dayList[dayConut%7])