import pandas as pd

# Dados da época, liga, equipes e classificação
epoca = [2018, 2018, 2018, 2018, 2018, 2018, 2018, 2018, 2018,2018,2018,2018,2018,2018,2018,2018,2018,2018]
liga = ['Bundesliga', 'Bundesliga','Bundesliga','Bundesliga','Bundesliga','Bundesliga','Bundesliga','Bundesliga','Bundesliga','Bundesliga','Bundesliga','Bundesliga','Bundesliga','Bundesliga','Bundesliga','Bundesliga','Bundesliga','Bundesliga',]
equipas = ['Bayern', 'Schalde', 'Hoffenheim', 'Dortmund', 'Leverkusen', 'RB Leipzig', 'Stuttgart', 'Frankfurt', 'Monchengladbach', 'Hertha', 'Bremen', 'Augsburg', 'Hannover', 'Mainz', 'Freiburg', 'Wolfsburg', 'Hamburger SV', 'FC Koin']
classificacao = [1, 2, 3, 4, 5, 6, 7, 8,9,10,11,12,13,14,15,16,17,18]



# Criar um dicionário com os dados
dados = {'epoca': epoca, 'liga': liga, 'equipa': equipas, 'classificacao': classificacao}

# Criar o DataFrame a partir do dicionário
df = pd.DataFrame(dados)

# Salvar o DataFrame em um arquivo CSV
df.to_csv('bundesliga1718.csv', index=False)

df = pd.read_csv('bundesliga1718.csv')

epoca_2019 = [2019] * len(df)
equipa_2019 = ['Bayern', 'Dortmund', 'RB Leipzig', 'Leverkusen', 'Monchengladbach', 'Wolfsburg', 'Frankfurt',  'Bremen', 'Hoffenheim', 'Dusseldorf', 'Hertha', 'Mainz', 'Freiburg', 'Schalke','Augsburg','Stuttgart', 'Hannover', 'Nurnberg']
classificacao_2019 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]

df_2019 = pd.DataFrame({'epoca': epoca_2019, 'liga': df['liga'], 'equipa': equipa_2019, 'classificacao': classificacao_2019})
df = pd.concat([df, df_2019])


epoca_2020 = [2020, 2020,2020,2020,2020,2020,2020,2020,2020,2020,2020,2020,2020,2020,2020,2020,2020,2020]
classificacao_2020 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]
equipa_2020 = ['Bayern', 'Dortmund', 'RB Leipzig', 'Monchengladbach', 'Leverkusen', 'Hoffenheim', 'Wolfsburg', 'Freiburg', 'Frankfurt', 'Hertha', 'Bremen', 'Augsburg', 'Hannover', 'Mainz', 'Schalke', 'Stuttgart', 'Hamburger SV', 'FC Koin']

df_2020 = pd.DataFrame({'epoca': epoca_2020, 'liga': liga, 'equipa': equipa_2020, 'classificacao': classificacao_2020})


df = pd.concat([df, df_2020]) 


df.to_csv('bundesliga1718.csv', index=False)


# La liga

# Dados da época, liga, equipes e classificação
epoca1 = [2018,2018,2018,2018,2018,2018,2018,2018,2018,2018,2018,2018,2018,2018,2018,2018,2018,2018,2018,2018]
liga1 = ['La Liga','La Liga','La Liga','La Liga','La Liga','La Liga','La Liga','La Liga','La Liga','La Liga','La Liga','La Liga','La Liga','La Liga','La Liga','La Liga','La Liga','La Liga','La Liga','La Liga'] 
equipas1 = ['Barcelona', 'Atlético Madrid', 'Real Madrid', 'Valencia', 'Villarreal', 'Betis', 'Sevilla', 'Getafe', 'Eibar', 'Girona', 'Espanyol', 'Real Sociedad', 'Celta Vigo', 'Alavés','Levante', 'Athletic Club', 'Leganes', 'La Coruña', 'Las Palmas', 'Malaga']
classificacao1 = [1, 2, 3, 4, 5, 6, 7, 8,9,10,11,12,13,14,15,16,17,18, 19,20]



