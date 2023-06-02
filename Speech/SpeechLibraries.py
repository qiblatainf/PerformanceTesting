class SpeechLibrary:
    def __init__(self, module_name, test_audio):
        self.module_name = module_name
        self.test_audio = test_audio
          
    def lib(self): 
        if (self.module_name == "google_transcribe" and self.test_audio != "large"):
            from Speech.SpeechToTextLibraries.GoogleTranscribe.google_transcribe import transcribe
            return transcribe(self.test_audio) 
        
        if (self.test_audio == "large"):
            print("Audio files greater than 2 minutes not supported.")
            
        
        #Add other libraries here
        
# print(SpeechLibrary("google_transcribe", "D:/PerformanceTesting/Speech/test-data/small.wav").lib())