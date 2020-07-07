import requests
import json

API_KEY = 't-8Kcg4CJP9b'
PROJECT_TOKEN = 'tiwTLdXvnjJ6'
RUN_TOKEN = 'tSkEiEw4Ft6a'




class DataCollect:
    def __init__(self, api_key, project_token):
        self.api_key = api_key
        self.project_token = project_token
        self.params = {
            'api_key' : self.api_key
        }
        self.get_data()
    
    def get_data(self):
        response = requests.get(f"https://www.parsehub.com/api/v2/projects/{PROJECT_TOKEN}/last_ready_run/data", params = {'api_key': API_KEY})
        self.data = json.loads(response.text)
    
    def get_total_cases(self):
        data =  self.data['total']
        for content in data:
            if content['name'] == 'Coronavirus Cases:':
                return content['values']

    def get_total_deaths(self):
        data =  self.data['total']
        for content in data:
            if content['name'] == 'Deaths:':
                return content['values']

    def get_total_recovered(self):
        data =  self.data['total']
        for content in data:
            if content['name'] == 'Recovered:':
                return content['values']

    def get_country_data(self, country):
        data = self.data['country']
        for content in data:
            if content['name'].lower() == country.lower():
                return content

data = DataCollect(API_KEY, PROJECT_TOKEN)
#print(data.data)
print(f'Total Cases: {data.get_total_cases()}')
print(f'Total Recovered: {data.get_total_recovered()}')
print(f'Total Deaths: {data.get_total_deaths()}')
data.get_country_data('USA')


