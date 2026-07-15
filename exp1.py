import pandas as pd
data = {
'Student_ID': ['70084', '70005', '70006', '70007', '70008', '70009', '70010'],
'Test_Score': [85, 90, 91, 65, 78, 85, 95]
}
df = pd.DataFrame(data)
df.index = range(1, len(df) + 1)
print("24BDS-1 DA Marks:")
print(df)
print("-" * 30)
mean_score = df['Test_Score'].mean()
median_score = df['Test_Score'].median()
mode_score = df['Test_Score'].mode()[0] # [0] extracts the first mode
variance_score = df['Test_Score'].var()
std_score = df['Test_Score'].std()
print(f"Mean (Average) Score: {mean_score:.2f}")
print(f"Median (Middle) Score: {median_score:.2f}")
print(f"Mode (Most Frequent) Score: {mode_score}")
print(f"Variance (Spread): {variance_score:.2f}")
print(f"Standard Deviation: {std_score:.2f}")