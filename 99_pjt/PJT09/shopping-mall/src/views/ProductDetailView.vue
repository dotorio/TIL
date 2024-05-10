<template>
  <div v-if="product.id">
    <h1>상품명: {{ product.title }}</h1>
    <img :src="product.image" alt="" width="200">
    <p>가격: {{ product.price }}</p>
    <p>카테고리: {{ product.category }}</p>
    <button @click="useCartStore.addCart(product)">장바구니에 추가</button>
  </div>
  <p v-else>Loading 중...</p>
</template>

<script setup>
import { useRoute } from 'vue-router';
import {ref} from 'vue';
import axios from 'axios';
import {useCartStore} from '@/stores/counter'
// 1. product Id를 params로부터 가져오기
const route = useRoute()
const productId = route.params.product_id
const cartStore = useCartStore()

// 2. product Id를 이용해서 데이터 가져오기
const product = ref([])
axios({
  method: 'get',
  url: `https://fakestoreapi.com/products/${productId}`
})
.then((response) => {
  // console.log(reponse)
  product.value = response.data
})
.catch((error) => {
  console.log(error)
})

// 3. 화면에 그려준다.
</script>

<style scoped>

</style>