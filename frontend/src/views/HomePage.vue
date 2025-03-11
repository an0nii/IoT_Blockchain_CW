<template>
  <div class="max-w-4xl mx-auto mt-8 p-6 bg-white rounded shadow">
    <div class="flex justify-between items-center mb-4">
      <h2 class="text-2xl font-semibold">Devices list</h2>
      <router-link to="/generate-qr">
        <button class="bg-blue-500 text-white px-4 py-2 rounded hover:bg-blue-600">
          Generate QR Code For Product
        </button>
      </router-link>
    </div>
    <table class="min-w-full bg-white">
      <thead>
        <tr>
          <th class="py-2 px-4 border-b">Name</th>
          <th class="py-2 px-4 border-b">Type</th>
          <th class="py-2 px-4 border-b">Description</th>
          <th class="py-2 px-4 border-b">Details</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="(device, index) in devices" :key="index">
          <td class="py-2 px-4 border-b">{{ device.name }}</td>
          <td class="py-2 px-4 border-b">{{ device.type }}</td>
          <td class="py-2 px-4 border-b">{{ device.description }}</td>
          <td class="py-2 px-4 border-b">
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

<script>
export default {
  name: 'HomePage',
  data() {
    return {
      devices: [
        { id: 1, name: 'IoTSender1', type: 'Sender', description: 'Device in Moscow' },
        { id: 2, name: 'IoTReceiver1', type: 'Recipient', description: 'Device in Minsk' },
      ],
    }
  },
}
</script>

<style scoped>
</style>