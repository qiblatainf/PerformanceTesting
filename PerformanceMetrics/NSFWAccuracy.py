
        

class NSFWAccuracy:
    def __init__(self, module_name, test_video):
        self.module_name = module_name
        self.test_video = test_video
        
    def nsfw_accuracy(self):
        from sklearn.metrics import accuracy_score
        import sys
        
        # adding folder to the system path
        sys.path.insert(1, '.\\Video\\')

        from VideoLibraries import VideoLibrary
        from VideoTestData import VideoData

        video = VideoData(self.module_name, self.test_video).test_data()
        video = VideoLibrary(self.module_name, video).lib()
        
        
        if (self.test_video == "small"):
            string = "NOT SAFE"
        elif (self.test_video== "medium"):
            string = "NOT SAFE"
            
        # s = VideoLibrary(self.module_name, s).lib()

        pred = [video]
        true = [100]
        
        accuracy = accuracy_score(pred, true)
        return "Accuracy of " + self.module_name + " " + str(round(accuracy*100,2)) + "%"
        
 
# print(ProfaneAccuracy("better_profanity").accuracy())
s1 = NSFWAccuracy("nsfw_mobilenet", "small")
s1.nsfw_accuracy()