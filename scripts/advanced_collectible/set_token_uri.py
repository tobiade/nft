from brownie import network, AdvancedCollectible
from scripts.helpers import OPENSEA_URL, get_account, get_breed

dog_metadata_dict = {
    "PUG": "https://ipfs.io/ipfs/Qmd9MCGtdVz2miNumBHDbvj8bigSgTwnr4SbyH6DNnpWdt?filename=0-PUG.json",
    "SHIBA_INU": "https://ipfs.io/ipfs/QmdryoExpgEQQQgJPoruwGJyZmz6SqV4FRTX1i73CT3iXn?filename=1-SHIBA_INU.json",
    "ST_BERNARD": "https://ipfs.io/ipfs/QmW4qPbedTL7DS3AgdzMnrw7YKYZB2miLAywJBNZe97kTz?filename=2-ST_BERNARD.json",
}


def main():
    print(f"Working on {network.show_active()}")
    advanced_collectible = AdvancedCollectible[-1]
    number_of_tokens = advanced_collectible.tokenCounter()
    print(f"You have created {number_of_tokens} collectibles!")
    for tokenId in range(number_of_tokens):
        breed = get_breed(advanced_collectible.tokenIdToBreed(tokenId))
        if not advanced_collectible.tokenURI(tokenId).startswith("https://"):
            print(f"Setting token URI of {tokenId}")
            set_tokenURI(tokenId, advanced_collectible, dog_metadata_dict[breed])


def set_tokenURI(token_id, nft_contract, tokenURI):
    account = get_account()
    tx = nft_contract.setTokenURI(token_id, tokenURI, {"from": account})
    tx.wait(1)
    print(
        f"Awesome! You can view nft at {OPENSEA_URL.format(nft_contract.address, token_id)}"
    )
