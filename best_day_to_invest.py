import matplotlib.pyplot as plt
import numpy as np
import time


convoluted_day_average = [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]
convolution = 10
for time_skip_value in range(convolution):
    print(time_skip_value)

    years_p_months_p_days = []
    years = []
    months = []
    days = []
    amounts = []

    data_array =[]
    day_amounts = [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]
    with open("SPX.csv","r") as data:
        for index, line in enumerate(data):
            data_array.append(line)
    for index, line in enumerate(data_array):
        try:
            date,Open,High,Low,Close,Adj_Close,Volume = line.split(',')
            year,month,day = date.split("-")
            if int(year)>2010 and index+time_skip_value+1< len(data_array):
                years.append(int(year))
                months.append(int(month))
                days.append(int(day))
                date_future,Open_future,High_future,Low_future,Close_future,Adj_Close_future,Volumedata_future = data_array[index+time_skip_value+1].split(',')

                day_amounts[int(day)-1].append((float(Close_future)-float(Close))/float(Close))
                years_p_months_p_days.append((int(year)+((int(month)-1)/12))+((int(day)-1)/365))
                amounts.append(float(Low))
        except Exception as e:
            print(e)
            print("propably just first line")
            print(f"curr line: {line}")



    day_amounts_average = []
    for day in day_amounts:
        day_amounts_average.append(sum(day)/len(day))

    for index, average in enumerate(day_amounts_average):
        convoluted_day_average[index].append(average)

averaged_convoluted_day_average = []
for day in convoluted_day_average:
    averaged_convoluted_day_average.append(sum(day)/len(day))


moving_average = sum(averaged_convoluted_day_average)/len(averaged_convoluted_day_average)


normalised_averaged_convoluted_day_average = []
for not_normalised_value in averaged_convoluted_day_average:
    normalised_averaged_convoluted_day_average.append(not_normalised_value-moving_average)

courses = range(len(normalised_averaged_convoluted_day_average))
values = normalised_averaged_convoluted_day_average
  
fig = plt.figure(figsize = (10, 5))
 
# creating the bar plot
plt.bar(courses, values, color ='maroon',
        width = 0.4)

plt.show()
