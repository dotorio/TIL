<template>
  <div>
    <h1>pinia 연습하기</h1>
    <ParentPage 
    v-for="member in Family.familyInfo"
    :key="member.familyName"
    :family="member"/>
  </div>
</template>

<script setup>
import ParentPage from './ParentPage.vue';

import { useFamilyStore } from '@/stores/family.js';

const Family = useFamilyStore()

// const props = defineProps(Family)
console.log(Family.familyInfo)

// import { useCounterStore } from '@/stores/counter';
// const store = useCounterStore()
// console.log(store.count)
</script>

<style scoped>

</style>