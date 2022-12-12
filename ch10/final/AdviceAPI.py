import requests


class AdviceAPI:
  def __init__(self):
    self.url = "https://api.adviceslip.com/advice" #adviceapi url
  def get(self):
    data = requests.get(self.url) #gets permission to reference the site
    json = data.json()
    random_advice = json["slip"]
    f_slip = random_advice["advice"] #shortens to only the advice from the original string
    return f_slip