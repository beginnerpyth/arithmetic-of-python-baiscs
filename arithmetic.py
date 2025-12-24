
#product = 1
#for x in range(10):
    #if (x != 0):
       # product = product * x 
    #print(product)

    #print("hello")
#for x in range(10):
    #print(x)
#x = int(input("enter a num:"))
#if x % 2 != 0:
 #   print("the number is odd")
#else:
#    print("the number is even")

import pandas as pd

df = pd.read_csv('pand.csv')
print(df)
new_df = df.dropna()
print(new_df)

import pandas as pd

df = pd.read_csv('pand.csv')

df.dropna(inplace = True)
df.fillna("caloriers:130")
print(df)