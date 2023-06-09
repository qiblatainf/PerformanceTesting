class ImageData:
    def __init__(self, module_name, test_string):
        self.module_name = module_name
        self.test_string = test_string
          
    def test_data(self):
        if (self.module_name == "alexnet" or self.module_name == "mobilenetv2" or self.module_name == "densenet"):
            if (self.test_string == "small"):
                self.test_string = 15
            elif(self.test_string == "medium"):
                self.test_string = 60
            elif (self.test_string == "large"):
                self.test_string = 120 
        elif (self.module_name == "stablediffusionGAN" or self.module_name == "openjourneyGAN" or self.module_name == "realisticvisionGAN" 
              or self.module_name == "realisticvisionGAN"):
            if (self.test_string == "small"):
                self.test_string = 5
            elif(self.test_string == "medium"):
                self.test_string = 15
            elif (self.test_string == "large"):
                self.test_string = 30
        return self.test_string

            
        
            
