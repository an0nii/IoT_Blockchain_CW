<template>
  <div class="max-w-md mx-auto mt-8 p-6 bg-white rounded shadow">
    <h2 class="text-2xl font-semibold mb-4">Add device</h2>
      <form @submit.prevent="handleSubmit">
      <div class="mb-4">
        <label class="block text-gray-700">Device name</label>
        <input
          type="text"
          v-model="device.name"
          class="w-full px-3 py-2 border rounded"
          placeholder="Type a device name"
          required
        />
      </div>

      <div class="mb-4">
        <label class="block text-gray-700">Device type</label>
        <select
          v-model="device.type"
          class="w-full px-3 py-2 border rounded"
          required
        >
          <option value="" disabled selected>Select device type</option>
          <option value="Sender">Sender</option>
          <option value="Recipient">Recipient</option>
        </select>
      </div>

      <div class="mb-4">
        <label class="block text-gray-700">Device address</label>
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
            Back
          </button>
        </router-link>
      </div>
    </form>
  </div>
</template>

<script>
export default {
  name: 'AddDevice',
  data() {
    return {
      device: {
        name: '',
        type: '',
        address: '', 
        description: '',
      },
    }
  },
  methods: {
    handleSubmit() {
      console.log('Device added:', this.device)
      
      // TODO
      this.device.name = ''
      this.device.type = ''
      this.device.address = ''
      this.device.description = ''
    },
  },
}
</script>

<style scoped>
</style>