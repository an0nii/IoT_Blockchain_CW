import { HardhatRuntimeEnvironment } from "hardhat/types";
import { DeployFunction } from "hardhat-deploy/types";

const func: DeployFunction = async function (
    hre: HardhatRuntimeEnvironment
) {
    const { getNamedAccounts, deployments } = hre;
    const { deploy, log } = deployments;
    const { deployer } = await getNamedAccounts();

    log("Deploying Token...")

    const token = await deploy("IOTContractMonitoring", {
        from: deployer,
        args: [deployer],
        log: true,
    });

    log(`Deployed token to address ${token.address}`)
};

export default func;
func.tags = ["iottoken"];