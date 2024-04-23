const player1 = document.querySelector('#player1-img')
const player2 = document.querySelector('#player2-img')
// console.log(player1)
// player1.src = './img/rock.png''
const btnScissors = document.querySelector('#scissors-button')
const btnRock = document.querySelector('#rock-button')
const btnPaper = document.querySelector('#paper-button')


function getRandomInt(max) {
  return Math.floor(Math.random() * max);
}



const list = ['scissors', 'rock', 'paper']

let nIntervId;

function changeImg() {
  // 간격이 이미 설정되어 있는지 확인합니다
  if (!nIntervId) {
    nIntervId = setInterval(changeSrc, 100);
  }
}
function changeSrc() {
  player2.src = `./img/${list[getRandomInt(3)]}.png`
}
function stopChange(choice2, gameResult) {
  clearInterval(nIntervId);
  // 변수에서 intervalID를 해체합니다
  nIntervId = null;
  player2.src = `./img/${choice2}.png`
  console.log(gameResult)
  console.log(modalChange(gameResult))
}

function playgame(choice1, choice2) {
  const count1 = 0
  const count2 = 0
  if (choice1 === 'scissors') {
    if (choice2 === 'rock') {
      
      return 2
    }
    else if (choice2 === 'paper') {
      return 1
    }
    else {
      return 0
    }
  }
  else if (choice1 === 'rock') {
    if (choice2 === 'scissors') {
      
      return 1
    }
    else if (choice2 === 'paper') {
      return 2
    }
    else {
      return 0
    }
  }
  else {
    if (choice2 === 'rock') {
      
      return 1
    }
    else if (choice2 === 'scissors') {
      return 2
    }
    else {
      return 0
    }
  }
}

const buttonClickHandler = function (choice) {
  const choice1 = choice.srcElement.alt
  player1.src = `./img/${choice1}.png`
  btnScissors.disabled = true
  btnRock.disabled = true
  btnPaper.disabled = true
  const choice2 = list[getRandomInt(3)]
  const gameResult = playgame(choice1, choice2)
  setTimeout(stopChange, 3000, choice2, gameResult)
  changeImg()
}

const modalChange = function (gameResult) {
  const modalContent = document.querySelector('.modal-content')
  console.log(modalContent)
  const modal = document.querySelector('.modal')
  console.log(modal)
  
  if (gameResult === 1) {
    modalContent.textContent = 'player 1 win'
  } else if (gameResult === 2) {
    modalContent.textContent = 'player 2 win'
  } else {
    modalContent.textContent = 'draw'
  }
  modal.style = 'display: flex'
}

btnScissors.addEventListener('click', buttonClickHandler)
btnRock.addEventListener('click', buttonClickHandler)
btnPaper.addEventListener('click', buttonClickHandler)
