<template>
  <div class="max-w-md mx-auto mt-8 p-6 bg-white rounded shadow">
    <h2 class="text-2xl font-semibold mb-4">Generate Product QR Code</h2>
    <form @submit.prevent="handleGenerate">
      <div class="mb-4">
        <label class="block text-gray-700">Sender Address</label>
        <input
          type="text"
          v-model="senderAddress"
          class="w-full px-3 py-2 border rounded"
          placeholder="Enter sender address"
          required
        />
      </div>
      <div class="mb-4">
        <label class="block text-gray-700">Reciver Address</label>
        <input
          type="text"
          v-model="reciverAddress"
          class="w-full px-3 py-2 border rounded"
          placeholder="Enter reciver address"
          required
        />
      </div>
      <div class="mb-4">
        <label class="block text-gray-700">Host Address</label>
        <input
          type="text"
          v-model="hostAddress"
          class="w-full px-3 py-2 border rounded"
          placeholder="Enter host address"
          required
        />
      </div>
      <div class="flex justify-between items-center">
        <button
          type="submit"
          class="bg-green-500 text-white px-4 py-2 rounded hover:bg-green-600"
        >
          Generate QR
        </button>
        <router-link to="/">
          <button
            type="button"
            class="bg-gray-500 text-white px-4 py-2 rounded hover:bg-gray-600"
          >
            Back
          </button>
        </router-link>
      </div>
    </form>
    <div v-if="qrCodeUrl" class="mt-6">
      <h3 class="text-xl font-semibold mb-2">Your QR Code:</h3>
      <img :src="qrCodeUrl" alt="QR Code" class="border p-2" />
      <a
        :href="qrCodeUrl"
        download="qrcode.png"
        class="mt-4 inline-block bg-blue-500 text-white px-4 py-2 rounded hover:bg-blue-600"
      >
        Download QR Code
      </a>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
export default {
  name: 'GenerateQRCode',
  data() {
    return {
      senderAddress: '',
      reciverAddress: '',
      hostAddress: '',
      qrCodeUrl: ''
    }
  },
  methods: {
    getNextId() {
      let lastId = localStorage.getItem('lastId')
      if (!lastId) {
        lastId = 0
      }
      const nextId = parseInt(lastId) + 1
      localStorage.setItem('lastId', nextId)
      return nextId
    },
    async handleGenerate() {
      try {
        const productId = this.getNextId()
        const typedData = `${productId}||${this.senderAddress}||${this.reciverAddress}||${this.hostAddress}`
        const response = await axios.post('http://localhost:3000/api/generate_qr', { data: typedData })
        this.qrCodtUrl = response.data.qrCode
      } catch (error) {
        console.error('QR Code generation failed:', error)
      }
    },
  },
}
</script>

<style scoped>
</style>