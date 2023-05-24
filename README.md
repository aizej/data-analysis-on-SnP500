# data-analysis-on-SnP500
some analysis on S&amp;P 500 about when was the right/wrong time to invest

WHY?:

Recently i became interested in investing and I wanted to see what was the propability of bad time to invest so i did little meaningles analisis on a dataset i found on the internet.


What im i looking for?:

1) times in the market where the price newer got lower than it was (good time to invest)
2) times where the price didnt go higier for long time             (bad time to invest)


The dataset:
Daily price from 1927-12-30 to 2020-11-04





The results:



Graph for just the 1) taking in to consideration all of the future prices:

![just](https://github.com/aizej/data-analysis-on-SnP500/assets/61479273/b6ee778c-4f81-4581-82e2-05f8b4be1b3d)

Logarithmic graph:

![just_log](https://github.com/aizej/data-analysis-on-SnP500/assets/61479273/dd4d42e1-13ac-42d3-aba5-036a17e9652d)


Graph that takes in to consideration just 1 year of future data:

![both](https://github.com/aizej/data-analysis-on-SnP500/assets/61479273/c0a2fc89-4033-4e95-b5ed-57230fdd5ac6)

Logarithmic graph:

![both_log](https://github.com/aizej/data-analysis-on-SnP500/assets/61479273/cd966d8d-bca0-42ff-b055-4633d83dfc0e)


green -times in the market where the price newer got lower than it was (good time to invest)
red -times where the price didnt go higier for long time               (bad time to invest)









These graphs are cool but what day in a month should I invest and does it make any diference?

What im i looking for?:

Are there days in the month that preform well in the folowing days or if there are days that constantly preform better even while looking further in to the future.

How have I analysed the data?:

1) From the dataset mentioned above, I pulled the average procentage growth from any given day to day+x (x is named convolution in the code)
2) I averaged over these growths
3) I averaged over all the days with the same date







