<template>
  <div>
    <h3>자식 페이지입니다.</h3>
    <p>이름 : {{ child.name }}</p>
    <p>나이 : {{ child.age }}</p>
  </div>
</template>

<script setup>

const props = defineProps({
  child: Object
})
console.log(props.child)
</script>

<style scoped>

</style>