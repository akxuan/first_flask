import pandas as pd

file = 'input.csv'
df = pd.read_csv(file)
df.set_index('name', inplace=True)
total = df.iloc[:,1].sum()
print(total)

# create a localfile called result.txt
with open('result.txt', 'w') as f:
    f.write(str(total))

#total = df.sum().sum()