import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns
movie_data = pd.read_csv('data (1).csv')
rows, col = movie_data.shape
print('We have {} total entries of movies and {} columns/features of it.'.format(rows-1, col))
del_col = [ 'id', 'imdb_id', 'popularity', 'budget_adj', 'revenue_adj', 'homepage', 'keywords', 'overview', 'production_companies', 'vote_count', 'vote_average']
movie_data = movie_data.drop(del_col, 1)
movie_data.head(3)
movie_data.drop_duplicates(keep = 'first', inplace = True)
rows, col = movie_data.shape
print('We now have {} total entries of movies and {} columns/features of it.'.format(rows-1, col))
check_row=['budget','revenue']
movie_data[check_row] = movie_data[check_row].replace(0, np.NAN)
movie_data[check_row] = movie_data[check_row].replace(0, np.NaN)
movie_data.dropna(subset = check_row, inplace = True)
rows, col = movie_data.shape
print('After cleaning, we now have only {} entries of movies.'.format(rows-1))
movie_data['runtime']=movie_data['runtime'].replace(0, np.NaN)
movie_data.release_date=pd.to_datetime(movie_data['release_date'])
movies_data=movie_data.head(3)
movies_data=movie_data.dtypes
change_coltype=['budget','revenue']
movie_data[change_coltype]=movie_data[change_coltype].applymap(np.int64)
moviesdata=movie_data.dtypes
movie_data.rename(columns={'budget' : 'budget_(in_us-dollars)', 'revenue':'revenue_(in_us-dollars)'}, inplace = True)
movie_data.insert(2,'profit_(in_us-dollars)', movie_data['revenue_(in_us-dollars)'] - movie_data['budget_(in_us-dollars)'])
movie_data['profit_(in_us-dollars)']=movie_data['profit_(in_us-dollars)'].apply(np.int64)
ans=movie_data.head(2)
def highest_lowest(column_name):
    highest_id = movie_data[column_name].idxmax()
    highest_details = pd.DataFrame(movie_data.loc[highest_id])
    lowest_id = movie_data[column_name].idxmin()
    lowest_details = pd.DataFrame(movie_data.loc[lowest_id])
    two_in_one_data = pd.concat([highest_details, lowest_details], axis = 1)
    return two_in_one_data
ans2=highest_lowest('profit_(in_us-dollars)')
ans3=highest_lowest('runtime')
ans4=highest_lowest('revenue_(in_us-dollars)')
def average_func(column_name):
 return movie_data[column_name].mean()
ans5=average_func('runtime')
sns.set_style('darkgrid')
plt.rc('xtick',labelsize=10)
plt.rc('ytick',labelsize=10)
plt.figure(figsize=(9,6),dpi=100)
plt.xlabel('Runtime of movies',fontsize=15)
plt.ylabel('number of movies',fontsize=15)
plt.title('Runtime distribution of all movies', fontsize=18)
plt.hist(movie_data['runtime'],rwidth=0.9, bins=31)
plt.show()
plt.figure(figsize=(9,7), dpi = 105)
sns.boxplot(x=movie_data['runtime'],linewidth = 3)
plt.show()
a6=movie_data['runtime'].describe()
profit_each_year=movie_data.groupby('release_year')['profit_(in_us-dollars)'].sum()
plt.figure(figsize=(12,6),dpi=150)
plt.xlabel('release year of movies', fontsize=12)
plt.ylabel('prifit in us dollars', fontsize=12)
plt.title('plot of total profit in each year')
plt.plot(profit_each_year)
plt.show()
a7=profit_each_year.idxmax()
a8=profit_each_year.tail()
profit_each_year=pd.DataFrame()
profit_movie_data=movie_data[movie_data['profit_(in_us-dollars)'] > 50000000]
def profit_avg_fuc(column_name):
    return profit_movie_data[column_name].mean()
a9=profit_avg_fuc('runtime')
a10=profit_avg_fuc('budget_(in_us-dollars)')
a11=profit_avg_fuc('revenue_(in_us-dollars)')
a12=profit_avg_fuc('profit_(in_us-dollars)')
a13=profit_movie_data['director'].value_counts()
def extract_data(column_name):
    all_data=profit_movie_data[column_name].str.cat(sep ='|')
    all_data=pd.Series(all_data.split('|'))
    count=all_data.value_counts(ascending=False)
    return count
a14=extract_data('director')
cast_count=extract_data('cast')
genre_most_popular=extract_data('genres')
genre_most_popular.sort_values(ascending=True, inplace=True)
ax = genre_most_popular.plot.barh(color = '#007482', fontsize = 15)
ax.set(title = 'The Most filmed genres')
ax.set_xlabel('Number of Movies', color = 'g', fontsize = '18')
ax.figure.set_size_inches(12, 10)
plt.show()














