import subprocess
class FIDScore:
    def __init__(self, module_name, test_string):
        self.module_name = module_name
        self.test_string = test_string
        
    def fid_score(self):  
        run_command('python -m pytorch_fid Image/ImageGenModels/genImages data/ImageGenDatasets/refGANDataset')

def run_command(command):
    try:
        output = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT, universal_newlines=True)
        print(output)
    except subprocess.CalledProcessError as e:
        print(f"Command '{command}' failed with error code {e.returncode}:")
        print(e.output)