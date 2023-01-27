import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import scipy.stats as stats

data_co2_emission = pd.read_csv('API_EN.ATM.CO2E.KT_DS2_en_csv_v2_4701269.csv',
                                skiprows=[0, 1, 2, 3])
data_access_to_electricity = pd.read_csv('API_EG.ELC.ACCS.ZS_DS2_en_csv_v2_4695288.csv',
                                         skiprows=[0, 1, 2, 3])

co2_data = data_co2_emission.iloc[259, 42:64]
electricity_data = data_access_to_electricity.iloc[259, 42:64]

dataframe = pd.DataFrame({'Access to electricity': electricity_data,
                   'Amount of CO2 emission': co2_data})

print(dataframe)

plt.plot(range(1998, 2020), co2_data)
plt.title('Amount of CO2 emitted in kilo tonnes')
plt.xlabel('Year')
plt.ylabel('kilo tonnes')
plt.show()

plt.plot(range(1998, 2020), electricity_data)
plt.title('Percentage of world population having access to electricity')
plt.xlabel('Year')
plt.ylabel('Percentage')
plt.show()

print('The mean value of percentage of world population having access to electricity is: '+
      str(np.mean(electricity_data)))
print('The mean value of amount of CO2 emitted is :' + str(np.mean(co2_data)))
print('The standard deviation of the world population data is :' +
      str(electricity_data.std()))
print('The standard deviation of the CO2 data is :' +
      str(co2_data.std()))

corr, pvalue = stats.pearsonr(co2_data, electricity_data)
print('The correlation between the amount of CO2 emission and the percentage '+
      'of world population having access to electricity is: ' + str(corr))
