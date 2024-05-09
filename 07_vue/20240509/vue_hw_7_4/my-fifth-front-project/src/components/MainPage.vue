<template>
  <div>
    <p>이름 : {{ person.name }}</p>
    <p>잔고 : {{ person.balance }}</p>
    <button @click="goDetail(person.name)">updateBalance</button>
    <hr>
  </div>
</template>

<script setup>
import MainView from '@/views/MainView.vue';
import { useRouter } from 'vue-router';

const router = useRouter()

const goDetail = function (name) {
  router.push({name: 'update', params: {'name':name}})
}

defineProps({person : Object})
</script>

<style scoped>

</style>