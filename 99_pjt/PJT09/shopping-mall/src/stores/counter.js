import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'

export const useCartStore = defineStore('cart', () => {
  // store에 저장되는 변수 : state(상태)
  const products = ref([])
  const carts = ref([])

  const getProducts = function() {
    // axios.get(url)
    axios({
      method: 'get',
      url: 'https://fakestoreapi.com/products'
    })
    .then((response) => {
      // console.log(reponse)
      products.value = response.data
    })
    .catch((error) => {
      console.log(error)
    })
  }

  const addCart = function(product) {
    carts.value.push(product)
  }

  const deleteCart = function(productId) {
    const idx = carts.value.findIndex(cart => cart.id === productId)
    if (idx !== -1) {
      carts.value.splice(idx, 1)
    }
  }


  return { products, carts, getProducts }
})
