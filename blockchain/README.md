# Smart-Contract-Part

## Tools
- Hardhat

## Install and init
```bash
npm install
```

## Testing
```bash
% npx hardhat test

  IOTContractMonitoring (complete)
    ✔ 1. should allow only authorized LabelCreator to create a label
    ✔ 2. should allow only owner to authorize roles
    ✔ 3. should allow only authorized IoTSender to mark as Sent
    ✔ 4. should allow only authorized IoTReceiver to mark as Received
    ✔ 5. should revert when trying to create label with invalid receiver
    ✔ 6. should revert if non-authorized user tries to execute restricted functions
    ✔ 7. should store labels correctly in the mapping
    ✔ 8. should initialize the contract with the correct owner
    ✔ 9. Should prevent replay attack on markAsReceived
    ✔ 10. Should not allow unauthorized sender to mark label as sent
    ✔ 11. Should not allow unauthorized sender to create label
    ✔ 12. Should prevent double voiding of label
    ✔ 13. should (de)authorize LabelCreators via setLabelCreatorAuthorization
    ✔ 14. should (de)authorize IoT roles with setIoTAuthorization
    ✔ 15. Only owner should be able to set device info

  15 passing (5s)
```

## Deploy
```bash
npx hardhat deploy --tags iottoken --network binance_testnet
```

## Verify
```bash
npx hardhat --network binance_testnet etherscan-verify --api-key {API_KEY}
```
