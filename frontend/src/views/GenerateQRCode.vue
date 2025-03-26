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
        <label class="block text-gray-700">Receiver Address</label>
        <input
          type="text"
          v-model="reciverAddress"
          class="w-full px-3 py-2 border rounded"
          placeholder="Enter receiver address"
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
          Home Page
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
    <div v-if="walletAddress" class="mt-6">
      <p class="text-lg">Using Wallet: {{ walletAddress }}</p>
      <button
        @click="sendToContract"
        class="mt-4 inline-block bg-indigo-500 text-white px-4 py-2 rounded hover:bg-indigo-600"
      >
        Send To Contract
      </button>
    </div>
    <div v-if="contractError" class="mt-4 p-2 bg-red-200 text-red-800 rounded">
      {{ contractError }}
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import { ethers, BrowserProvider } from 'ethers'
import IOTContractMonitoring from '../../IOTContractMonitoring.json'
export default {
  name: 'GenerateQRCode',
  data() {
    return {
      senderAddress: '',
      reciverAddress: '',
      qrCodeUrl: '',
      walletAddress: '',
      currentProductId: null,
      pendingProductId: null,
      contractError: ''
    }
  },
  created() {
    const storedWallet = localStorage.getItem("walletAddress")
    if (storedWallet) {
      this.walletAddress = storedWallet
    }
    if (!localStorage.getItem("currentId")) {
      localStorage.setItem("currentId", 1)
    }
  },
  methods: {
    getCurrentId() {
      let currentId = localStorage.getItem("currentId")
      return parseInt(currentId, 10)
    },
    incrementCurrentId() {
      let currentId = this.getCurrentId()
      currentId++
      localStorage.setItem("currentId", currentId)
      return currentId
    },
    async handleGenerate() {
      try {
        const productId = this.getCurrentId()
        this.pendingProductId = productId
        const typedData = `${productId}||${this.senderAddress}||${this.reciverAddress}`
        const response = await axios.post('http://localhost:3000/api/generate_qr', { data: typedData })
        this.qrCodeUrl = response.data.qrCode
      } catch (error) {
        console.error('QR Code generation failed:', error)
      }
    },
    async sendToContract() {
      try {
        if (!window.ethereum) {
          throw new Error('MetaMask not installed')
        }
        this.contractError = ''
        console.log("Sending transaction with parameters:", {
          productId: this.pendingProductId,
          sender: this.senderAddress,
          receiver: this.reciverAddress
        })
        const provider = new BrowserProvider(window.ethereum)
        const signer = await provider.getSigner()
        const contractAddress = IOTContractMonitoring.address
        const contractABI = IOTContractMonitoring.abi
        const contract = new ethers.Contract(contractAddress, contractABI, signer)
        const tx = await contract.createLabel(this.pendingProductId, this.senderAddress, this.reciverAddress)
        console.log("Transaction hash:", tx.hash)
        await tx.wait()
        console.log("Transaction confirmed")
        this.currentProductId = this.pendingProductId
        this.incrementCurrentId()
      } catch (error) {
        console.error("Transaction failed:", error)
        if (error.message.includes("Sender not authorized")) {
          this.contractError = "Transaction failed: sender is not authorized to perform this operation."
        } else {
          this.contractError = error.message
        }
      }
    }
  }
}
</script>

<style scoped>
</style>