# Criar um dicionário com os dados
dados2 = {'epoca': epoca1, 'liga': liga1, 'equipa': equipas1, 'classificacao': classificacao1}


# Criar o DataFrame a partir do dicionário
df3 = pd.DataFrame(dados2)

df = pd.concat([df, df3]) 

# Salvar o DataFrame em um arquivo CSV
df.to_csv('bundesliga1718.csv', index=False)


df4 = pd.read_csv('bundesliga1718.csv')

epoca_2019 = [2019,2019,2019,2019,2019,2019,2019,2019,2019,2019,2019,2019,2019,2019,2019,2019,2019,2019,2019,2019]
equipas_2019 = ['Barcelona', 'Atlético Madrid', 'Real Madrid', 'Valencia', 'Getafe', 'Sevilla', 'Espanyol','Athletic Club', 'Real Sociedad',  'Betis',  'Alavés', 'Eibar',  'Leganes', 'Villareal', 'Levante', 'Valladolid', 'Celta Vigo' , 'Girona', 'Huesca', 'Rayo Vallecano']
classificacao_2019 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18,19,20]


df_2019 = pd.DataFrame({'epoca': epoca_2019, 'liga': liga1, 'equipa': equipas_2019, 'classificacao': classificacao_2019})
df4 = pd.concat([df, df_2019])




df4.to_csv('bundesliga1718.csv', index=False)



epoca_2020 = [2020, 2020,2020,2020,2020,2020,2020,2020,2020,2020,2020,2020,2020,2020,2020,2020,2020,2020,2020,2020]
classificacao_2020 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18,19,20]
equipas_2020 = ['Real Madrid','Barcelona', 'Atlético Madrid', 'Sevilla', 'Villarreal','Real Sociedad','Granada', 'Getafe', 'Valencia','Osasuna','Athletic Club', 'Levante', 'Valladolid', 'Eibar', 'Betis', 'Alavés', 'Celta Vigo' , 'Leganes', 'Mallorca', 'Espanyol']

df_2020 = pd.DataFrame({'epoca': epoca_2020, 'liga': liga1, 'equipa': equipas_2020, 'classificacao': classificacao_2020})



df = pd.concat([df, df_2020]) 


df.to_csv('bundesliga1718.csv', index=False)


# Ligue 


# Dados da época, liga, equipes e classificação
epoca1 = [2018,2018,2018,2018,2018,2018,2018,2018,2018,2018,2018,2018,2018,2018,2018,2018,2018,2018,2018,2018]
liga1 = ['Ligue', 'Ligue', 'Ligue','Ligue','Ligue','Ligue','Ligue','Ligue','Ligue','Ligue','Ligue','Ligue','Ligue','Ligue','Ligue','Ligue','Ligue','Ligue','Ligue','Ligue'] 
equipas1 =['Paris S-G', 'Monaco', 'Lyon', 'Marseille', 'Rennes', 'Bordeaux', 'Saint-Étienne', 'Nice', 'Nantes', 'Montpellier', 'Dijon', 'Guingamp', 'Amiens', 'Angers', 'Strasbourg', 'Caen', 'Lille', 'Toulouse', 'Troyes', 'Metz']
classificacao1 = [1, 2, 3, 4, 5, 6, 7, 8,9,10,11,12,13,14,15,16,17,18, 19,20]



# Criar um dicionário com os dados
dados2 = {'epoca': epoca1, 'liga': liga1, 'equipa': equipas1, 'classificacao': classificacao1}


# Criar o DataFrame a partir do dicionário
df3 = pd.DataFrame(dados2)

df = pd.concat([df, df3]) 


df.to_csv('bundesliga1718.csv', index=False)


