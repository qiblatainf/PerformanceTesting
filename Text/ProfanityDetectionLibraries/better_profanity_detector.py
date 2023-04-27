from better_profanity import profanity

def detect(string):
    result = profanity.contains_profanity(string)
    return result

