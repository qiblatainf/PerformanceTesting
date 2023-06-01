class SpeechData:
    def __init__(self, module_name, test_audio):
        self.module_name = module_name
        self.test_audio = test_audio
          
    def test_data(self):
        if (self.module_name == "google_transcribe"):            
            if (self.test_audio == "small"):
                self.test_audio = "./Speech/test-data/small.wav"
            elif(self.test_audio == "medium"):
                self.test_audio = "./Speech/test-data/medium.wav"
            elif (self.test_audio == "large"):
                self.test_audio = "Not supported yet"
                
            return self.test_audio
        
            
