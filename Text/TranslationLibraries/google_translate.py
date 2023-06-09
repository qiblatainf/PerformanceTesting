import six
from google.cloud import translate_v2
from google.oauth2 import service_account
# import os
# os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = ""

creds = service_account.Credentials.from_service_account_file('ApiCredidentials\google_credidentials.json')

def detect(string):
    print(creds)

    translate_client = translate_v2.Client(credentials=creds)
    
    if isinstance(string, six.binary_type):
        string = string.decode("utf-8")
    
    result = translate_client.translate(string, target_language="en")
    return result["translatedText"]
    
    #print(u"Translation: {}".format(result["translatedText"]))
    # print(result["translatedText"])
    return result["translatedText"]
