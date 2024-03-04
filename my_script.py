# import pandas as pd

# mydataset = {
#   'cars': ["BMW", "Volvo", "Ford"],
#   'passings': [3, 7, 2]
# }
# # df = pd.DataFrame(mydataset)
# df=pd.DataFrame(mydataset,index=["day1", "day2", "day3"])
# print(df)
# y=df[['passings']]
# print(y)
# print(df)
# print(df.loc[0])


#import CSV files:-

# myvar = pd.DataFrame(mydataset)
# print(myvar)
# import pandas as pd
# df = pd.read_csv('data.csv')
# df.head()
# print(df.to_string())


import pandas as pd
# Creating a DataFrame from a dictionary
data = {'Name': ['Alice', 'Bob', 'Charlie', 'David'],
        'Age': [25, 30, 35, 28],
        'City': ['New York', 'San Francisco', 'Los Angeles', 'Chicago']}
df = pd.DataFrame(data)
df1= df[df['Age'] > 25]
print(df1)
