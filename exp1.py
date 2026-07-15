import pandas as pd
data = {
'S.No': range(1, 8),
'Student_ID': ['70085', '70005', '70006', '70007', '70008', '70009', '70010'],
'Test_Score': [85, 90, 91, 65, 78, 85, 95]
}
df = pd.DataFrame(data)
print("24BDS-1 DA Marks:")
print(df.to_string(index=False))
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