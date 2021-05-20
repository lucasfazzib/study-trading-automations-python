import requests
import quandl
import yfinance
import investpy
import pandas_datareader
import binance.client
import zipfile
import io
import pandas as pd
import numpy as np


# 1. Fundos de investimento

# http://dados.cvm.gov.br/dataset
# http://dados.cvm.gov.br/dados/FI/DOC/INF_DIARIO/DADOS
# Coiar link de arquivo csv 

r = requests.get('http://dados.cvm.gov.br/dados/FI/DOC/INF_DIARIO/DADOS/inf_diario_fi_202105.csv')
lines = [i.strip().split(';') for i in r.text.split('\n')]
fundo = pd.DataFrame(lines[1:], columns = lines[0])
#print(fundo.head())

r2 = requests.get('http://dados.cvm.gov.br/dados/FI/DOC/EXTRATO/DADOS/extrato_fi_2021.csv')
lines2 = [i.strip().split(';') for i in r2.text.split('\n')]
cadastro = pd.DataFrame(lines2[1:], columns = lines2[0])
#print(cadastro.head())

fundos_df = cadastro.merge(fundo, how='left', on='CNPJ_FUNDO')
#print(fundos_df.head())

alaska = fundos_df[fundos_df['DENOM_SOCIAL'].str.contains('ALASKA', na = False)]
#print(alaska.shape)
#print(alaska.DENOM_SOCIAL.unique())

alaska_black = alaska[alaska['DENOM_SOCIAL'] == 'ALASKA BLACK 70 ADVISORY XP SEGUROS PREVIDENCIÁRIO FI EM COTAS DE FI MULTIMERCADO']
#print(alaska_black.columns)
#DT_COMPTC_y -> quando preço foi armazenado
# VL_QUOTA -> valor da cota naquele dia.
dados = alaska_black[['DT_COMPTC_y', 'VL_QUOTA']]
#print(dados.head())
dados.index = dados['DT_COMPTC_y']
#print(dados.head())

# plotando com pandas, necessario interface grafica.
#print(pd.to_numeric(dados['VL_QUOTA']).plot())



