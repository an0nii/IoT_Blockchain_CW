<template>
  <div class="max-w-6xl mx-auto mt-8 p-6 bg-white rounded shadow">
    <div class="flex justify-between items-center mb-4">
      <h2 class="text-2xl font-semibold">Products List</h2>
      <router-link to="/">
        <button class="bg-gray-500 text-white px-4 py-2 rounded hover:bg-gray-600">
          Home Page
        </button>
      </router-link>
    </div>
    <div v-if="error" class="mb-4 p-2 bg-red-200 text-red-800 rounded">
      {{ error }}
    </div>
    <div class="w-full">
      <table class="min-w-full bg-white table-fixed">
        <thead>
          <tr>
            <th class="w-1/5 py-2 px-4 border text-center">ID</th>
            <th class="w-1/5 py-2 px-4 border text-center">Sent</th>
            <th class="w-1/5 py-2 px-4 border text-center">Received</th>
            <th class="w-1/5 py-2 px-4 border text-center">Voided</th>
            <th class="w-1/5 py-2 px-4 border text-center">Details</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="(product, index) in products" :key="index">
            <td class="w-1/5 py-2 px-4 border text-center">{{ product.id }}</td>
            <td class="w-1/5 py-2 px-4 border text-center">{{ product.sent ? 'Yes' : 'No' }}</td>
            <td class="w-1/5 py-2 px-4 border text-center">{{ product.received ? 'Yes' : 'No' }}</td>
            <td class="w-1/5 py-2 px-4 border text-center">{{ product.voided ? 'Yes' : 'No' }}</td>
            <td class="w-1/5 py-2 px-4 border text-center">
              <router-link :to="`/product/${product.id}`">
                <button class="bg-blue-500 text-white px-3 py-1 rounded hover:bg-blue-600">
                  View
                </button>
              </router-link>
            </td>
          </tr>
        </tbody>
      </table>
    </div>
    <div v-if="loading" class="mt-4 text-gray-600">
      Loading...
    </div>
  </div>
</template>

<script>
import { ethers, BrowserProvider } from 'ethers'
import IOTContractMonitoring from '../../IOTContractMonitoring.json'

export default {
  name: 'ProductList',
  data() {
    return {
      products: [],
      loading: false,
      error: '',
      intervalId: null
    }
  },
  methods: {
    async fetchProducts() {
      this.loading = true
      this.error = ''
      try {
        if (!window.ethereum) {
          throw new Error('MetaMask not installed')
        }
        const provider = new BrowserProvider(window.ethereum)
        const contract = new ethers.Contract(IOTContractMonitoring.address, IOTContractMonitoring.abi, provider)
        const currentId = parseInt(localStorage.getItem("currentId"), 10) || 1
        let products = []
        for (let i = 1; i < currentId; i++) {
          try {
            const labelData = await contract.labels(i)
            products.push({
              id: labelData.id.toString(),
              sent: labelData.sent,
              received: labelData.received,
              voided: labelData.voided,
              sender: labelData.sender,
              receiver: labelData.receiver
            })
          } catch (err) {
            console.error("Failed to fetch label with id", i, err)
          }
        }
        this.products = products
        sessionStorage.setItem("cachedProducts", JSON.stringify(products))
      } catch (e) {
        this.error = e.message || "Failed to fetch products."
      } finally {
        this.loading = false
      }
    }
  },
  mounted() {
    this.fetchProducts()
    this.intervalId = setInterval(() => {
      this.fetchProducts()
    }, 5000)
    const cached = sessionStorage.getItem("cachedProducts")
    if (cached) {
      this.products = JSON.parse(cached)
    }
  },
  beforeUnmount() {
    if (this.intervalId) {
      clearInterval(this.intervalId)
    }
  }
}
</script>

<style scoped>
table {
  table-layout: fixed;
  border-collapse: collapse;
}
th, td {
  padding: 0.5rem 1rem;
  border: 1px solid #d1d5db;
  text-align: center;
}
</style>