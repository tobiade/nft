from brownie import network
from scripts.helpers import LOCAL_BLOCKHAIN_ENVIRONMENTS, get_account
import pytest
from scripts.simple_collectible.deploy_and_create import deploy_and_create


def test_can_create_simple_collectible():
    if network.show_active() not in LOCAL_BLOCKHAIN_ENVIRONMENTS:
        pytest.skip()
    simple_collectible = deploy_and_create()
    assert simple_collectible.ownerOf(0) == get_account()
