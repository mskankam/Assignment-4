#6939121

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
Data=pd.read_csv('accidentData.csv')

f=np.array(Data['Fatality'])
s=np.array(Data['SevereInjury'])
m=np.array(Data['MinorInjury'])
Persons_affected=f+s+m
Data['PersonsAffected']=Persons_affected
Data.to_csv('accidentData.csv')

fig, ax1=plt.subplots(figsize=(7,5))
ax1.plot('Year','Fatality','C6',data=Data)
ax1.set_ylabel('Year against Fatality',color='C6')

ax2=ax1.twinx()
ax2.plot('Year','PersonsAffected','C3',data=Data)
ax2.set_ylabel('PersonsAffected',color='C3')

plt.title('Accident Data')

fig.savefig('plot.png')

plt.show()
