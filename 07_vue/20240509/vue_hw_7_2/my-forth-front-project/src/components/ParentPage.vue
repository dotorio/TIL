<template>
  <div id="parent">
    <h2>부모 컴포넌트</h2>
    <p>{{ family.father }}</p>
    <p>{{ family.mother }}</p>
    <ChildPage
      v-for="child in family.children"
      :key="child.name"
      :child="child" />
  </div>
</template>

<script setup>
import ChildPage from './ChildPage.vue';


defineProps({family : Object})

// console.log(child)
</script>

<style scoped>
#parent {
  background-color: #eee;
  text-align: center;
  border: 1px solid black;
  margin: 15px;
  padding: 3px;
}
</style>