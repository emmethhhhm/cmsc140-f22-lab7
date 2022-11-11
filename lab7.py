import pandas as pd 
temps = pd.read_csv("city_temperature.csv")
print (temps) 


grouptemps = temps.groupby(["Region"])
indices = grouptemps["AvgTemperature"].idxmax()
print (indices)
indices = temps.loc[indices]
print (indices)

indices.to_csv("citytempmaximums.csv")