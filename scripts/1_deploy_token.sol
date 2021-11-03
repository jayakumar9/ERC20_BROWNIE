# create this file under ERC20_BROWNIE/scripts-video time 3.solidity 1:02:49

from brownie import OurToken
from scripts.helpful_scripts import get_account
from web3 import web3


initial_supply=web3.toWei(1000,"ether")


def main():
    account=get_account()
    our_token=OurToken.deploy(initial_supply.{"from":account})
    print(our_token.name())
    
    
