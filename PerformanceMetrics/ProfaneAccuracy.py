class ProfaneAccuracy:
    def __init__(self, module_name):
        self.module_name = module_name
        
    def accuracy(self):
        
        from sklearn.metrics import accuracy_score
        import sys
        
        # adding folder to the system path
        sys.path.insert(0, 'D://PerformanceTesting//')

        from Text.TextLibraries import TextLibrary
        from Text.TextTestData import TextData

        s = TextData(self.module_name, "small").test_data()
        m = TextData(self.module_name, "medium").test_data()
        l = TextData(self.module_name, "large").test_data()

        s = TextLibrary(self.module_name, s).lib()
        m = TextLibrary(self.module_name, m).lib()
        l = TextLibrary(self.module_name, l).lib()

        pred = [s, m, l]
        # print(pred)
        true = [True, True, False]
        # print(true)

        accuracy = accuracy_score(pred, true)
        return "Accuracy of " + self.module_name + " " + str(round(accuracy*100,2)) + "%"

# print(ProfaneAccuracy("better_profanity").accuracy())