import pandas as pd
import numpy as np
import requests

# Load data from the new API URL
url = 'https://api.bcb.gov.br/dados/serie/bcdata.sgs.12/dados?formato=json'
response = requests.get(url)
data = response.json()

# Create a DataFrame from the JSON data
cdi = pd.DataFrame(data)

# Convert 'data' column to datetime
cdi['data'] = pd.to_datetime(cdi['data'], dayfirst=True)

# Convert 'valor' column to numeric type
cdi['valor'] = pd.to_numeric(cdi['valor'], errors='coerce')

# Initialize variables
accumulated_valor = 0
accumulated_values = []

# Iterate through the DataFrame
for index, row in cdi.iterrows():
    # Check if it's Thursday
    if row['data'].day_name() == 'Thursday':
        accumulated_valor = row['valor']  # Initialize with the value for Thursday
    # Add the value for Friday, Monday, Tuesday, and Wednesday
    elif row['data'].day_name() in ['Friday', 'Monday', 'Tuesday', 'Wednesday']:
        accumulated_valor += row['valor']
    # Check if it's the last row or if the next row is Thursday (to save the accumulated value)
    if (index == len(cdi) - 1) or (cdi.loc[index + 1, 'data'].day_name() == 'Thursday'):
        accumulated_values.append(accumulated_valor)  # Save the accumulated value

# Convert the accumulated values to a NumPy array
accumulated_valor_array = np.array(accumulated_values)

print(accumulated_valor_array)
