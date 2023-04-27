class ProfaneAccuracy:
    def __init__(self, module_name):
        self.module_name = module_name
        
    def accuracy(self):
        
        from sklearn.metrics import accuracy_score
        import sys
        
        # adding folder to the system path
        sys.path.insert(0, 'D://PerformanceTesting//')

        from Speech.SpeechLibraries import SpeechLibrary
        from Speech.SpeechTestData import SpeechData

        s = SpeechData(self.module_name, "small").test_data()
        m = SpeechData(self.module_name, "medium").test_data()
        l = SpeechData(self.module_name, "large").test_data()

        s = SpeechLibrary(self.module_name, s).lib()
        m = SpeechLibrary(self.module_name, m).lib()
        l = SpeechLibrary(self.module_name, l).lib()

        test = [s, m, l]
        pred = [True, True, False]

        accuracy = accuracy_score(test,pred)
        return "Accuracy of " + self.module_name + " " + str(round(accuracy*100,2)) + "%"

