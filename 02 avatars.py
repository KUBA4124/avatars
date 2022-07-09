from urllib import response
import requests
import random

from pathlib import Path
response = requests.get(f'https://avatars.dicebear.com/api/male/{random.random()}.svg')


Path('./avatars').mkdir(exist_ok=True)

with open('./avatars/avatar.svg', 'wb') as file:
    file.write(response.content)


