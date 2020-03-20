import requests

def  translating(original_sentence,lang_from,lang_to):
    #TRANSLATING get translation from an API
    #   Get a sentence in language lang_from and translate to lang_to
    #   print codes
    #     200 Operation completed successfully
    #     401 Invalid API key
    #     402 Blocked API key
    #     404 Exceeded the daily limit on the amount of translated text
    #     413 Exceeded the maximum text size
    #     422 The text cannot be translated
    #     501 The specified translation direction is not supported

    # API params
    api_url = 'https://translate.yandex.net/api/v1.5/tr.json/translate?'
    api_key = 'trnsl.1.1.20170317T113329Z.422ab0bd5e8bd8ff.62c79feb943e326d73044d35e827eabd42a3e14c'

    # API call
    url = api_url+'key='+api_key+'&text='+original_sentence+'&lang='+lang_from+'-'+lang_to
    result = requests.get(url)
    
    if result.status_code == 200:
        translated_sentence = result.text
    else:
        value = result.status_code
        if value == 401:
            print('Invalid API key')
        elif value == 402:
            print('Blocked API key')
        elif value ==  404:
            print('Exceeded the daily limit on the amount of translated text')
        elif value ==  413:
            print('Exceeded the maximum text size')
        elif value ==  422:
            print('The text cannot be translated')
        elif value ==  501:
            print('The specified translation direction is not supported')
        translated_sentence = ''
    return translated_sentence
