import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('OliveYoung_Results_Preprocessed.csv')

# Divide data by popularity ranking intervals
num_of_intervals = 100
bins = range(0, len(df) + num_of_intervals + 1, num_of_intervals)
df['Interval'] = pd.cut(df['Popularity Ranking'], bins=bins, labels=False)

# Calculate average discount rate
discount_rate_avg = df.groupby('Interval')['Discount Rate'].mean()

#Draw the graph for average discount rate
plt.bar(range(0, len(discount_rate_avg) * num_of_intervals, num_of_intervals), discount_rate_avg.values, width=num_of_intervals, edgecolor='black', align='edge')
plt.bar(len(discount_rate_avg) * num_of_intervals, df[df['Popularity Ranking'] >= len(discount_rate_avg) * num_of_intervals]['Discount Rate'].mean(), width=num_of_intervals, edgecolor='black', align='edge')
plt.xticks(range(0, (len(discount_rate_avg) + 1) * num_of_intervals, num_of_intervals), [str(i) for i in range(0, (len(discount_rate_avg) + 1) * num_of_intervals, num_of_intervals)])
plt.xlabel('Popularity Ranking')
plt.ylabel('Average Discount Rate')
plt.title('Average Discount Rate by Popularity Ranking')
plt.show()

#----------------

#Calculate average current price
discount_rate_avg = df.groupby('Interval')['Current Price'].mean()

# Draw the graph for average current price
plt.bar(range(0, len(discount_rate_avg) * num_of_intervals, num_of_intervals), discount_rate_avg.values, width=num_of_intervals, edgecolor='black', align='edge')
plt.bar(len(discount_rate_avg) * num_of_intervals, df[df['Popularity Ranking'] >= len(discount_rate_avg) * num_of_intervals]['Current Price'].mean(), width=num_of_intervals, edgecolor='black', align='edge')
plt.xticks(range(0, (len(discount_rate_avg) + 1) * num_of_intervals, num_of_intervals), [str(i) for i in range(0, (len(discount_rate_avg) + 1) * num_of_intervals, num_of_intervals)])
plt.xlabel('Popularity Ranking')
plt.ylabel('Average Current Price')
plt.title('Average Current Price by Popularity Ranking')
plt.show()


#----------------

# Group popularity ranking into intervals of 100 and calculate the average number of reviews
reviews_by_ranking = df.groupby(df.index // 100)['Number of Reviews'].mean()

# # Plot the average number of reviews by popularity ranking
plt.plot(reviews_by_ranking, marker='o')
plt.xlabel('Popularity Ranking')
plt.ylabel('Average Number of Reviews')
plt.title('Average Number of Reviews by Popularity Ranking')

# Set the x-axis labels to rankings
plt.xticks(range(len(reviews_by_ranking)), [(i+1)*100 for i in range(len(reviews_by_ranking))])

plt.show()