epoca_2019 = [2019,2019,2019,2019,2019,2019,2019,2019,2019,2019,2019,2019,2019,2019,2019,2019,2019,2019,2019,2019]
equipas1 =['Paris S-G', 'Lille', 'Lyon', 'Saint-Étienne', 'Marseille', 'Montpellier', 'Nice',  'Reims', 'Nimes', 'Rennes', 'Strasbourg', 'Nantes', 'Angers', 'Bordeaux', 'Amiens',  'Toulouse', 'Monaco', 'Dijon', 'Caen', 'Guingamp']
classificacao_2019 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18,19,20]

print(len(epoca_2019))
print(len(equipas1))
print(len(classificacao_2019))

df_2019 = pd.DataFrame({'epoca': epoca_2019, 'liga': liga1, 'equipa': equipas1, 'classificacao': classificacao_2019})
df4 = pd.concat([df, df_2019])




df4.to_csv('bundesliga1718.csv', index=False)

epoca_2020 = [2020, 2020,2020,2020,2020,2020,2020,2020,2020,2020,2020,2020,2020,2020,2020,2020,2020,2020,2020,2020]
classificacao_2020 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18,19,20]
equipas_2020 = ['Paris S-G', 'Marseille','Rennes','Lille', 'Nice',  'Reims', 'Lyon', 'Montpellier', 'Monaco', 'Strasbourg', 'Angers', 'Bordeaux', 'Nantes', 'Brest', 'Metz', 'Dijon', 'Saint-Étienne', 'Nimes', 'Amiens', 'Toulouse']


df_2020 = pd.DataFrame({'epoca': epoca_2020, 'liga': liga1, 'equipa': equipas_2020, 'classificacao': classificacao_2020})



df = pd.concat([df, df_2020]) 


df.to_csv('bundesliga1718.csv', index=False)

# Premier League

# Dados da época, liga, equipes e classificação
epoca1 = [2018,2018,2018,2018,2018,2018,2018,2018,2018,2018,2018,2018,2018,2018,2018,2018,2018,2018,2018,2018]
liga1 = ['Premier League', 'Premier League', 'Premier League', 'Premier League', 'Premier League','Premier League','Premier League','Premier League','Premier League','Premier League','Premier League','Premier League','Premier League','Premier League','Premier League','Premier League','Premier League','Premier League','Premier League','Premier League']  
equipas1 =['Manchester City', 'Manchester Utd', 'Tottenham', 'Liverpool', 'Chelsea', 'Arsenal', 'Burnley', 'Everton', 'Leicester', 'Newcastle', 'Crystal Palace', 'Bournemouth', 'West Ham', 'Watford', 'Brighton', 'Huddersfield', 'Southhampton', 'Swansea', 'Stoke', 'West Brom']
classificacao1 = [1, 2, 3, 4, 5, 6, 7, 8,9,10,11,12,13,14,15,16,17,18, 19,20]



# Criar um dicionário com os dados
dados2 = {'epoca': epoca1, 'liga': liga1, 'equipa': equipas1, 'classificacao': classificacao1}


# Criar o DataFrame a partir do dicionário
df3 = pd.DataFrame(dados2)

df = pd.concat([df, df3]) 


df.to_csv('bundesliga1718.csv', index=False)

epoca_2019 = [2019,2019,2019,2019,2019,2019,2019,2019,2019,2019,2019,2019,2019,2019,2019,2019,2019,2019,2019,2019]
equipas1 =['Manchester City', 'Liverpool', 'Chelsea', 'Tottenham', 'Arsenal', 'Manchester Utd', 'Wolves', 'Everton', 'Leicester',  'West Ham', 'Watford', 'Crystal Palace', 'Newcastle',  'Bournemouth', 'Burnley', 'Southhampton', 'Brighton', 'Cardiff', 'Fulham' , 'Huddersfield']
classificacao_2019 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18,19,20]

print(len(epoca_2019))
print(len(equipas1))
print(len(classificacao_2019))

df_2019 = pd.DataFrame({'epoca': epoca_2019, 'liga': liga1, 'equipa': equipas1, 'classificacao': classificacao_2019})
df4 = pd.concat([df, df_2019])

df4.to_csv('bundesliga1718.csv', index=False)

