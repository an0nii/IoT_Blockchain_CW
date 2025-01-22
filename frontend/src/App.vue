<template>
  <div>
    <header class="bg-green-500 p-4 flex justify-between items-center">
      <h1 class="text-white text-lg">Supply chain control panel</h1>
      
      <div class="flex space-x-4">
        <router-link to="/add-device" v-if="showAddButton">
          <button class="bg-white text-green-500 px-4 py-2 rounded">Add device</button>
        </router-link>
        
        <router-link to="/products" v-if="showProductsButton">
          <button class="bg-white text-green-500 px-4 py-2 rounded">Products</button>
        </router-link>
      </div>
    </header>
    <main class="p-4">
      <router-view />
    </main>
  </div>
</template>

<script>
export default {
  name: 'App',
  computed: {
    showAddButton() {
      return this.$route.path !== '/add-device';
    },
    showProductsButton() {
      return this.$route.path !== '/products';
    }
  },
}
</script>

<style>
</style>