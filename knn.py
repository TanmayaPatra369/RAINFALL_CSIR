# -*- coding: utf-8 -*-
"""knn.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1ApOC7JIoKf4es8MeMCJGeKrynYEixuJQ
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from google.colab import drive
drive.mount('/content/drive')
df = pd.read_csv('/content/drive/MyDrive/POWER_Point_Daily_19810101_20240430_012d97N_077d59E_LST (1).csv')
df

df

"""# PREDICTION USING KNN

"""

df = df.drop(df.index[:19])
select = ['-BEGIN HEADER-','Unnamed: 1','Unnamed: 5']
ndf = df[select]
cols = ['year','dayno.','rainfall']
ndf.columns = cols
ndf.head()

ndf.loc[:, 'rainfall'] = ndf['rainfall'].astype(float)
ndf.loc[:, 'year'] = ndf['year'].astype(int)
total = ndf['rainfall'].sum()
total

ndf = ndf.groupby("year")['rainfall'].sum()

ndf = ndf.reset_index()

ndf = ndf.head(43)
ndf

"""# ANNUAL RAINFALL"""

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsRegressor
from sklearn.metrics import mean_squared_error
X = ndf[['year']]
y = ndf['rainfall']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)
k = 5
knn_model = KNeighborsRegressor(n_neighbors=k)
knn_model.fit(X_train_scaled, y_train)
y_pred = knn_model.predict(X_test_scaled)
y_pred_train = knn_model.predict(X_train_scaled)

result_df_train_knn = pd.DataFrame({'Year': X_train.values.flatten(), 'Actual Rainfall': y_train, 'Predicted Rainfall': y_pred_train})
result_df_train_knn['Absolute Error'] = abs(result_df_train_knn['Actual Rainfall'] - result_df_train_knn['Predicted Rainfall'])
result_df_train_knn

from sklearn.metrics import r2_score

r2 = r2_score(y_test, y_pred)
print(f"R-squared: {r2}")

import pandas as pd

predicted_df = pd.DataFrame({
    'Year': X_test['year'],
    'Predicted Rainfall': y_pred,
'Actual Rainfall': y_test
    })
predicted_df

predicted_df['Absolute Error'] = abs(predicted_df['Predicted Rainfall'] - predicted_df['Actual Rainfall'])
predicted_df

result_combined = pd.concat([result_df_train_knn, predicted_df])
result_combined['Percentage Error'] = (result_combined['Absolute Error'] / result_combined['Actual Rainfall']) * 100
result_combined

result_combined['Percentage Error'].mean()

# prompt: Using dataframe result_combined: absolute error vs year bar graph

import altair as alt

chart = alt.Chart(result_combined).mark_bar().encode(
    x = 'Year',
    y = 'Absolute Error',

).properties(
    title = 'Absolute Error vs Year'
)

chart

result_combined['Absolute Error'].mean()

"""# JJAS ANALYSIS"""

jjas_df = pd.read_csv('/content/drive/MyDrive/POWER_Point_Daily_19810101_20240430_012d97N_077d59E_LST (1).csv')

select = ['-BEGIN HEADER-','Unnamed: 1','Unnamed: 5']
ndf = df[select]
cols = ['year','dayno.','rainfall']
ndf.columns = cols
ndf.head()
ndf.loc[:, 'rainfall'] = ndf['rainfall'].astype(float)
ndf.loc[:, 'year'] = ndf['year'].astype(int)
total = ndf['rainfall'].sum()
ndf['dayno.'] = ndf['dayno.'].astype(int)
selected_days = ndf[(ndf['dayno.'] >= 150) & (ndf['dayno.'] <= 250)]
jjs_rain_sum = selected_days.groupby('year')['rainfall'].sum().reset_index()
jjs_rain_sum

X = jjs_rain_sum[['year']]
y = jjs_rain_sum['rainfall']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)
k = 5
knn_model = KNeighborsRegressor(n_neighbors=k)
knn_model.fit(X_train_scaled, y_train)
y_pred = knn_model.predict(X_test_scaled)
y_pred_train = knn_model.predict(X_train_scaled)

X_train = X_train.values.flatten()
result_df_train = pd.DataFrame({'Year': X_train, 'Actual Rainfall': y_train, 'Predicted Rainfall': y_pred_train})
result_df_train['Absolute Error'] = abs(result_df_train['Actual Rainfall'] - result_df_train['Predicted Rainfall'])
result_df_train

