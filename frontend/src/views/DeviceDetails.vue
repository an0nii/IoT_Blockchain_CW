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
      <div class="mt-6">
        <h3 class="text-xl font-semibold mb-4">Related Products</h3>
        <div v-if="loadingProducts" class="text-gray-600">
          Loading related products...
        </div>
        <div v-else>
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
              <tr v-for="(product, index) in relatedProducts" :key="index">
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
              <tr v-if="relatedProducts.length === 0">
                <td colspan="5" class="py-2 px-4 border text-center text-gray-600">
                  No related products found.
                </td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>

    </div>
    <div v-else class="text-gray-600">
      Device not found.
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
      error: '',
      relatedProducts: [],
      loadingProducts: false,
      errorProducts: ''
    }
  },
  created() {
    try {
      const devices = JSON.parse(localStorage.getItem('devices') || '[]');
      this.device = devices.find(d => String(d.id) === String(this.id));
      if (!this.device) {
        this.error = "Device not found.";
      } else {
        this.fetchRelatedProducts();
      }
    } catch (e) {
      this.error = e.message || "Error loading device details.";
    }
  },
  methods: {
  fetchRelatedProducts() {
    this.loadingProducts = true;
    try {
      let products = [];
      if (sessionStorage.getItem("cachedProducts")) {
        products = JSON.parse(sessionStorage.getItem("cachedProducts"));
      }
      const deviceAddress = this.device.address.trim().toLowerCase();
      this.relatedProducts = products.filter(product => {
        const sender = product.sender.trim().toLowerCase();
        const receiver = product.receiver.trim().toLowerCase();
        return sender === deviceAddress || receiver === deviceAddress;
      });
    } catch (e) {
      this.errorProducts = e.message || "Failed to load related products.";
    } finally {
      this.loadingProducts = false;
    }
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