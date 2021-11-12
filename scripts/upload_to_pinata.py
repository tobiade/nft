import os

PINATA_BASE_URL = "https://api.pinata.cloud/"
ENDPOINT = "pinning/pinFileToIPFS"

filepath = "./img/pug.png"
filename = filepath.split("/")[-1]
headers = {
    "pinata_api_key": os.getenv("PINATA_API_KEY"),
    "pinata_secret_api_key": os.getenv("PINATA_API_SECRET"),
}
