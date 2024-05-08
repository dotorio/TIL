<template>
  <div>
    <h2>학생 상세 정보 페이지입니다</h2>
    <p>이름 : {{ name }}</p>
  </div>
</template>

<script setup>
import { useRoute } from 'vue-router';

const route = useRoute()

console.log(route.params)

const name = route.params.name
</script>

<style lang="scss" scoped>

</style>