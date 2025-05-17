import pandas as pd

def change_sex(item):
    # Заменяем пол на числовое значение
    return item=='male'

def is_alone(row):
    return row['SibSp'] + row['Parch'] == 0

df = pd.read_csv('./titanic.csv')

df.drop(columns=['PassengerId', 'Name', 'Ticket', 'Cabin'], inplace=True)

df = df.dropna()

df['Sex'] = df['Sex'].apply(change_sex)

# Преобразование категориальных данных в столбце Embarked с созданием новых столбцов
df = pd.get_dummies(df, columns=['Embarked'])


df['Alone'] = df.apply(is_alone, axis=1)


# Нормируе  Fare и Age
df['Fare'] = (df['Fare'] - df['Fare'].min()) / (df['Fare'].max() - df['Fare'].min())
df['Age'] = (df['Age'] - df['Age'].min()) / (df['Age'].max() - df['Age'].min())


# ------------------------------- ОБУЧЕНИЕ МОДЕЛЕЙ -----------------------

from sklearn.neighbors import KNeighborsClassifier as knn
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# KNN -------------------------------------
model = knn(n_neighbors=5)

# Определяем признаки и целевую переменную
X = df.drop('Survived', axis=1)
y = df['Survived']

# Разбиваем на обучающую и тестовую выборки
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Обучаем модель
model.fit(X_train, y_train)

y_predic = model.predict(X_test)


# Logistic Linear model -------------------------------------

# Логистическая регрессия для сравнения с KNN
logreg = LogisticRegression(max_iter=1000)
logreg.fit(X_train, y_train)

y_pred_logreg = logreg.predict(X_test)


# Решение случайным лесом -------------------------------------

# Создаем и обучаем модель случайного леса
rf_model = RandomForestClassifier(n_estimators=100, random_state=42)
rf_model.fit(X_train, y_train)

# Предсказываем значения на тестовой выборке
y_pred_rf = rf_model.predict(X_test)


# Оцениваем точность -------------------------------------
accuracy_rf = accuracy_score(y_test, y_pred_rf)
print("Accuracy Random Forest:", accuracy_rf)
accuracy_scaled = accuracy_score(y_test, y_predic)
print("Accuracy after scaling:", accuracy_scaled)
accuracy_logreg = accuracy_score(y_test, y_pred_logreg)
print("Accuracy Logistic Regression:", accuracy_logreg)
