<template>
  <div id="child">
    <h3>자식 페이지</h3>
    {{ child.name }}
  </div>
</template>

<script setup>
defineProps({child : Object})
</script>

<style scoped>
#child {
  background-color: #fff;
  border: 1px solid black;
  padding: 15px;
  margin:  10px;
}
</style>