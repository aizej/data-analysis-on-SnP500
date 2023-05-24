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

What was my premise?:

I was looking for high short term growth in the last days of the month
My reasoning: A lot of people get paid at the end of the month or at the very begining of the month 31. or 1. and so they propably invest in the same time they get their paychecks
thats why the market should avberagely increase in value from the 25 th to 5 becouse a lot of people invest.

How have I analysed the data?:

1) From the dataset mentioned above, I pulled the average procentage growth from any given day to day+x (x is named convolution in the code)
2) I averaged over these growths
3) I averaged over all the days with the same date
4) I substacted the mean average to get cleaner representation on the diference of growths between days (snp500 tends to grow :O )

The results:

From 1927-12-30 to 2020-11-04  x (named convolution in the code) = 10 days:

![all](https://github.com/aizej/data-analysis-on-SnP500/assets/61479273/c9d00238-ad0e-4915-aefd-fba6e87d680d)

WOW i was compleatly right!
lets chck if this patern stays even for long term investments:

From 1927-12-30 to 2020-11-04  x (named convolution in the code) = 100 days:

![all_100](https://github.com/aizej/data-analysis-on-SnP500/assets/61479273/59fd3a2f-1902-4acc-b844-1af41383aab5)

wow it stays!
does this mean we can get rich if we invest every 27th?

sadly no :(

If we look at the data from 2000 this patern starts to disapear:

From 2000-1-1 to 2020-11-04  x (named convolution in the code) = 10 days:

![2000_10](https://github.com/aizej/data-analysis-on-SnP500/assets/61479273/297a91db-dc31-4823-8a08-46a4e88b1c2c)

From 2000-1-1 to 2020-11-04  x (named convolution in the code) = 100 days:

![2000_100](https://github.com/aizej/data-analysis-on-SnP500/assets/61479273/b9abb977-c83f-41c3-9bda-f1070b80381a)


and then by year 2010 its almost gone:

From 2010-1-1 to 2020-11-04  x (named convolution in the code) = 10 days:

![2010_10](https://github.com/aizej/data-analysis-on-SnP500/assets/61479273/c1f3b6a0-f8c6-4453-8d35-43712e66bca6)

From 2010-1-1 to 2020-11-04  x (named convolution in the code) = 100 days:

![2010_100](https://github.com/aizej/data-analysis-on-SnP500/assets/61479273/2cc84b07-da4c-4e2f-9e9e-2ba05dbcf448)









