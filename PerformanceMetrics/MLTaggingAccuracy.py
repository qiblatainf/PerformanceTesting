class MLTaggingAccuracy:
    def __init__(self, module_name, test_string):
        self.module_name = module_name
        self.test_string = test_string
        
    def accuracy_score(self):
        from Image.ImageLibraries import ImageModels
        from Image.ImageTestData import ImageData

        self.test_string = ImageData(self.module_name, self.test_string).test_data()

        preds = ImageModels(self.module_name, self.test_string).lib()

        with open("data\MLTaggingDatasets\imagenet_testset.txt", "r") as file:
            lines = file.readlines()

        # print(str(preds))
        correctPredictions = 0
        for i in range(0, len(preds)):
            #print(str(i) + " Text Line: " + str(((lines[i].strip()).split(", "))))
            #print(str(i) + " ML Array: " + str(preds[i]))

            if any(elem in lines[i] for elem in preds[i]):
                correctPredictions += 1
                
        return {"Performance Metric: Accuracy Score": str(round((correctPredictions/(len(preds))),6)*100) + "%"}
# print(ProfaneAccuracy("better_profanity").accuracy())