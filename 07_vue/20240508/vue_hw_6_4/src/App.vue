<script setup>
import { RouterLink, RouterView } from 'vue-router'
import MainPage from './components/MainPage.vue';

</script>

<template>
  <header>
    <div class="wrapper">
      <MainPage />
      <nav>
        <RouterLink to="/">Home</RouterLink> |
        <RouterLink to="/Other">Other</RouterLink> |
        <RouterLink to="/Students">Students</RouterLink>
      </nav>

    </div>
  </header>

  <RouterView />
</template>

<style scoped>

</style>
