from sklearn.datasets import load_breast_cancer
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report,confusion_matrix
import numpy as np

loadData = load_breast_cancer()
df = pd.DataFrame(loadData.data, columns=loadData.feature_names)
df['Result'] = pd.DataFrame(loadData.target)
print("\nLoading DataSet Of Breast Cancer Analysis...\n")
print(df.head())
print("\nPlotting Pair Plots For The DataSet.\nPlease Wait...")
saveFigure = sns.pairplot(df, vars=loadData.feature_names, hue='Result', diag_kind='kde', plot_kws={'alpha': 0.6, 's': 80, 'edgecolor' : 'k'}, height=2)
saveFigure._legend.get_title().set_fontsize(20)
plt.show()
plt.savefig("PairPlot.png")
print("Saved the pair plots extracted from data.\n")
x_train, x_test, y_train, y_test = train_test_split(df.drop('Result', axis=1), loadData.target, test_size=0.3, random_state=28)
KnnModel = KNeighborsClassifier(n_neighbors=1)
KnnModel.fit(x_train,y_train)
print("Setting Up The Knn Model With K value = 3(No. of neighbours)")
predictions = KnnModel.predict(x_test)
print("We Have Confusion Matrix as :\n")
print(confusion_matrix(y_test, predictions),"\n\nAnd Classification report as :\n")
print(classification_report(y_test, predictions))
print("Let's plot the Elbow Method graph for finding the correct value of K.\nPlotting...")

error_rate = []
for k in range(1,21):
    TestKnnModel = KNeighborsClassifier(n_neighbors=k)
    TestKnnModel.fit(x_train, y_train)
    TestPredictions = TestKnnModel.predict(x_test)
    error_rate.append(np.mean(y_test != TestPredictions))
plt.figure(figsize=(10,10))
plt.xticks(range(1,21))
plt.yticks(error_rate)
plt.plot(range(1,21), error_rate, color='green', linestyle="--", marker="o", markerfacecolor='red', markersize=10)
plt.title("Finding Best K Value( ErrorRate Vs K Values)")
plt.xlabel("K Values")
plt.ylabel("Error Rate")
plt.show()
plt.savefig("ErrorRate_Vs_KValue.png")
print("\nSaved Elbow Method Graph.")
print("As per graph we can select k = 3,4,8,14,15....\nWe will go for k=8 and Compare with previous classification reports.")
print("\nSo for K=8, Setting Up The Model...")
PerfectKnnModel = KNeighborsClassifier(n_neighbors=15)
PerfectKnnModel.fit(x_train, y_train)
PerfectPredictions = PerfectKnnModel.predict(x_test)
print("Now We Have Confusion Matrix as :\n\n",confusion_matrix(y_test,PerfectPredictions),"\n\nClassification Report as :\n\n",classification_report(y_test,PerfectPredictions))
