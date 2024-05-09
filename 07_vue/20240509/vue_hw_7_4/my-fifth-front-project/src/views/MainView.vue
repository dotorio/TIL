<template>
  <div>
    <h2>메인 페이지</h2>
    <MainPage 
    v-for="person in store.balances"
    :key="person.name"
    :person="person"/>
  </div>
</template>

<script setup>
import MainPage from '@/components/MainPage.vue';

import { useBalanceStore } from '@/stores/balance.js';

const store = useBalanceStore()

console.log(store.balances)
</script>

<style scoped>

</style>