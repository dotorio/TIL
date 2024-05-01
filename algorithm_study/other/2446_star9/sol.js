let fs = require('fs')
let num = Number(fs.readFileSync('input.txt'))
for (let i = 0; i < num; i++) {
  let star = ''
  star += " ".repeat(i)
  star += "*".repeat((num-i)*2-1)
  console.log(star)
}
for (let i = num-2; i > -1; i--) {
  let star = ''
  star += " ".repeat(i)
  star += "*".repeat((num-i)*2-1)
  console.log(star)
}