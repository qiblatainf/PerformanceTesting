import os
from google.cloud import speech_v1p1beta1 as speech
import soundfile as sf
from memory_profiler import profile
from line_profiler import LineProfiler
# from test_accuracy import check_similarity
import time
# import ray

import warnings
warnings.filterwarnings("ignore")

# ray.init(num_cpus = 4) 
# start = time.time()

# file_path = "D:/PerformanceTesting/Speech/test-data/small.wav"

# @profile(precision= 4)
# @ray.remote
def transcribe(file_path):
    #accessing the json key file
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "D:\PerformanceTesting\Speech\SpeechToTextLibraries\GoogleTranscribe\google-key.json"
    #creating a speech-to-text client object
    client = speech.SpeechClient()
    data, sample_rate = sf.read(file_path)
    # print(f'Sample rate: {sample_rate} Hz')
    first_lang = 'ur-PK'    # second_lang = 'en-UK'

    with open(file_path, 'rb') as audio_file:
        content = audio_file.read()

    audio = speech.RecognitionAudio(content=content)
    config = speech.RecognitionConfig(
        encoding= speech.RecognitionConfig.AudioEncoding.LINEAR16,
        sample_rate_hertz=sample_rate,
        language_code= first_lang,
    )
    response = client.recognize(config=config, audio=audio)
    for result in response.results:
        return result.alternatives[0].transcript
    
    # print(result)
    with open('./Speech/SpeechToTextLibraries/GoogleTranscribe/results/small_result.txt', 'w', encoding='utf-8') as f:
        f.write(result)
        
# STT = transcribe(file_path) 
# STT = transcribe.remote(file_path)
# result = ray.get(STT)
# print(STT)
# path = file_path
# lp = LineProfiler()
# lp_wrapper = lp(transcribe)
# lp_wrapper(path)
# lp.print_stats()

# print("آپ کیسے ہو")

# with open('./Speech/SpeechToTextLibraries/GoogleTranscribe/results/small_result.txt', 'w', encoding='utf-8') as f:
#     f.write(STT)
 
# check_similarity("very small", STT)
# print(result)
# stop = time.time()

# print("Time Consumed (Latency): {} secs".format(stop - start))