class SimilarityScore:
    def __init__(self, module_name, test_audio):
        self.module_name = module_name
        self.test_audio = test_audio
        
    def similarity_score(self):
        
        from thefuzz import fuzz 
        import sys
        
        # adding folder to the system path
        sys.path.insert(0, 'D://PerformanceTesting//')

        from Speech.SpeechLibraries import SpeechLibrary
        from Speech.SpeechTestData import SpeechData

        
        audio = SpeechData(self.module_name, self.test_audio).test_data()
        audio = SpeechLibrary(self.module_name, audio).lib()
        
        
        if (self.test_audio == "small"):
            string = "اور اس پہ تھا وہ کہتا ہے"
        elif (self.test_audio == "medium"):
            string = "میں اپنے دفتری کام کے لیے اپنے اردو آڈیو کی جانچ کر رہا ہوں۔ آئیے دیکھتے ہیں کہ تبدیلی کس حد تک درست طریقے سے کام کرتی ہے۔ اس آڈیو میں شامل کل الفاظ اڑتیس ہیں اور آڈیو کا دورانیہ صفر پوائنٹ پانچ سیکنڈ ہے۔"
        elif (self.test_audio == "large"):
            string = "کمپیوٹر سیکنڈوں میں بڑی تعداد میں اضافہ، گھٹا، ضرب اور تقسیم کر سکتا ہے۔ یہاں تک کہ ایک ماہر ریاضی دان کو بھی ایسے حسابات مکمل کرنے میں زیادہ وقت لگے گا۔ کمپیوٹر اب تمام ترقی یافتہ ممالک میں ڈیٹا پروسیسنگ کے لیے بڑے پیمانے پر استعمال کیے جاتے ہیں، جس میں حقائق کی تالیف، ارتباط اور انتخاب شامل ہیں۔ تحقیق، صنعت اور کاروبار کے تمام شعبوں میں کمپیوٹر کا استعمال بڑھ رہا ہے۔ کمپیوٹر کے بے شمار فوائد ہیں۔ وہ وقت بچاتے ہیں، کام کو تیز کرتے ہیں، مزدوری بچاتے ہیں، اور طویل مدت میں اخراجات کم کرتے ہیں۔ وہ تمام ترقی یافتہ ممالک میں تعلیمی اداروں، صنعتوں، تحقیقی لیبارٹریوں، سرکاری محکموں وغیرہ میں استعمال ہوتے ہیں۔"
        
        print(f"Similarity score: {fuzz.ratio(string, audio)}")
        
        
 
        # return "Similarity Score of " + self.module_name + " " + str(fuzz.ratio(string, audio)) + "%"
        # return "Accuracy of " + self.module_name + " " + str(round(accuracy*100,2)) + "%"

# print(ProfaneAccuracy("better_profanity").accuracy())
# s1 = SimilarityScore("google_transcribe", "small")
# s1.similarity_score()