import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import os
from dotenv import load_dotenv
load_dotenv()

apikey = os.environ['apikey']

url = os.environ['url']

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url(url)

#translation = language_translator.translate(
#    text='Hello, how are you today?',
#    model_id='en-es').get_result()
#print(json.dumps(translation, indent=2, ensure_ascii=False))



def englishToFrench(englishText):
    if englishText is None:
        return None
 
    else:
        frenchText1 = language_translator.translate(englishText, model_id = 'en-fr').get_result()
        frenchText2 = frenchText1['translations']
        frenchText = frenchText2[0]['translation']

        return frenchText

def frenchToEnglish(frenchText):

    if frenchText is None:
        return None

    else:
        englishText1 = language_translator.translate(frenchText, model_id = 'fr-en').get_result()
        englishText2 = englishText1['translations']
        englishText = englishText2[0]['translation']
        return englishText

#test
#print(json.dumps(englishToFrench('Hello'), indent=2, ensure_ascii=False))
#print(json.dumps(frenchToEnglish('Bonjour'), indent=2, ensure_ascii=False))
