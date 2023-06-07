class BleuScore:
    def __init__(self, module_name, test_string):
        self.module_name = module_name
        self.test_string = test_string

    def bleu_score(self):
        from nltk.translate.bleu_score import sentence_bleu

        from Text.TextLibraries import TextLibrary
        from Text.TextTestData import TextData

        testData = TextData(self.module_name, self.test_string).test_data()
        textLib = TextLibrary(self.module_name, testData).lib()

        candidates = textLib.split(" / ")

        n = 0
        if (self.test_string == "small"):
            n = 5
        elif (self.test_string == "medium"):
            n = 20
        elif (self.test_string == "large"):
            n = 100

        references = []
        with open('data/translationDatasets/englishDataset.txt', 'r', encoding='utf-8') as f:
            for i in range(n):
                line = f.readline()
                if not line:
                    break
                references.append(line.strip())
                #print(str(i) + ": " + line)

            totalScore = 0
            # print("References: " + ', '.join(references))
            # print("Candidates: " + ', '.join(candidates))

            for reference, candidate in zip(references, candidates):
                score = sentence_bleu([candidate], reference, weights = (0.5, 0.5))
                #print("Score: " + str(score))
                totalScore += score
            # if(s and m and l):
            #     # Add bleu scores next
            #     candidates = [s.split(), m.split(), l.split()]
            #     references = ["i wish youd trust me".split(), 
            #                 "he and only he knows the whole truth".split(), 
            #                 "i can not stand being in traffic jams".split()]
            #     score = 0
            #     for reference, candidate in zip(references, candidates):
            #         score += sentence_bleu([candidate], reference, weights = (0.5, 0.5))
            return {"Performance Metric: BLEU SCORE": str(round((totalScore/n),6))}
