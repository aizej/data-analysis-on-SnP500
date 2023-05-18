import matplotlib.pyplot as plt
import numpy as np
import time

years_p_months_p_days = []
years = []
months = []
days = []
amounts = []
with open("SPX.csv","r") as data:
    for index, line in enumerate(data):
        try:
            date,Open,High,Low,Close,Adj_Close,Volume = line.split(',')
            year,month,day = date.split("-")
            years.append(int(year))
            months.append(int(month))
            days.append(int(day))
            years_p_months_p_days.append((int(year)+((int(month)-1)/12))+((int(day)-1)/365))
            amounts.append(float(Low))
        except Exception as e:
            print(e)
            print("propably just first line")
            print(f"curr line: {line}")



yes = []
colors = []
sizes = []
start=time.time()
show_every=100
convolution_value = 35600
for index,amount in enumerate(amounts):
    if index%show_every==0:
        end = time.time()-start
        start = time.time()
        if convolution_value > 25000:
            print(f"{round(((1-((((index/len(amounts))**2)/2-(index/len(amounts))+0.5)*2))*100),2)}%  {int(show_every*end*((((index/len(amounts))**2)/2-(index/len(amounts))+0.5)*2))}s till end")  #x*(n-x)is complexity so integral to get its time = x-(x**2)/2 + any real number
        else:
            print(f"{round(((index/len(amounts))*100),2)}% {int(2*show_every*end*(1-(index/len(amounts))))}s till end")
    for amount_tested in amounts[index+1:index+convolution_value+1]:
        yes.append(amount<amount_tested)
    if all(yes):
        colors.append("g")
        sizes.append(20)

    elif all(_ is False for _ in yes):
        colors.append("r")
        sizes.append(20)

    else:
        colors.append("k")
        sizes.append(1)
        
    yes = []

plt.style.use('_mpl-gallery')
fig, ax = plt.subplots()


#amounts = np.log(amounts)
ax.scatter(years_p_months_p_days, amounts,c=colors,s=sizes)
plt.show()