epoca_2020 = [2020, 2020,2020,2020,2020,2020,2020,2020,2020,2020,2020,2020,2020,2020,2020,2020,2020,2020,2020,2020]
classificacao_2020 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18,19,20]
equipas_2020 = ['Liverpool', 'Manchester City', 'Manchester Utd', 'Chelsea', 'Leicester', 'Tottenham', 'Wolves', 'Arsenal', 'Sheffield Utd', 'Burnley', 'Southampton', 'Everton', 'Newcastle', 'Crystal Palace', 'Brighton', 'West Ham', 'Aston Villa', 'Bournemouth', 'Watford', 'Norwich']


df_2020 = pd.DataFrame({'epoca': epoca_2020, 'liga': liga1, 'equipa': equipas_2020, 'classificacao': classificacao_2020})



df = pd.concat([df, df_2020]) 


df.to_csv('bundesliga1718.csv', index=False)

# Serie A

# Dados da época, liga, equipes e classificação
epoca1 = [2018,2018,2018,2018,2018,2018,2018,2018,2018,2018,2018,2018,2018,2018,2018,2018,2018,2018,2018,2018]
liga1 = ['Serie A','Serie A','Serie A','Serie A','Serie A','Serie A','Serie A','Serie A','Serie A','Serie A', 'Serie A','Serie A','Serie A','Serie A','Serie A','Serie A','Serie A','Serie A','Serie A','Serie A']  
equipas1 =['Juventus', 'Napoli', 'Roma', 'Inter', 'Lazio', 'Milan', 'Atalanta', 'Fiorentina', 'Torino', 'Sampdoria', 'Sassuolo', 'Genoa', 'Chievo', 'Udinese', 'Bologna', 'Cagliari', 'Spal', 'Crotone', 'Verona', 'Benevento']
classificacao1 = [1, 2, 3, 4, 5, 6, 7, 8,9,10,11,12,13,14,15,16,17,18, 19,20]



# Criar um dicionário com os dados
dados2 = {'epoca': epoca1, 'liga': liga1, 'equipa': equipas1, 'classificacao': classificacao1}


# Criar o DataFrame a partir do dicionário
df3 = pd.DataFrame(dados2)

df = pd.concat([df, df3]) 


df.to_csv('bundesliga1718.csv', index=False)

epoca_2019 = [2019,2019,2019,2019,2019,2019,2019,2019,2019,2019,2019,2019,2019,2019,2019,2019,2019,2019,2019,2019]
equipas1 =['Juventus', 'Napoli', 'Atalanta', 'Inter', 'Milan', 'Roma', 'Torino', 'Lazio',  'Sampdoria', 'Bologna', 'Sassuolo', 'Udinese', 'Spal', 'Parma', 'Cagliari', 'Fiorentina', 'Genoa', 'Empoli', 'Frosinone', 'Chievo']

classificacao_2019 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18,19,20]

print(len(epoca_2019))
print(len(equipas1))
print(len(classificacao_2019))

df_2019 = pd.DataFrame({'epoca': epoca_2019, 'liga': liga1, 'equipa': equipas1, 'classificacao': classificacao_2019})
df4 = pd.concat([df, df_2019])

df4.to_csv('bundesliga1718.csv', index=False)

epoca_2020 = [2020, 2020,2020,2020,2020,2020,2020,2020,2020,2020,2020,2020,2020,2020,2020,2020,2020,2020,2020,2020]
classificacao_2020 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18,19,20]
equipas_2020 =['Juventus', 'Inter', 'Atalanta', 'Lazio', 'Roma', 'Milan', 'Napoli', 'Sassuolo', 'Verona',  'Fiorentina', 'Parma', 'Bologna', 'Udinese', 'Cagliari', 'Sampdoria', 'Torino', 'Genoa', 'Lecce', 'Brescia', 'Spal']


df_2020 = pd.DataFrame({'epoca': epoca_2020, 'liga': liga1, 'equipa': equipas_2020, 'classificacao': classificacao_2020})



df = pd.concat([df, df_2020]) 


df.to_csv('bundesliga1718.csv', index=False)
