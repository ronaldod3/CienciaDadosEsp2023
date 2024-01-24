#https://pt.linkedin.com/pulse/calculando-o-capm-python-rodrigo-jov%C3%AA

import yfinance as yf
from datetime import datetime
import numpy as np
import pandas as pd

end_data = datetime.now().strftime('%Y-%m-%d')

acao1 = (yf.download("VALE", start="2019-01-01", end=end_data, progress=False, interval='1mo')['Adj Close'].pct_change()).dropna()
mercado = (yf.download("^BVSP", start="2019-01-01", end=end_data, progress=False, interval='1mo')['Adj Close'].pct_change()).dropna()

cdi = pd.read_json('https://api.bcb.gov.br/dados/serie/bcdata.sgs.4390/dados?formato=json')['valor']
cdi1 = cdi[-len(mercado):]

acao1 = np.array(acao1)
mercado = np.array(mercado)

#estimacao do modelo

#alfa de Jenses

#risco especifico

#teste de modelo

#correlacao serial


#retorno_esperado = cdi1 + beta * (acao1 - cdi1)
