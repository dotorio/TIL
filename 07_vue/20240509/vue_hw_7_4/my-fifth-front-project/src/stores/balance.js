import { ref, computed } from 'vue'
import { defineStore } from 'pinia'

export const useBalanceStore = defineStore('balance', () => {
  const balances = ref([
    {
      name: '김하나',
      balance: 100000
      },
      {
      name: '김두리',
      balance: 10000
      },
      {
      name: '김서이',
      balance: 100
      },
  ])

  const findPersonName = function (name) {
    console.log(balances)
    const personInfo = balances.value.find((person) => 
      person.name === name
    )
    console.log(personInfo)
    return personInfo
  }

  const plusBalance = function (name) {
    const personInfo = balances.value.find((person) => 
      person.name === name
    )
    personInfo.balance += 1000
    // return personInfo.balance
  }
  return {balances, findPersonName, plusBalance}
})