<template>
  <div class="max-w-2xl mx-auto mt-8 p-6 bg-white rounded shadow">
    <h2 class="text-2xl font-semibold mb-6">Product Details</h2>
    
    <div class="mb-6">
      <p class="mb-2"><strong>ID:</strong> {{ product.id }}</p>
      <p class="mb-2"><strong>Sender:</strong> {{ product.sender }}</p>
      <p class="mb-2"><strong>Time:</strong> {{ product.time }}</p>
      <p class="mb-2"><strong>Destination:</strong> {{ product.destination }}</p>
      <p class="mb-2"><strong>Sent:</strong> {{ product.sent ? 'Yes' : 'No' }}</p>
      <p class="mb-2"><strong>Received:</strong> {{ product.received ? 'Yes' : 'No' }}</p>
      <p class="mb-2"><strong>Description:</strong> {{ product.description }}</p>
    </div>

    <router-link to="/products">
      <button class="mt-6 bg-gray-500 text-white px-4 py-2 rounded hover:bg-gray-600">
        Back to Products
      </button>
    </router-link>
  </div>
</template>

<script>
export default {
  name: 'ProductDetails',
  props: ['id'],
  data() {
    return {
      product: {
        id: this.id,
        sender: 'Moscow',
        time: '0 hour(s)',
        destination: 'Minsk',
        sent: false,
        received: false,
        description: 'product 1',
      },
    }
  },
}
</script>

<style scoped>
</style>