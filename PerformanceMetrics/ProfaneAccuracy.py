from sklearn.metrics import accuracy_score
# import os
# os.chdir("D://PerformanceTesting//")


import sys
 
# adding Folder_2 to the system path
sys.path.insert(0, 'D://PerformanceTesting//')

from Speech.SpeechLibraries import SpeechLibrary
from Speech.SpeechTestData import SpeechData

module_name = "profanityfilter"
# accuracy_score(labels_test,pred)

s = SpeechData(module_name, "small").test_data()
m = SpeechData(module_name, "medium").test_data()
l = SpeechData(module_name, "large").test_data()

s = SpeechLibrary(module_name, s).lib()
m = SpeechLibrary(module_name, m).lib()
l = SpeechLibrary(module_name, l).lib()

# print(s)

test = [s, m, l]
print(test)
pred = [True, True, False]
print(pred)

accuracy = accuracy_score(test,pred)
print(round(accuracy*100,2))
