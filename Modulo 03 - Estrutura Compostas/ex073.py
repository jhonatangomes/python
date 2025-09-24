print('-=' * 35)
tabela = ('Flamengo','Cruzeiro','Palmeiras','Mirassol',
          'Botafogo','Bahia','São Paulo','Fluminense',
          'Bragantino','Corinthians','Ceará SC','Grêmio',
          'Internacional','Santos','Atlético-MG','Vasco da Gama',
          'EC Vitória','Juventude','Fortaleza','Sport Recife')
print(f'lista de times do brasileirão : {tabela}')
print('-=' * 35)
print(f'Os 5 primeiro são {tabela[0:5]}')
print('-=' * 35)
print(f'Os 4 últimos são {tabela[-4:]}')
print('-=' * 35)
print(f'Times em ordem alfabética: {sorted(tabela)}')
print('-=' * 35)
print(f'O Vasco está na {tabela.index('Vasco da Gama')+1}ª posição')