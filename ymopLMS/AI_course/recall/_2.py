import pandas as pd
from sklearn.ensemble import AdaBoostClassifier
from sklearn.metrics import *
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split

df = pd.read_csv('https://yastatic.net/s3/lyceum/files/cef58ceb-187c-4104-9a90-124714292af0/upload.csv',
                 names=['buying', 'maint', 'doors', 'persons', 'lug_boot', 'safety', 'accep'])
df['accep'] = ~(df['accep'] == 'unacc')  # 1 - приемлемо, 0 - неприемлемо
X = pd.get_dummies(df.iloc[:, 0:6], drop_first=True)
y = df['accep']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)

base = DecisionTreeClassifier(max_depth=3)
base.fit(X_train, y_train)
y_pred_tr = base.predict(X_test)
print(f"Tree accuracy score: {accuracy_score(y_pred_tr, y_test)}")

boost = AdaBoostClassifier(estimator=base, n_estimators=100, learning_rate=0.5)
boost.fit(X_train, y_train)

boost.predict(X_test)
y_pred_ad = boost.predict(X_test)

print(f"Booster score: {accuracy_score(y_pred_ad, y_test)}")

from sklearn.ensemble import StackingClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
meta = LogisticRegression()

base_estimators = [
    ('rf', RandomForestClassifier(max_depth=4, n_estimators=100)),
    ('bo', AdaBoostClassifier(base, n_estimators=100))
]
stack = StackingClassifier(
    estimators=base_estimators,
    final_estimator=meta,
    passthrough=True,
)

stack.fit(X_train, y_train)

y_pred_st = stack.predict(X_test)
print(f"Stack accuracy: {accuracy_score(y_test, y_pred_st)}")