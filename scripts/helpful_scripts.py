# create this file under ERC20_BROWNIE/scripts  video 3.solidity time 1:02:49


from brownie import (accounts, network, config, MockV3Aggregator, VRFCoordinator,LinkToken,contract,interface,)
FORKED_LOCAL_ENVIRONMENTS=["mainnet-fork","mainnet-fork-dev"]
LOCAL_BLOCKCHAIN_ENVIRONMENTS=["development","ganache-local"]

def get_account(index=None,id=None):
    #accounts[0]
    #accounts.add("env")
    #accounts.load("id")
    if index:
        return accounts[index]
    if id:
        return accounts.load(id)
    if(
        network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENTS
        or network.show_active() in FORKED_LOCAL_ENVIRONMENTS
      ):  
        return accounts[0]
    return accounts.add(config["wallets"]["from_key"])

