import os
import json
import requests
class connect():
    def getenv(self):
        return os.environ.get("API_URL")


    def get_plans(self, url):
        #criando um session object
        gh_session = requests.Session()
        plans = json.loads(gh_session.get(url).text)
        return plans.get("results")
