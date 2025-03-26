<template>
  <div class="max-w-md mx-auto mt-8 p-6 bg-white rounded shadow">
    <h2 class="text-2xl font-semibold mb-4">Add Device</h2>
    <form @submit.prevent="handleSubmit">
      <div class="mb-4">
        <label class="block text-gray-700">Device Name</label>
        <input
          type="text"
          v-model="device.name"
          class="w-full px-3 py-2 border rounded"
          placeholder="Type a device name"
          required
        />
      </div>

      <div class="mb-4">
        <label class="block text-gray-700">Device Type</label>
        <select
          v-model="device.type"
          class="w-full px-3 py-2 border rounded"
          required
        >
          <option value="" disabled selected>Select Device Type</option>
          <option value="Sender">Sender</option>
          <option value="Receiver">Receiver</option>
        </select>
      </div>

      <div class="mb-4">
        <label class="block text-gray-700">Device Adress</label>
        <input
          type="text"
          v-model="device.address"
          class="w-full px-3 py-2 border rounded"
          placeholder="Enter device address"
          required
        />
      </div>

      <div class="mb-4">
        <label class="block text-gray-700">Description</label>
        <textarea
          v-model="device.description"
          class="w-full px-3 py-2 border rounded"
          placeholder="Type a description"
          rows="4"
        ></textarea>
      </div>

      <div class="flex justify-between items-center">
        <button
          type="submit"
          class="bg-green-500 text-white px-4 py-2 rounded hover:bg-green-600"
        >
          Save
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
    <div v-if="deviceError" class="mt-4 p-2 bg-red-200 text-red-800 rounded">
      {{ deviceError }}
    </div>
  </div>
</template>

<script>
import { ethers, BrowserProvider } from 'ethers'
import IOTContractMonitoring from '../../IOTContractMonitoring.json'
export default {
  name: 'AddDevice',
  data() {
    return {
      device: {
        name: '',
        type: '',
        address: '',
        description: ''
      },
      deviceError: '',
    }
  },
  methods: {
    async handleSubmit() {
      try {
        const _account = this.device.address
        const _asSender = this.device.type === 'Sender'
        const _asReceiver = this.device.type === 'Receiver'
        const _status = true
        if (!window.ethereum) {
          throw new Error('MetaMask not installed')
        }
        const provider = new BrowserProvider(window.ethereum)
        const signer = await provider.getSigner()
        const contract = new ethers.Contract(IOTContractMonitoring.address, IOTContractMonitoring.abi, signer)
        const tx = await contract.setIoTAuthorization(_account, _asSender, _asReceiver, _status)
        console.log("setIoTAuthorization transaction hash:", tx.hash)
        await tx.wait()
        console.log("setIoTAuthorization transaction confirmed")
        let devices = []
        const storedDevices = localStorage.getItem('devices')
        if (storedDevices) {
          devices = JSON.parse(storedDevices)
        }
        const newDevice = { ...this.device, id: Date.now() }
        devices.push(newDevice)
        localStorage.setItem('devices', JSON.stringify(devices))
        console.log('Device added:', newDevice)
        this.device.name = ''
        this.device.type = ''
        this.device.address = ''
        this.device.description = ''        
        this.$router.push('/')
      } catch (error) {
        console.error('Error adding device:', error)
        this.deviceError = error.message
      }
    },
  },
}
</script>

<style scoped>
</style>