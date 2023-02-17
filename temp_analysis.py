/*
In this python code, using the pandas, seaborn and matplotlib libraries, the temperatures of the countries were analyzed on a sample dataset. 
A concrete visualization of the analysis made using the seaborn and matplotlib visualization libraries is provided.
*/
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("data.csv",parse_dates=["dt"])
df_prepared = df.dropna(axis=0,how="any")
#result = df_prepared["Country"].value_counts() # Country dında verileri gruplandırır sayısını döndürür.
#result = df_prepared[df_prepared["Country"] == "Turkey"] # sadece Country kolonunun Turkey olanları getir.
#result = df_prepared[(df_prepared["Country"] == "Turkey") | (df_prepared["Country"] == "Brazil") ] # Country kolonundaki değer Turkey yada Brazil olanları getir
#result = df_prepared[(df_prepared["Country"] == "Turkey") & (df_prepared["AverageTemperature"] > 30) ] # Country kolonu Turkey olan ve Avaregetempreture kolonu 30 dan büyük olan verileri getir
data_selected = df_prepared[df_prepared["Country"].isin(["Turkey","Brazil","United States"])] #isin() eğer bu değer varsa getir.
#result = data_selected.groupby(by="Country").mean() # Country kolonuna göre ortalama al
#result = data_selected.groupby(by="Country").agg(["min","mean","max"])  # # Country kolonuna göre min , ortalam ve max değeri al. agg fonksiyonu istenilen değerlri bir liste içersiinde getirir.

# Turkiyede tarih ve şehirlerden bağımsız olarak ortalama sicaklıkları göstermek
"""
tr_avg_temps = data_selected[data_selected["Country"] == "Turkey"]["AverageTemperature"]
br_avg_temps = data_selected[data_selected["Country"] == "Brazil"]["AverageTemperature"]
sns.distplot(tr_avg_temps)
sns.distplot(br_avg_temps)

sns.set_style("whitegrid") # gridleri ekliyoruz.
plt.figure(figsize=(15,5)) # boyutları ayarlıyoruz
countries = data_selected["Country"].unique()
colors = ["blue","orange","green"]
for color,country in zip(colors,countries):
      data=data_selected[data_selected["Country"] ==country]["AverageTemperature"]
      countries_mean = data_selected[data_selected["Country"] ==country]["AverageTemperature"].mean()
      plt.vlines(countries_mean,0, 0.16,colors=color) # virtical line oluşturmak . iki argüman alır ymin ve ymax
      sns.distplot(data)
plt.legend(countries) # hangi rengin hangi ülkeyi temsil ettiğini görmek için kullanıyoruz

# tam otomatikleştirme
columns = data_selected.columns[1:3]
countries = data_selected["Country"].unique()
plt.figure(figsize=(15,5))
for column in columns:
    plt.figure(figsize=(15,5))
    for country in countries:
        sns.displot(data_selected[data_selected["Country"] ==country][column])
    
    plt.show()
"""
# scatterplot ile analiz

tr_data = data_selected[(data_selected["Country"]=="Turkey") & (data_selected["dt"]>"01.01.1900")]
plt.figure(figsize=(15,5))
#sns.scatterplot(x="dt",y="AverageTemperature",data=tr_data,hue="AverageTemperature") # hue argümanı sicaklıkların artış ve azalışlarına göre renklendirme yapıyor.

# tarihlere göre gruplandırma
tr_data_means=tr_data.groupby(tr_data["dt"].dt.to_period("Y")).mean() # tarihi yıllara göre gruplamak
tr_data_means = tr_data_means.reset_index() # indexi kolon moduna geçirir ve kolona yeni bir indexleme yapar
tr_data_means["dt"]=tr_data_means["dt"].astype("string").astype("datetime64") # datetime veri tipinde olmayan dt yi datetime veri tipine dönüştürdük.
plt.figure(figsize=(15,5))
#sns.lineplot(x="dt",y="AverageTemperature",data=tr_data_means)

# 3 ülke için yıllara göre ortalama sicaklık grafiği

columns = data_selected.columns[1:3]
countries = data_selected["Country"].unique()
plt.figure(figsize=(15,5))

data_1900 = data_selected[data_selected["dt"]>"01.01.1900"]
data_mean = data_1900.groupby(["Country",data_1900["dt"].dt.to_period("Y")]).mean()
data_means = data_mean.reset_index() # indexi kolon moduna geçirir ve kolona yeni bir indexleme yapar
data_means["dt"]=data_means["dt"].astype("string").astype("datetime64") # datetime veri tipinde olmayan dt yi datetime veri tipine dönüştürdük.
for col in data_means.columns[2:4]:
    plt.figure(figsize=(15,5))
    for ulke in data_means["Country"].unique():
        data = data_means[data_means["Country"]==ulke]
        sns.lineplot(x="dt",y=col,data=data)
        plt.legend(data_means["Country"].unique())
    plt.show()