predicted_df = pd.DataFrame({
    'Year': X_test['year'],
    'Actual Rainfall': y_test,
    'Predicted Rainfall': y_pred
})

predicted_df['Absolute Error'] = abs(predicted_df['Predicted Rainfall'] - predicted_df['Actual Rainfall'])
predicted_df

combine_jjas = pd.concat([result_df_train, predicted_df])
combine_jjas['Percentage Error'] = (combine_jjas['Absolute Error'] / combine_jjas['Actual Rainfall']) * 100
combine_jjas

from matplotlib import pyplot as plt
import seaborn as sns
def _plot_series(series, series_name, series_index=0):
  palette = list(sns.palettes.mpl_palette('Dark2'))
  xs = series['Year']
  ys = series['Predicted Rainfall']

  plt.plot(xs, ys, label=series_name, color=palette[series_index % len(palette)])

fig, ax = plt.subplots(figsize=(10, 5.2), layout='constrained')
df_sorted = combine_jjas.sort_values('Year', ascending=True)
_plot_series(df_sorted, '')
sns.despine(fig=fig, ax=ax)
plt.xlabel('Year')
_ = plt.ylabel('Predicted Rainfall')
plt.title('Predicted by KNN')
plt.legend()
plt.grid(True)
plt.show()

import matplotlib.pyplot as plt
import seaborn as sns

def _plot_series(series, series_name, series_index=0):
    palette = list(sns.palettes.mpl_palette('Dark2'))
    xs = series['Year']
    ys = series['Actual Rainfall']

    plt.bar(xs, ys, label=series_name, color=palette[series_index % len(palette)])

fig, ax = plt.subplots(figsize=(10, 5.2), layout='constrained')

df_sorted = combine_jjas.sort_values('Year', ascending=True)

_plot_series(df_sorted, 'Actual Rainfall')

sns.despine(fig=fig, ax=ax)
plt.xlabel('Year')
plt.ylabel('Actual Rainfall')
plt.title('Actual Rainfall Over Years')
plt.legend()
plt.grid(True)
plt.show()

import matplotlib.pyplot as plt
import seaborn as sns

def _plot_series(series, series_name, series_index=0):
    palette = list(sns.palettes.mpl_palette('Dark2'))
    xs = series['Year']
    ys = series['Percentage Error']

    plt.bar(xs, ys, label=series_name, color=palette[series_index % len(palette)])

fig, ax = plt.subplots(figsize=(10, 5.2), layout='constrained')

df_sorted = combine_jjas.sort_values('Year', ascending=True)

_plot_series(df_sorted, 'Percentage Error')

sns.despine(fig=fig, ax=ax)
plt.xlabel('Year')
plt.ylabel('Percentage Error')
plt.title('Percentage Error Over Years')
plt.legend()
plt.grid(True)
plt.show()

combine_jjas['Percentage Error'].mean()

"""# JUNE RAINFALL

#percent error vs year bar
#predicted rain vs year plot
#actual rain vs year bar
"""

ndf

select = ['-BEGIN HEADER-','Unnamed: 1','Unnamed: 5']
ndf = df[select]
cols = ['year','dayno.','rainfall']
ndf.columns = cols
ndf.head()

ndf.loc[:, 'rainfall'] = ndf['rainfall'].astype(float)
ndf.loc[:, 'year'] = ndf['year'].astype(int)
total = ndf['rainfall'].sum()

ndf['dayno.'] = ndf['dayno.'].astype(int)
selected_days = ndf[(ndf['dayno.'] >= 150) & (ndf['dayno.'] <= 180)]
june_rain_sum = selected_days.groupby('year')['rainfall'].sum().reset_index()
june_rain_sum

X = june_rain_sum[['year']]
y = june_rain_sum['rainfall']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)
k = 5
knn_model = KNeighborsRegressor(n_neighbors=k)
knn_model.fit(X_train_scaled, y_train)
y_pred = knn_model.predict(X_test_scaled)
y_pred_train = knn_model.predict(X_train_scaled)

result_train_june = pd.DataFrame({'Year': X_train.values.flatten(), 'Actual Rainfall': y_train, 'Predicted Rainfall': y_pred_train})
result_train_june['Error'] = abs(result_train_june['Actual Rainfall'] - result_train_june['Predicted Rainfall'])
result_train_june

predicted_df = pd.DataFrame({
    'Year': X_test['year'],
    'Actual Rainfall': y_test,
    'Predicted Rainfall': y_pred
})
predicted_df['Error'] = abs(predicted_df['Predicted Rainfall'] - predicted_df['Actual Rainfall'])
predicted_df

