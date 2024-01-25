import yfinance as yf
from datetime import datetime
import numpy as np
import pandas as pd

end_data = datetime.now().strftime('%Y-%m-%d')
mercado = (yf.download("^BVSP", start="2019-01-01", end=end_data, progress=False, interval='1mo')['Adj Close'].pct_change()).dropna()
mercado = np.array(mercado)

#CDI DIARIO
cdi = pd.read_json('https://api.bcb.gov.br/dados/serie/bcdata.sgs.12/dados?formato=json')

#CDI MES
cdi = pd.read_json('https://api.bcb.gov.br/dados/serie/bcdata.sgs.4390/dados?formato=json')['valor']
cdi1 = np.array(cdi[-len(mercado):])

import statsmodels.formula.api as smf
acoes = ['VALE', 'PETR4.SA']

for item in acoes:
    #Modelo Regressao/Teste Modelo
    acao = (yf.download(item, start="2019-01-01", end=end_data, progress=False, interval='1mo')['Adj Close'].pct_change()).dropna()
    y = acao
    x = mercado
    df = pd.DataFrame({'Ativo': y, 'Mercado': x})
    model = smf.ols('Ativo ~ Mercado', data=df).fit()
    print(f'Ativo: {item}')
    print(model.summary(), '\n')

    #Alfa Jensen é o intercepto, teste t do intercepto
    y = acao - cdi1
    x = mercado - cdi1
    df = pd.DataFrame({'Rativo': y, 'Rmercado': x})
    model = smf.ols('Rativo ~ Rmercado', data=df).fit()
    print(f'Ativo: {item}')
    print(f'Alfa de Jensen: {item}')
    print(model.summary(), '\n')

'''risco especifico

    # Specific Risk and t-value
    specific_risk = np.sqrt(model.mse_resid)  # Residual Standard Error
    dof = len(acao) - 2  # Degrees of Freedom
    t_value = model.tvalues['Mercado']  # t-value for the market coefficient

    print(f'Specific Risk for {item}: {specific_risk}')
    print(f't-value for {item}: {t_value}\n')


#correlacao serial

    # Plotting Correlogram
    fig, ax = plt.subplots(figsize=(8, 4))
    tsaplots.plot_acf(acao, lags=20, ax=ax, alpha=0.05)
    ax.set_title(f'Autocorrelation for {item}')
    plt.show()

'''


