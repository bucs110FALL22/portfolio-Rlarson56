import requests


class AdviceAPI:
  def __init__(self):
    self.url = "https://api.adviceslip.com/advice" #adviceapi url
  def get(self):
    data = requests.get(self.url) #gets permission to reference the site
    json = data.json()
    advice = json["slip"]
    slip = advice["advice"] #shortens to only the advice from the original string
    return slip