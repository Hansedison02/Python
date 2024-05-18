# import libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from sklearn.metrics import confusion_matrix, classification_report
from sklearn.neighbors import (NeighborhoodComponentsAnalysis, KNeighborsClassifier)
from sklearn.model_selection import train_test_split

# call data
df = sns.load_dataset('iris')
df.head()

# data length
df.shape

# call features

dropped_column = ['species']
features = df.drop(dropped_column, axis = 1)
features.head()

# class variable
dropped_column = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width']

true_class = df.drop(dropped_column, axis = 1)
true_class.head()

#draw scatter graph

plt.scatter(features, true_class, c = "#1F77B4")
plt.scatter(x1, y1, c="pink", linewidths = 2, marker = "s", edgecolor = "green", s = "50")
plt.scatter(x1, y1, c="yellow", linewidths = 2, marker = "^", edgecolor = "#C42B1C", s = "200")
plt.xlabel("Length")
plt.ylabel("Width")
plt.title('Iris Dataset')
plt.show()

# chose samples for training and testing
X_train, X_test, y_train, y_test = train_test_split(features, true_class, test_size = 0.2, random_state = 12345)

#train features 
X_train

#train class
y_train

#test features

X_test

#test class

y_test

knn = KNeighborsClassifier(n_neighbors = 3)

knn_model = knn.fit(X_train, y_train)

predicted_class = knn_model.predict(X_test)
predicted_class

cm = confusion_matrix(y_test, predicted_class)
cm

class_name = y_test['species'].unique().tolist()
class_name

sns.heatmap(cm, annot = True, fmt = 'g', xticklabels=class_name, yticklabels = class_name)
plt.ylabel('Predicted Class:', fontsize = 13)
plt.xlabel('True Class:', fontsize = 13)
plt.title('Confusion Matrix', fontsize = 17)
plt.show()

print(classification_report(y_test, predicted_class))
