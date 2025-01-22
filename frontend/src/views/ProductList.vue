<template>
  <div class="max-w-4xl mx-auto mt-8 p-6 bg-white rounded shadow">
    <div class="flex justify-between items-center mb-4">
      <h2 class="text-2xl font-semibold">Products list</h2>
      <router-link to="/">
        <button class="bg-gray-500 text-white px-4 py-2 rounded hover:bg-gray-600">
          Back
        </button>
      </router-link>
    </div>
    <table class="min-w-full bg-white">
      <thead>
      <tr>
        <th class="py-2 px-4 border-b">ID</th>
        <th class="py-2 px-4 border-b">Sender</th>
        <th class="py-2 px-4 border-b">Time</th>
        <th class="py-2 px-4 border-b">Destination</th>
        <th class="py-2 px-4 border-b">Sent</th>
        <th class="py-2 px-4 border-b">Received</th>
        <th class="py-2 px-4 border-b">Details</th>
      </tr>
      </thead>
      <tbody>
        <tr v-for="(product, index) in products" :key="index">
          <td class="py-2 px-4 border-b">{{ product.id }}</td>
          <td class="py-2 px-4 border-b">{{ product.sender }}</td>
          <td class="py-2 px-4 border-b">{{ product.time }}</td>
          <td class="py-2 px-4 border-b">{{ product.destination }}</td>
          <td class="py-2 px-4 border-b">{{ product.sent ? 'Yes' : 'No' }}</td>
          <td class="py-2 px-4 border-b">{{ product.received ? 'Yes' : 'No' }}</td>
          <td class="py-2 px-4 border-b">
            <router-link :to="`/product/${product.id}`">
              <button class="bg-blue-500 text-white px-3 py-1 rounded hover:bg-blue-600">
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
  name: 'ProductList',
  data() {
    return {
      products: [
        // Examples
        {
          id: 1,
          sender: 'Moscow',
          time: '0 hour(s)',
          destination: 'Minsk',
          sent: false,
          received: false,
          description: 'P 1',
        },
        {
          id: 2,
          sender: 'Moscow',
          time: '2 hour(s)',
          destination: 'Minsk',
          sent: true,
          received: false,
          description: 'P 2',
        },
      ],
    }
  },
}
</script>

<style scoped>
</style>