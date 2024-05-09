<template>
  <div>
    <RouterLink :to="{name: 'main'}">main</RouterLink>
    <h1>pinia + router 연습하기</h1>
    <RouterView />
  </div>
</template>


<script setup>
import { RouterLink, RouterView } from 'vue-router';
import MainView from './views/MainView.vue';
</script>

<style scoped>

</style>
