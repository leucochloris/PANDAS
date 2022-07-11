import pandas as pd
import matplotlib.pyplot as plt

# opened data file
df = pd.read_csv("IHME-GBD_2019_DATA-ff08d9bc-1.csv", delimiter=',', encoding='utf-8')




# make agregat table (y_axies - countries, x_axies - reason of death
df_pivot = df.pivot_table(values='val', index='year', columns='cause', aggfunc='mean', margins=False, dropna=True,
                          fill_value=None).plot(kind='line')
# print(df_pivot)



plt.ylabel('Death per 100 000 people')
plt.title('Death from some diseases')

plt.show()





'''
            # agregat table - mean and median of every desiase.
df_cause = (df.groupby('cause').agg({'year' : ['count'], 'val' : ['mean', 'median']}))
print(df_cause)
'''






'''
            # make agregat table (y_axies - countries, x_axies - reason of death
df_pivot = df.pivot_table(values='val', index='location', columns='cause', aggfunc='mean', margins=False, dropna=True, fill_value=None)
print(df_pivot)
'''






''' 
            # check - how many people die in Transport injuries
df_gender = df.groupby(['cause', 'sex']).agg({'val': ['mean', 'median']})  # total check
a = df_gender.xs('Transport injuries', level='cause')                      # exactly in Transport injuries
print(a)
'''





# print(df_cause['val']['mean'].sort_values(ascending=False))           # most popular reason of death
# print(df.groupby('cause').agg('mean'))  # agragat function - group by all val by CAUSE (reason of death)
# print(df.describe())                                                  # total statics
# print(df[df['location'] == 'Russian Federation'].nlargest(5, 'val'))  # sorted with the condition top 5 cause of death in Russian Feberaion
# print(df.sort_values(['val'], ascending = False))                     # sorted by 'val'
# print(df.head())                                                      # output 5 random values
