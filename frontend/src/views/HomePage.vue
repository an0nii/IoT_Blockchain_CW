<template>
  <div class="max-w-4xl mx-auto mt-8 p-6 bg-white rounded shadow">
    <div class="flex justify-between items-center mb-4">
      <router-link to="/generate-qr">
        <button class="bg-blue-500 text-white px-4 py-2 rounded hover:bg-blue-600">
          Generate QR Code For Product
        </button>
      </router-link>
      <button @click="connectWallet" class="bg-indigo-500 text-white px-4 py-2 rounded hover:bg-indigo-600">
        <span v-if="walletAddress">Connected</span>
        <span v-else>Connect Wallet</span>
      </button>
    </div>
    <div v-if="walletAddress" class="mb-4">
      <p class="text-lg text-green-600">Wallet connected: {{ walletAddress }}</p>
    </div>
    <table class="min-w-full bg-white table-fixed">
      <thead>
        <tr>
          <th class="w-1/3 py-2 px-4 border text-center">Name</th>
          <th class="w-1/3 py-2 px-4 border text-center">Type</th>
          <th class="w-1/3 py-2 px-4 border text-center">Details</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="device in devices" :key="device.id">
          <td class="w-1/3 py-2 px-4 border text-center">{{ device.name }}</td>
          <td class="w-1/3 py-2 px-4 border text-center">{{ device.type }}</td>
          <td class="w-1/3 py-2 px-4 border text-center">
            <router-link :to="`/device/${device.id}`">
              <button class="bg-green-500 text-white px-3 py-1 rounded hover:bg-green-600">
                View
              </button>
            </router-link>
          </td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import axios from 'axios'
import { useMetaMaskWallet } from "vue-connect-wallet"
import "vue-connect-wallet/dist/style.css"

const walletAddress = ref("")
const wallet = useMetaMaskWallet()

const connectWallet = async () => {
  const result = await wallet.connect()
  if (Array.isArray(result)) {
    walletAddress.value = result[0]
    localStorage.setItem("walletAddress", result[0])
    console.log("Wallet connected:", result[0])
  } else {
    console.error("Error connecting wallet:", result)
  }
}

wallet.onAccountsChanged((accounts) => {
  if (accounts && accounts.length > 0) {
    walletAddress.value = accounts[0]
    localStorage.setItem("walletAddress", accounts[0])
    console.log("Wallet account changed:", accounts[0])
  } else {
    walletAddress.value = ""
    localStorage.removeItem("walletAddress")
  }
})

const devices = ref([])

const fetchDevices = async () => {
  try {
    const res = await axios.get('http://localhost:3000/api/devices')
    devices.value = res.data.devices
  } catch (e) {
    console.error("Error fetching devices: ", e)
  }
}

const syncDevices = async () => {
  try {
    const storedDevices = localStorage.getItem("devices")
    if (storedDevices) {
      const localDevices = JSON.parse(storedDevices)
      for (const device of localDevices) {
        await axios.post('http://localhost:3000/api/devices', device)
      }
      localStorage.removeItem("devices")
    }
  } catch (e) {
    console.error("Error syncing devices: ", e)
  }
}

onMounted(async () => {
  const storedWallet = localStorage.getItem("walletAddress")
  if (storedWallet) {
    walletAddress.value = storedWallet
  }
  await syncDevices()
  await fetchDevices()
})
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