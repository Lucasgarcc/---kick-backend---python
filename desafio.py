
from cmath import inf
import requests
from bs4 import BeautifulSoup

HEADERS = {
'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; Touch; MAARJS; rv:11.0) like Gecko',
'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
'Accept-Encoding':'gzip,deflate,sdch',
'Accept-Language':'pt-BR; q=0.9;en-US,en;q=0.8',
'Connection':'Keep-alive',
'Referer':'https://www.google.com.br',
}
resposta = requests.get('https://www.netshoes.com.br/games?mi=hm_ger_mntop_E_games&psn=Menu_Top', headers=HEADERS)

#print(resposta.text)
soup = BeautifulSoup(resposta.text,'html.parser')

span = soup.find_all(class_='item-card__description')

lista = []
for i in  (span):
    span = soup.find_all('snap')
    lista.append(i.text)
print(lista)

with open('lista.csv','w') as l:
        l.write(str(lista))
        
        
        import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('lista.csv')

df.plot(lista ='Lista', x = 'produtos', y = 'informações')

plt.show()

