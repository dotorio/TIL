<template>
  <MainPage />
  <nav>
    <RouterLink to="/">Home</RouterLink> |
    <RouterLink to="/Other">Other</RouterLink>
  </nav>
  <RouterView />
</template>

<script setup>
  import MainPage from '@/components/MainPage.vue';
</script>

<style scoped>

</style>
