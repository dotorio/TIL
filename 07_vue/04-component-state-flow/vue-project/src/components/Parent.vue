<template>
  <div>
    <ParentChild 
    my-msg="message"
    :dynamic-props="name"
    @some-event="someCallback" />
  </div>
  <ParentItem
    v-for="item in items"
    :key="item.id"
    :my-prop="item" />
</template>

<script setup>
import { ref } from 'vue'
import ParentChild from '@/components/ParentChild.vue'
import ParentItem from '@/components/ParentItem.vue'

const name = ref('Alice')

const items = ref([
  { id:1, name: '사과'},
  { id:2, name: '바나나'},
  { id:3, name: '딸기'}
])

const someCallback = function () {
  console.log('ParentChild가 발신한 이벤트를 수신했어요.')
}

</script>

<style scoped>

</style>