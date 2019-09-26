from bs4 import BeautifulSoup
import requests
import json
import pandas as pd

data = requests.get('http://digidb.io/digimon-list/')
soup = BeautifulSoup(data.content,'html.parser')
data = soup.find('table', id='digiList')

digimon1 = []

for i in soup.find_all('th'):
    digimon1.append(i.string)
# print(digimon1)

digimon2 = []

data = data.find_all('tr')
for item in data[1:]:
    no = item.td.string
    nama = item.a.string
    gambar = item.img['src']
    stage = item.center.string
    typeDigimon = item.td.find_next_sibling().find_next_sibling().find_next_sibling()
    attribute = item.td.find_next_sibling().find_next_sibling().find_next_sibling().find_next_sibling()
    memory = attribute.find_next_sibling()
    equip = memory.find_next_sibling()
    HP = equip.find_next_sibling()
    SP = HP.find_next_sibling()
    attack = SP.find_next_sibling()
    defense = attack.find_next_sibling()
    intellegence = defense.find_next_sibling()
    speed = intellegence.find_next_sibling()
    x = {
        'no':int(no),
        'digimon':nama,
        'image':gambar,
        'stage':stage,
        'type':typeDigimon.string,
        'attribute':attribute.string,
        'memory':memory.string,
        'equip slots':equip.string,
        'hp':HP.string,
        'sp':SP.string,
        'atk':attack.string,
        'def':defense.string,
        'int':intellegence.string,
        'spd': speed.string}
    digimon2.append(x)
print(digimon2)

# Save to Json

with open('digimon.json','w') as x:
    x.write(str(digimon2).replace("'",'"'))


    
