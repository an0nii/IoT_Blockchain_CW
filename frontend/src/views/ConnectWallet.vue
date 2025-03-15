<template>
  <div class="max-w-md mx-auto mt-8 p-6 bg-white rounded shadow">
    <h2 class="text-2xl font-bold mb-4">Connect Your Wallet</h2>
    <ConnectWalletButton @wallet-connected="handleConnected" />
    <div v-if="walletAddress" class="mt-4">
      <p class="text-lg">Connected Wallet: {{ walletAddress }}</p>
    </div>
  </div>
</template>
<script>
import { ConnectWalletButton } from "vue-connect-wallet";
export default {
  name: "ConnectWalletPage",
  components: {
    ConnectWalletButton,
  },
  data() {
    return {
      walletAddress: "",
    };
  },
  methods: {
    handleConnected(address) {
      this.walletAddress = address;
      console.log("Wallet connected:", address);
    },
  },
};
</script>
<style scoped>
</style>