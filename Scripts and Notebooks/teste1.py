import requests
from bs4 import BeautifulSoup

# Fazer a solicitação GET à página web
url = 'https://www.flashscore.pt/futebol/alemanha/bundesliga-2017-2018/classificacoes/#/U5NfqEkf/table/overall'
response = requests.get(url)

# Criar o objeto BeautifulSoup para analisar o conteúdo da página
soup = BeautifulSoup(response.content, 'html.parser')

#print (soup)


table_body = soup.find('body', class_='responsive soccer _fs flat pid_20 mgc hasFsNews tournament-p...yout light-bg-1 v3 bg3 seoTopWrapperHidden background-add-on')

print (table_body)
'''

# Encontrar a classe ui-table__body
table_body = soup.find('div', class_='ui-table__body')

# Encontrar todas as classes ui-table__row dentro de ui-table__body
rows = table_body.find_all('div', class_='ui-table__row')

# Percorrer as linhas
for row in rows:
    # Encontrar a classe table__cell table__cell--rank table__cell--sorted
    rank_cell = row.find('div', class_='table__cell table__cell--rank table__cell--sorted')
    rank = rank_cell.text.strip()
    
    # Encontrar a classe tableCellParticipant__name dentro de table__cell table__cell--participant
    name_cell = row.find('div', class_='table__cell table__cell--participant')
    name = name_cell.find('span', class_='tableCellParticipant__name').text.strip()

    print(f'Rank: {rank}, Equipe: {name}')
'''