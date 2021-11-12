from brownie import network, AdvancedCollectible
from scripts.helpers import LOCAL_BLOCKHAIN_ENVIRONMENTS, get_account, get_contract
import pytest
from scripts.advanced_collectible.deploy_and_create import deploy_and_create


def test_can_create_simple_collectible():
    if network.show_active() not in LOCAL_BLOCKHAIN_ENVIRONMENTS:
        pytest.skip()
    advanced_collectible, creation_tx = deploy_and_create()
    requestId = creation_tx.events["requestedCollectable"]["requestId"]
    # random number callback
    random_number = 777
    get_contract("vrf_coordinator").callBackWithRandomness(
        requestId, random_number, advanced_collectible.address, {"from": get_account()}
    )
    assert advanced_collectible.tokenCounter() == 1
    assert advanced_collectible.tokenIdToBreed(0) == random_number % 3
