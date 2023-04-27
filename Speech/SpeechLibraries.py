class SpeechLibrary:
    def __init__(self, module_name, test_audio):
        self.module_name = module_name
        self.test_audio = test_audio
          
    def lib(self): 
        if (self.module_name == "google_transcribe"):
            from SpeechToTextLibraries.GoogleTranscribe.google_transcribe import transcribe
            return transcribe(self.test_audio) 
        
        #Add other libraries here
        
# print(SpeechLibrary("google_transcribe", "D:/PerformanceTesting/Speech/test-data/small.wav").lib())