import numpy as np
import pandas as pd
pd.options.mode.chained_assignment = None  # default='warn'
import matplotlib.pyplot as plt
import seaborn as sns
netflix=pd.read_csv(r'C:\Users\timot\Desktop\Kagglicious\Netflix\netflix_titles.csv')
print(netflix)
netflix.count()

#movie count vs tv series count
sns.set (style="darkgrid")
count_type=sns.countplot(x="type", data=netflix, palette="Set2") # graph of count vs type
plt.show()


netflix_date=netflix['date_added'].dropna()
print(netflix_date)
netflix_date.count()


#movie ratings
plt.figure(figsize=(12,10))
sns.set(style="darkgrid")
movie_ratings=sns.countplot(x="rating", data=netflix,palette="Set2",
                            order=netflix['rating'].value_counts().index[0:15] ) # in descending order
plt.show()

#The largest count of movies are made with the 'TV-MA' rating."TV-MA" is a rating assigned by the
#TV Parental Guidelines to a television program that was designed for mature audiences only.
##Second largest is the 'TV-14' stands for content that may be deemed inappropriate
## for children younger than 14 years of age.

#yearly analysis

plt.figure(figsize=(12,10))
sns.set(style="darkgrid")
year_analysis=sns.countplot(y="release_year",data=netflix,palette="Set2",
                            order=netflix['release_year'].value_counts().index[0:15])
plt.show()
#2017 had the most movies released


#Top 10 movie content countries
countries={}
netflix['country']=netflix['country'].fillna('Unknown')
cou=list(netflix['country'])
for i in cou:
    #print(i)
    i=list(i.split(','))
    if len(i)==1:
        if i in list(countries.keys()):
            countries[i]+=1
        else:
            countries[i[0]]=1
    else:
        for j in i:
            if j in list(countries.keys()):
                countries[j]+=1
            else:
                countries[j]=1
countries_fin = {}
for country, no in countries.items():
    country = country.replace(' ', '')
    if country in list(countries_fin.keys()):
        countries_fin[country] += no
    else:
        countries_fin[country] = no

countries_fin = {k: v for k, v in sorted(countries_fin.items(), key=lambda item: item[1], reverse=True)}


plt.figure(figsize=(8,8))
ax = sns.barplot(x=list(countries_fin.keys())[0:10],y=list(countries_fin.values())[0:10])
ax.set_xticklabels(list(countries_fin.keys())[0:10],fontsize=5,rotation = 90)

plt.show()
#most number of movies were created in the US

from collections import Counter

genres=list(netflix['listed_in'])
gen=[]

for i in genres:
    i=list(i.split(','))
    for j in i:
        gen.append(j.replace(' ',""))
g=Counter(gen)
g = {k: v for k, v in sorted(g.items(), key=lambda item: item[1], reverse= True)}

fig, ax = plt.subplots()

fig = plt.figure(figsize = (10, 10))
x=list(g.keys())
y=list(g.values())
ax.vlines(x, ymin=0, ymax=y, color='green')
ax.plot(x,y, "o", color='maroon')
ax.set_xticks([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42])
ax.set_xticklabels(x, fontsize=3, rotation = 90)
ax.set_ylabel("Count of movies")
# set a title
ax.set_title("Genres");
plt.close()
plt.show()
# international movies, dramas and comedies were the top three genres of content on netflix

### TV shows with the highest number of seasons
netflix_fr=netflix[netflix['country']=='France']
nannef=netflix_fr.dropna()
import plotly.express as px
fig = px.treemap(nannef, path=['country','director'],
                  color='director', hover_data=['director','title'],color_continuous_scale='Purples')
fig.show()
# no director takes up the majority of the movies. perhaps more creative chances to other directors in charge.