from brownie import AdvancedCollectible
from scripts.helpers import fund_with_link, get_account
from web3 import Web3


def create_collectible():
    account = get_account()
    advanced_collectible = AdvancedCollectible[-1]
    fund_with_link(advanced_collectible, amount=Web3.toWei(0.1, "ether"))
    creation_tx = advanced_collectible.createCollectible({"from": account})
    creation_tx.wait(1)
    print("Collectible created!")


def main():
    create_collectible()
