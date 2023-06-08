class ImageModels:
    def __init__(self, module_name, test_string):
        self.module_name = module_name
        self.test_string = test_string
          
    def lib(self): 
        if (self.module_name == "alexnet"):
            from Image.AutoTaggingModels.alexnet import detect

            # sends dataset type path to perform testing
            return detect(self.test_string) 
        elif (self.module_name == "mobilenetv2"):
            from Image.AutoTaggingModels.mobilenetv2 import detect

            # sends dataset type path to perform testing
            return detect(self.test_string) 
        elif (self.module_name == "densenet"):
            from Image.AutoTaggingModels.densenet import detect

            # sends dataset type path to perform testing
            return detect(self.test_string) 
        elif (self.module_name == "stablediffusionGAN"):
            from Image.ImageGenModels.stablediffusion import detect

            # sends dataset type path to perform testing
            return detect(self.test_string) 
        elif (self.module_name == "openjourneyGAN"):
            from Image.ImageGenModels.openjourney import detect

            # sends dataset type path to perform testing
            return detect(self.test_string) 
        elif (self.module_name == "realisticvisionGAN"):
            from Image.ImageGenModels.realisticvision import detect

            # sends dataset type path to perform testing
            return detect(self.test_string) 
        else:
            print("Module " + self.module_name + " not found")
