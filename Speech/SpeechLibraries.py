

class SpeechLibrary:
    def __init__(self, module_name, test_string):
        self.module_name = module_name
        self.test_string = test_string
          
    def lib(self): 
        if (self.module_name == "better_profanity"):
            from Speech.ProfanityDetectionLibraries.better_profanity_detector import detect
            return detect(self.test_string) 
        elif (self.module_name == "profanity_filter"):
            from Speech.ProfanityDetectionLibraries.profanity_filter_detector import detect
            return detect(self.test_string)
        elif(self.module_name == "profanityfilter"):
            from Speech.ProfanityDetectionLibraries.profanityfilter_detector import detect
            return detect(self.test_string)
        elif(self.module_name == "profanity"):
            from Speech.ProfanityDetectionLibraries.profanity_detector import detect
            return detect(self.test_string)