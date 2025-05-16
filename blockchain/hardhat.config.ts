import { HardhatUserConfig } from "hardhat/config";
import "@nomicfoundation/hardhat-toolbox";
import "hardhat-deploy";
import dotenv from 'dotenv'
dotenv.config()

const config: HardhatUserConfig = {
  solidity: "0.8.28",
  networks: {
    binance_testnet: {
      url: `https://bsc-prebsc-dataseed.bnbchain.org/`,
      chainId: 97,
      accounts: [`0x${process.env.METAMASK_PRIVATE_KEY}`]
    },
    hardhat: {}
  },
  namedAccounts: {
    deployer: 0,
  },
};

export default config;