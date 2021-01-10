import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import svm
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import cross_val_score, LeaveOneOut
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from pprint import pprint
from statistics import mean

# Prepare dataset
metadata1 = pd.read_csv("./results/tpehgdb_metadata.csv",
                        true_values=["t"], false_values=["f"])
del metadata1["Group"]

metadata2 = pd.read_csv("./results/tpehgdb_additional_metadata.csv",
                        true_values=["yes"], false_values=["no"], na_values=["None"])
metadata2["Record"] = metadata2["RecID"].map("tpehg{}".format)
metadata2["Placental_position"] = metadata2["Placental_position"].replace(
    {"end": -1, "front": 1})
metadata2["Funneling"] = metadata2["Funneling"].replace(
    {"negative": -1, "positive": 1})
del metadata2["RecID"]
del metadata2["Gestation"]
del metadata2["Rectime"]

metadata = pd.merge(metadata1, metadata2, on="Record")
metadata = metadata.dropna()

data = pd.read_csv("./results/sample_entropy_ch4.csv")
del data["Group"]
del data["Rec_Time"]

data = pd.merge(data, metadata, on="Record")

# Calculate weights
class_counts = {
    True: sum(data["Premature"] == True),
    False: sum(data["Premature"] == False)
}
pprint(class_counts)
max_class_count = max(class_counts.values())
class_weights = {
    True: max_class_count/class_counts[True],
    False: max_class_count/class_counts[False],
}

# Split dataset
X = data.copy()
del X["Premature"]
del X["Gestation"]
del X["Record"]
y = data["Premature"]


# Estimate model accuracy with leave one out schema
clf1 = make_pipeline(
    StandardScaler(),
    svm.SVC(kernel='linear', C=1,
            # class_weight=class_weights
            )
)
scores = cross_val_score(clf1, X, y, cv=LeaveOneOut())
print(
    f"[SVM] Leave one out cross validation score: {scores.mean()} ({scores.std()})")


# Find feature importances
clf2 = RandomForestClassifier(
    n_estimators=500, n_jobs=-1, class_weight=class_weights)
clf2.fit(X, y)
features = X.columns
importances = clf2.feature_importances_
indices = np.argsort(importances)
plt.figure(figsize=(5, 5))
plt.title('Feature Importances')
plt.barh(range(len(indices)), importances[indices], color='k', align='center')
plt.yticks(range(len(indices)), [features[i] for i in indices])
plt.xlabel('Relative Importance')
plt.subplots_adjust(left=0.5)
plt.savefig("./results/feature_importances.pdf")