combine_june = pd.concat([result_train_june, predicted_df])
combine_june['Percentage Error'] = (combine_june['Error'] / combine_june['Actual Rainfall']) * 100
combine_june

import matplotlib.pyplot as plt
import seaborn as sns

def _plot_series(series, series_name, series_index=0):
    palette = list(sns.palettes.mpl_palette('Dark2'))
    xs = series['Year']
    ys = series['Percentage Error']

    plt.bar(xs, ys, label=series_name, color=palette[series_index % len(palette)])

fig, ax = plt.subplots(figsize=(10, 5.2), layout='constrained')

df_sorted = combine_june.sort_values('Year', ascending=True)

_plot_series(df_sorted, 'Percentage Error')

sns.despine(fig=fig, ax=ax)
plt.xlabel('Year')
plt.ylabel('Percentage Error')
plt.title('Percentage Error Over Years')
plt.legend()
plt.grid(True)
plt.show()

import matplotlib.pyplot as plt
import seaborn as sns

def _plot_series(series, series_name, series_index=0):
    palette = list(sns.palettes.mpl_palette('Dark2'))
    xs = series['Year']
    ys = series['Actual Rainfall']

    plt.bar(xs, ys, label=series_name, color=palette[series_index % len(palette)])

fig, ax = plt.subplots(figsize=(10, 5.2), layout='constrained')

df_sorted = combine_june.sort_values('Year', ascending=True)

_plot_series(df_sorted, 'Actual Rainfall')

sns.despine(fig=fig, ax=ax)
plt.xlabel('Year')
plt.ylabel('Actual Rainfall')
plt.title('Actual Rainfall Over Years')
plt.legend()
plt.grid(True)
plt.show()

from matplotlib import pyplot as plt
import seaborn as sns
def _plot_series(series, series_name, series_index=0):
  palette = list(sns.palettes.mpl_palette('Dark2'))
  xs = series['Year']
  ys = series['Predicted Rainfall']

  plt.plot(xs, ys, label=series_name, color=palette[series_index % len(palette)])

fig, ax = plt.subplots(figsize=(10, 5.2), layout='constrained')
df_sorted = combine_june.sort_values('Year', ascending=True)
_plot_series(df_sorted, '')
sns.despine(fig=fig, ax=ax)
plt.xlabel('Year')
_ = plt.ylabel('Predicted Rainfall')
plt.title('Predicted by KNN')
plt.legend()
plt.grid(True)
plt.show()

combine_june['Error'].mean()

"""# JULY RAINFALL"""

ndf['dayno.'] = ndf['dayno.'].astype(int)
selected_days = ndf[(ndf['dayno.'] >= 180) & (ndf['dayno.'] <= 210)]
july_rain_sum = selected_days.groupby('year')['rainfall'].sum().reset_index()
july_rain_sum

X = july_rain_sum[['year']]
y = july_rain_sum['rainfall']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)
k = 5
knn_model = KNeighborsRegressor(n_neighbors=k)
knn_model.fit(X_train_scaled, y_train)
y_pred = knn_model.predict(X_test_scaled)
y_pred_train = knn_model.predict(X_train_scaled)

result_train_july = pd.DataFrame({'Year': X_train.values.flatten(), 'Actual Rainfall': y_train, 'Predicted Rainfall': y_pred_train})
result_train_july['Error'] = abs(result_train_july['Actual Rainfall'] - result_train_july['Predicted Rainfall'])
result_train_july

predicted_df = pd.DataFrame({
    'Year': X_test['year'],
    'Actual Rainfall': y_test,
    'Predicted Rainfall': y_pred
})
predicted_df['Error'] = abs(predicted_df['Predicted Rainfall'] - predicted_df['Actual Rainfall'])
predicted_df

combine_july = pd.concat([result_train_july, predicted_df])
combine_july['Percentage Error'] = (combine_july['Error'] / combine_july['Actual Rainfall']) * 100
combine_july.head()

# prompt: Using dataframe combine_july: predicted values vs year plot

import altair as alt

chart = alt.Chart(combine_july).mark_line().encode(
    x='Year',
    y='Predicted Rainfall'
).properties(
    title='Predicted Rainfall vs Year'
)

chart

import altair as alt

chart = alt.Chart(combine_july).mark_bar().encode(
    x = 'Year:N',
    y = 'Actual Rainfall:Q'
)

chart

import altair as alt

