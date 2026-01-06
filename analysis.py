import pandas as pd

def load_data():
    data = {
        "Name": ["Alice", "Bob", "Charlie", "David"],
        "Department": ["IT", "HR", "IT", "Finance"],
        "Salary": [60000, 45000, 70000, 50000]
    }
    return pd.DataFrame(data)

def analyze_data(df):
    print("Full Dataset:")
    print(df)
    print("\nAverage Salary:")
    print(df["Salary"].mean())
    print("\nSalary by Department:")
    print(df.groupby("Department")["Salary"].mean())

def main():
    df = load_data()
    analyze_data(df)

if __name__ == "__main__":
    main()
