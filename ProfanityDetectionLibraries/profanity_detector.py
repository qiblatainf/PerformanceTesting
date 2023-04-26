from profanity import profanity

def detect(string):
    result = profanity.contains_profanity(string)
    print(result)
    