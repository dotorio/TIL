<template>
  <div>
    <h2>User Profile</h2>
    <p>Username: {{ username }}</p>
    <hr>
    <RouterLink :to="{ name: 'user-profile'}">상세 프로필</RouterLink> |
    <RouterLink :to="{ name: 'user-posts'}">작성한 게시글</RouterLink> 
    <hr>
    <RouterView />
    
  </div>
</template>

<script setup>
import { RouterLink, RouterView } from 'vue-router'
import { ref } from 'vue'
import { useRoute } from 'vue-router'

const route = useRoute()
const username = ref(route.params.username)
</script>
