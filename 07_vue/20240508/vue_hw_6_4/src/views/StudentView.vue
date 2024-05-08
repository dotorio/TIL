<template>
  <div>
    <h3>학생 상세 정보 목록입니다.</h3>
    <p v-for="student in students" :key="student.name">
      <RouterLink :to="{ name:'StudentsDetail', params: {'name': student.name} }" class="student">
      {{ student.name }} 학생 정보 보기
      </RouterLink>
    </p>
  </div>
</template>

<script setup>
import { ref } from 'vue'
const students = ref([
  {name: '김하나'},
  {name: '김두리'},
  {name: '김서이'},
])
</script>



<style scoped>
.student {
  text-decoration: none;
  color: black;
}
</style>