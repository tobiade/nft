from scripts.helpers import (
    fund_with_link,
    get_account,
    OPENSEA_URL,
    get_contract,
    get_from_networks_config,
)
from brownie import AdvancedCollectible, config, network

sample_token_uri = "https://ipfs.io/ipfs/Qmd9MCGtdVz2miNumBHDbvj8bigSgTwnr4SbyH6DNnpWdt?filename=0-PUG.json"


def deploy_and_create():
    account = get_account()
    advanced_collectible = AdvancedCollectible.deploy(
        get_contract("vrf_coordinator"),
        get_contract("link_token"),
        get_from_networks_config("keyhash"),
        get_from_networks_config("fee"),
        {"from": account},
        publish_source=config["networks"][network.show_active()].get("verify", False),
    )
    fund_with_link(advanced_collectible)

    creating_tx = advanced_collectible.createCollectible({"from": account})
    creating_tx.wait(1)
    print("New token has been created!")
    return advanced_collectible, creating_tx


def main():
    deploy_and_create()
