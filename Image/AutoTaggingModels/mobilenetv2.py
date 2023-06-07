from PIL import Image
from torchvision import transforms
import os
import torch

def detect(test_string):
    model = torch.hub.load('pytorch/vision:v0.10.0', 'mobilenet_v2', pretrained=True)
    model.eval()

    # Loop through every img in folder

    preprocess = transforms.Compose([
        transforms.Resize(256),
        transforms.CenterCrop(224),
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
    ])

    n = 0
    if (test_string == "smallImageSet"):
        n = 15
    elif (test_string == "mediumImageSet"):
        n = 60
    elif (test_string == "largeImageSet"):
        n = 120

    preds = []

    for i in range(1, n):
        input_image = Image.open("data\MLTaggingDatasets\imagenet1k\IMG" + str(i) + ".jpg")
        input_tensor = preprocess(input_image)

        # create a mini-batch as expected by the model
        input_batch = input_tensor.unsqueeze(0)

        # move the input and model to GPU for speed if available
        if torch.cuda.is_available():
            input_batch = input_batch.to('cuda')
            model.to('cuda')

        with torch.no_grad():
            output = model(input_batch)

        # Runs softmax to get normalized scores
        probabilities = torch.nn.functional.softmax(output[0], dim=0)
        
        # Read the categories
        with open("Image\AutoTaggingModels\imagenet_classes.txt", "r") as f:
            categories = [s.strip() for s in f.readlines()]

        # Show top categories per image
        top5_prob, top5_catid = torch.topk(probabilities, 5)
        
        temp = []
        for j in range(top5_prob.size(0)):
            temp.append(categories[top5_catid[j]])
        
        #print(str(i) + " Text Line: " + str(((lines[i-1].strip()).split(", "))))
        #print(str(i) + " ML Array: " + str(temp))
        #print("------------------------")

        preds.append(temp)
    return preds
