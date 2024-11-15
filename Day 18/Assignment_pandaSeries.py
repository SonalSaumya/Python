import numpy as np
import pandas as pd


months=['jan','feb','march','april','may','june','july','august','sept','oct','nov','dec']

values = np.random.randint(1000,5000,12)

m_exp = pd.Series(values, index=months)

#Series and dtype
print(m_exp)

print("sum : ",m_exp.sum())
print("mean : ",m_exp.mean())
print("minimum : ",m_exp.min())
print("maximum : ",m_exp.max())

print("Values at march",m_exp.loc['march'])

print("\nvalues from jan to march\n",m_exp.loc['jan':'march'])

res = m_exp['values'] > 2000
print(res)





