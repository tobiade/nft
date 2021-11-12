from brownie import network, AdvancedCollectible
from scripts.helpers import LOCAL_BLOCKHAIN_ENVIRONMENTS, get_account, get_contract
import pytest
import time
from scripts.advanced_collectible.deploy_and_create import deploy_and_create


def test_can_create_simple_collectible_integration():
    if network.show_active() in LOCAL_BLOCKHAIN_ENVIRONMENTS:
        pytest.skip("Only for integration testing")
    advanced_collectible, creation_tx = deploy_and_create()
    time.sleep(240)

    assert advanced_collectible.tokenCounter() == 1
