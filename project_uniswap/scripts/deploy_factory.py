from brownie import UniswapV2FactoryMock, accounts, network, config

def main():
    if network.show_active() == "development":
        deploy_mocks()
    else:
        print("Only deploying to the development network.")

def deploy_mocks():
    deployer = accounts[0]

    # Địa chỉ Uniswap V2 Factory Mock
    uniswap_v2_factory_address = "0x5C69bEe701ef814a2B6a3EDD4B1652CB9cc5aA6f"

    factory = UniswapV2FactoryMock.deploy(uniswap_v2_factory_address, {"from": deployer})

    print("Factory deployed at:", factory.address)
