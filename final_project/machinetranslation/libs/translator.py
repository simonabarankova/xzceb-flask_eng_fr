'''This script translates French to English (function FrenchToEnglish)
and also from English to French (function englishToFrench) '''

import json
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

# Assign API keys to variables

APIKEY = os.environ['apikey']
URL = os.environ['url']

# Authenticate and instantiate the object of the Language Translator

authenticator = IAMAuthenticator(APIKEY)
language_translator = LanguageTranslatorV3(
    version="2018-05-01",
    authenticator=authenticator
)

language_translator.set_service_url(URL)

def english_to_french(english_text):

    '''This function translates from english to French
    Returns translated string in French'''

    if english_text is not None:

        translation = language_translator.translate(
        text = english_text,
        model_id ='en-fr').get_result()

        response_json = json.loads(json.dumps(translation, indent=2, ensure_ascii=False))
        french_text = response_json["translations"][0]["translation"]

        return french_text

    if_input_none = "You need to specify the text to be translated, man"
    return if_input_none

def french_to_english(french_text):

    '''This function translates from French to English
    Returns translated string in English'''

    if french_text is not None:

        translation = language_translator.translate(
        text = french_text,
        model_id ='fr-en').get_result()

        response_json = json.loads(json.dumps(translation, indent=2, ensure_ascii=False))
        english_text = response_json["translations"][0]["translation"]

        return english_text

    if_input_none = "You need to specify the text to be translated, man"
    return if_input_none

print(english_to_french("Hello my dear"))
