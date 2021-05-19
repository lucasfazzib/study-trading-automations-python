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

print(fundo.head())