import numpy as np 
import pandas as pd 
from pandas import DataFrame

jobkorea=pd.read_excel('result.xlsx',sep=',',header=None)
print(jobkorea.info())
print(jobkorea.head())
