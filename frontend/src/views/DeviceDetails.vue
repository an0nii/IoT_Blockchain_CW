<template>
  <div class="max-w-2xl mx-auto mt-8 p-6 bg-white rounded shadow">
    <h2 class="text-2xl font-semibold mb-6">Device details</h2>

    <div>
      <h3 class="text-xl font-semibold mb-4">Related products</h3>
      <ul class="list-disc list-inside">
        <li v-for="(product, index) in relatedProducts" :key="index">
          <router-link :to="`/products`" class="text-blue-500 hover:underline">
            Product ID: {{ product.id }}
          </router-link>
          - {{ product.description }}
        </li>
      </ul>
    </div>

    <router-link to="/">
      <button class="mt-6 bg-gray-500 text-white px-4 py-2 rounded hover:bg-gray-600">
        Back
      </button>
    </router-link>
  </div>
</template>

<script>
export default {
  name: 'DeviceDetails',
  props: ['id'],
  data() {
    return {
      relatedProducts: [
        // Examples
        {
          id: 1,
          description: 'product 1',
        },
        {
          id: 2,
          description: 'product 2',
        },
      ],
    }
  },
}
</script>

<style scoped>
</style>