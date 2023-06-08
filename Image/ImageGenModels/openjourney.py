import requests
import io
from PIL import Image
import json

def detect(test_string):
    with open('ApiCredidentials\huggingface_credidentials.json') as file:
        data = json.load(file)
    API_URL = "https://api-inference.huggingface.co/models/prompthero/openjourney"
    headers = {"Authorization": data["api_key"]}
   
    prompt = "beautiful landscape, high quality"

    n = test_string

    for i in range(0, n):
        def query(payload):
            response = requests.post(API_URL, headers=headers, json=payload)
            return response.content

        image_bytes = query({
            "inputs": prompt + " " + str(i),
        })

        # Save the image to folder
        with open("Image\ImageGenModels\genImages\GANimage" + str(i+1) + ".jpg", "wb") as file:
            file.write(image_bytes)

        # Open the image using PIL
        image = Image.open(io.BytesIO(image_bytes))
