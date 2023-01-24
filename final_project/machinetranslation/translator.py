import json
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
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



def english_to_french(english_text):
    if english_text is None:
        return None
 
    else:
        french_text1 = language_translator.translate(english_text, model_id = 'en-fr').get_result()
        french_text2 = french_text1['translations']
        french_text = french_text2[0]['translation']

        return french_text

def french_to_english(french_text):

    if french_text is None:
        return None

    else:
        english_text1 = language_translator.translate(french_text, model_id = 'fr-en').get_result()
        english_text2 = english_text1['translations']
        english_text = english_text2[0]['translation']
        return english_text

#test
#print(json.dumps(english_to_french('Hello'), indent=2, ensure_ascii=False))
#print(json.dumps(french_to_english('Bonjour'), indent=2, ensure_ascii=False))
