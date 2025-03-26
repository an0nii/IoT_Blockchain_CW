<template>
  <div class="max-w-2xl mx-auto mt-8 p-6 bg-white rounded shadow">
    <h2 class="text-2xl font-semibold mb-6">Device Details</h2>
    <div v-if="device">
      <p class="mb-4"><strong>Device Name:</strong> {{ device.name }}</p>
      <p class="mb-4"><strong>Device Type:</strong> {{ device.type }}</p>
      <p class="mb-4"><strong>Device Address:</strong> {{ device.address }}</p>
      <p class="mb-4" v-if="device.description">
        <strong>Description:</strong> {{ device.description }}
      </p>
    </div>
    <div v-else class="text-gray-600">
      Device Not Found.
    </div>
    <router-link to="/">
      <button class="mt-6 bg-gray-500 text-white px-4 py-2 rounded hover:bg-gray-600">
        Home Page
      </button>
    </router-link>
    <div v-if="error" class="mt-4 p-2 bg-red-200 text-red-800 rounded">
      {{ error }}
    </div>
  </div>
</template>

<script>
export default {
  name: "DeviceDetails",
  props: ['id'],
  data() {
    return {
      device: null,
      error: ''
    }
  },
  created() {
    try {
      const devices = JSON.parse(localStorage.getItem('devices') || '[]');
      this.device = devices.find(d => String(d.id) === String(this.id));
      if (!this.device) {
        this.error = "Device not found.";
      }
    } catch (e) {
      this.error = e.message || "Error loading device details.";
    }
  }
}
</script>

<style scoped>
</style>