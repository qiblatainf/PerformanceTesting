from profanityfilter import ProfanityFilter


def detect(string):
    pf = ProfanityFilter()
    result = pf.is_profane(string)
    print(result)
    
