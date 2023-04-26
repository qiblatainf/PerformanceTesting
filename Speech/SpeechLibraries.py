

class SpeechLibrary:
    def __init__(self, module_name, test_string):
        self.module_name = module_name
        self.test_string = test_string
          
    def lib(self): 
        if (self.module_name == "better_profanity"):
            from ProfanityDetectionLibraries.better_profanity_detector import detect
            detect(self.test_string) 
        elif (self.module_name == "profanity_filter"):
            from profanity_filter_detector import detect
            detect(self.test_string)
        elif(self.module_name == "profanityfilter"):
            from profanityfilter_detector import detect
            detect(self.test_string)
        elif(self.module_name == "profanity"):
            from profanity_detector import detect
            detect(self.test_string)