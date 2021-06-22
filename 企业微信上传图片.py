import requests

url = "https://qyapi.weixin.qq.com/cgi-bin/media/upload?access_token=TpqAuI3eclGywYb7d6O6xAxLCoz6_AwIDztJS66nBnWQXom9qHUy-yLUrz5N6NFTRVKF5KkfANaT0cPXejDyG5_axLQo8TrMkKCdwSq4RHrYCtwBQSUdf3udlsOmfrRyTgzvk8gnCBEV9LPrRDZvviyrCO473c2R5rTbqPE3kTkVURoz7eqkUUmTz2eHPl8fFt9uyjiVSPrHKpfEuQYnGA&type=image"

payload={}
files=[
  ('media',('1231.jpg',open('1231.jpg','rb'),'image/jpeg'))
]
headers = {}

response = requests.request("POST", url, headers=headers, data=payload, files=files)

print(response.text)
