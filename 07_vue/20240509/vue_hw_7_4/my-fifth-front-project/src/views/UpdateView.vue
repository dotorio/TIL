<template>
  <div>
    <h2>데이터 수정 페이지</h2>
    <p>이름 : {{ person.name }}</p>
    <p>잔고 : {{ person.balance }}</p>
    <button @click="store.plusBalance(person.name)">+</button>
  </div>
</template>

<script setup>
import { useBalanceStore } from '@/stores/balance';
import { useRoute } from 'vue-router';
const route = useRoute()

const store = useBalanceStore()

const person = store.findPersonName(route.params.name)

</script>

<style scoped>

</style>