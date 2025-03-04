import pandas as pd
import os

print("Current Working Directory:", os.getcwd())

file_path = 'titanic.csv'
if not os.path.exists('titanic.csv'):
    print(f"Error: The file '{file_path}' does not exist in the current directory.")
else:
    print(f"File '{file_path}' found. Loading data...")

    try:
        df = pd.read_csv('titanic.csv', on_bad_lines='skip')

        print(df.head())
        print(df.info())

        df['Age'].fillna(df['Age'].median(), inplace=True)
        df['Embarked'].fillna(df['Embarked'].mode()[0], inplace=True)
        df.drop('Cabin', axis=1, inplace=True)

        df.drop(['PassengerId', 'Name', 'Ticket'], axis=1, inplace=True)

        df['Sex'] = df['Sex'].map({'male': 0, 'female': 1})
        df['Embarked'] = df['Embarked'].map({'S': 0, 'C': 1, 'Q': 2})

        df.drop_duplicates(inplace=True)

        df.to_csv('cleaned_titanic.csv', index=False)

        print(df.head())
        print(df.isnull().sum())

    except pd.errors.ParserError as e:
        print(f"Error reading the CSV file: {e}")