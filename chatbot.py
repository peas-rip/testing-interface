import requests
import os
def chatres():

    paragraphs = '2'
    api_url = 'https://api.api-ninjas.com/v1/loremipsum?paragraphs={}'.format(paragraphs)
    response = requests.get(api_url, headers={'X-Api-Key': 'Q+BRZSNZzwljmcRyCKdNOA==FEy5bOukQpLHwo8H'})
    if response.status_code == requests.codes.ok:
        return response.text

    
