<template>
  <div>
    <h3>자식 페이지입니다.</h3>
    <p>이름 : {{ childInfo.name }}</p>
    <p>나이 : {{ childInfo.age }}</p>
    <p>용돈 : {{ childInfo.balance }}</p>
    <button @click="giveMeAllowance">용돈 주세요.</button>
  </div>
</template>

<script setup>
const props = defineProps({
  childInfo: Object
})

const emit = defineEmits(['giveMeAllowance'])

const giveMeAllowance = function () {
  emit('giveMeAllowance')
}

</script>

<style scoped>

</style>