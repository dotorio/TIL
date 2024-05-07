<template>
  <div>
    <p>{{ myMsg }}</p>
    <p>{{ dynamicProps }}</p>
    <ParentGrandChild :my-msg="myMsg"/>
    <button @click="$emit('someEvent')">클릭</button>
  </div>
</template>

<script setup>
import ParentGrandChild from '@/components/ParentGrandChild.vue'
// 내려받은 프롭스를 선언
// defineProps(['myMsg'])
// defineProps({
//   myMsg: String
// })

const props = defineProps({
  myMsg: String,
  dynamicProps: String
})

console.log(props)
console.log(props.myMsg)
</script>

<style scoped>

</style>