alt.Chart(combine_july).mark_bar().encode(
    x='Year',
    y='Percentage Error',
    color='Year'
).properties(width=600)

combine_july['Percentage Error'].mean()

"""# AUGUST RAINFALL"""

ndf['dayno.'] = ndf['dayno.'].astype(int)
selected_days = ndf[(ndf['dayno.'] >= 210) & (ndf['dayno.'] <= 240)]
july_rain_sum = selected_days.groupby('year')['rainfall'].sum().reset_index()
july_rain_sum

X = july_rain_sum[['year']]
y = july_rain_sum['rainfall']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)
k = 5
knn_model = KNeighborsRegressor(n_neighbors=k)
knn_model.fit(X_train_scaled, y_train)
y_pred = knn_model.predict(X_test_scaled)
y_pred_train = knn_model.predict(X_train_scaled)

result_train_august = pd.DataFrame({'Year': X_train.values.flatten(), 'Actual Rainfall': y_train, 'Predicted Rainfall': y_pred_train})
result_train_august['Error'] = abs(result_train_august['Actual Rainfall'] - result_train_august['Predicted Rainfall'])
result_train_august

predicted_df = pd.DataFrame({
    'Year': X_test['year'],
    'Actual Rainfall': y_test,
    'Predicted Rainfall': y_pred
})
predicted_df['Error'] = abs(predicted_df['Predicted Rainfall'] - predicted_df['Actual Rainfall'])
predicted_df

combine_august = pd.concat([result_train_august, predicted_df])
combine_august['Percentage Error'] = (combine_august['Error'] / combine_august['Actual Rainfall']) * 100
combine_august.head()

import altair as alt

chart = alt.Chart(combine_august).mark_line().encode(
    x='Year',
    y='Predicted Rainfall'
).properties(
    title='Predicted Rainfall vs Year'
)
chart

import altair as alt

bar = alt.Chart(combine_august).mark_bar().encode(
    x = 'Year:N',
    y = 'Actual Rainfall:Q'
).properties(
    width=600
)

bar

import altair as alt
chart = alt.Chart(combine_august).mark_bar().encode(
    x = alt.X('Year:N', title='Year'),
    y = alt.Y('Percentage Error:Q', title='Percentage Error')
).properties(
    width=600
)
chart

combine_august['Percentage Error'].mean()



"""# SEPTEMBER ANALYSIS

"""

ndf['dayno.'] = ndf['dayno.'].astype(int)
selected_days = ndf[(ndf['dayno.'] >= 240) & (ndf['dayno.'] <= 270)]
sep_rain_sum = selected_days.groupby('year')['rainfall'].sum().reset_index()
sep_rain_sum

X = sep_rain_sum[['year']]
y = sep_rain_sum['rainfall']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)
k = 5
knn_model = KNeighborsRegressor(n_neighbors=k)
knn_model.fit(X_train_scaled, y_train)
y_pred = knn_model.predict(X_test_scaled)
y_pred_train = knn_model.predict(X_train_scaled)

result_train_sep = pd.DataFrame({'Year': X_train.values.flatten(), 'Actual Rainfall': y_train, 'Predicted Rainfall': y_pred_train})
result_train_sep['Error'] = abs(result_train_sep['Actual Rainfall'] - result_train_sep['Predicted Rainfall'])
result_train_sep

predicted_df = pd.DataFrame({
    'Year': X_test['year'],
    'Actual Rainfall': y_test,
    'Predicted Rainfall': y_pred
})
predicted_df['Error'] = abs(predicted_df['Predicted Rainfall'] - predicted_df['Actual Rainfall'])
predicted_df

combine_sep = pd.concat([result_train_sep, predicted_df])
combine_sep['Percentage Error'] = (combine_sep['Error'] / combine_sep['Actual Rainfall']) * 100
combine_sep.head()

import altair as alt

chart = alt.Chart(combine_sep).mark_line().encode(
    x='Year',
    y='Predicted Rainfall'
).properties(
    title='Predicted Rainfall vs Year'
)
chart

import altair as alt

bar = alt.Chart(combine_sep).mark_bar().encode(
    x = 'Year:N',
    y = 'Actual Rainfall:Q'
).properties(
    width=600
)

bar

import altair as alt
chart = alt.Chart(combine_sep).mark_bar().encode(
    x = alt.X('Year:N', title='Year'),
    y = alt.Y('Percentage Error:Q', title='Percentage Error')
).properties(
    width=600
)
chart

combine_sep['Percentage Error'].mean()
