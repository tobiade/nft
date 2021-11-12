from brownie import AdvancedCollectible, network
from scripts.helpers import get_breed
from pathlib import Path
from metadata.sample_metadata import metadata_template
import requests
import json

IPFS_URL = "http://127.0.0.1:5001"
ENDPOINT = "/api/v0/add"


def create_metadata():
    advanced_collectible = AdvancedCollectible[-1]
    number_of_tokens = advanced_collectible.tokenCounter()
    print(f"You have created {number_of_tokens} collectibles!")
    for token_id in range(number_of_tokens):
        breed = get_breed(advanced_collectible.tokenIdToBreed(token_id))
        metadata_file_name = (
            f"./metadata/{network.show_active()}/{token_id}-{breed}.json"
        )
        collectible_metadata = metadata_template
        if Path(metadata_file_name).exists():
            print(f"{metadata_file_name} already exists! Delete it to overwrite")
        else:
            print(f"Creating metadata file: {metadata_file_name}")
            collectible_metadata["name"] = breed
            collectible_metadata["description"] = f"An adorable {breed} pup!"
            image_path = "./img/" + breed.lower().replace("_", "-") + ".png"
            image_uri = upload_to_ipfs(image_path)
            print(image_uri)
            collectible_metadata["image"] = image_uri
            with open(metadata_file_name, "w") as file:
                json.dump(collectible_metadata, file)
            metadata_uri = upload_to_ipfs(metadata_file_name)
            print(metadata_uri)


def upload_to_ipfs(filepath):
    with Path(filepath).open("rb") as fp:
        image_binary = fp.read()
        response = requests.post(IPFS_URL + ENDPOINT, files={"file": image_binary})
        ipfs_hash = response.json()["Hash"]
        filename = filepath.split("/")[-1]
        uri = f"https://ipfs.io/ipfs/{ipfs_hash}?filename={filename}"
        return uri


def main():
    create_metadata()
