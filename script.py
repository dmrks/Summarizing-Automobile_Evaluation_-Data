import pandas as pd
import numpy as np

car_eval = pd.read_csv('car_eval_dataset.csv')
print(car_eval.head())

#1 What is the modal category? = Japan, Which country appears 4th most frequently? = US
print(car_eval.manufacturer_country.value_counts())

#2 What percentage of cars were manufactured in Japan? = 22,8%

print(car_eval.manufacturer_country.value_counts(normalize= True))

#3 Print out a list of the possible values for this variable = ['vhigh' 'med' 'low' 'high']

print(car_eval.buying_cost.unique())

#4 

buying_cost_categories = ['low', 'med' ,'high' ,'vhigh']

#5
car_eval.buying_cost = pd.Categorical(car_eval.buying_cost,buying_cost_categories, ordered = True )

#6 Median-Category = med
median_index= np.median(car_eval.buying_cost.cat.codes)
median_buying_cost = buying_cost_categories[int(median_index)]
print(median_buying_cost)

#7 small    0.339 / med      0.333 / big      0.328
print(car_eval.luggage.value_counts(normalize = True).head())

#8 small    0.339 / med      0.333 / big      0.328
print(car_eval.luggage.value_counts(normalize = True, dropna = False).head())

#9 small    0.339 / med      0.333 / big      0.328
print(car_eval.luggage.value_counts()/len(car_eval.luggage))

#10 Frequency = 246 of the cars have +5 Doors
frequency = (car_eval["doors"] == "5more").sum()
print(frequency)

#11 Prop = 0.246 = 24,6% of cars have +5 Doors
mean = (car_eval["doors"] == "5more").mean()
print(mean)
