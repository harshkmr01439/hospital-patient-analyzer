# Hospital Patient Data Analyzer
# PS No. 13 - First Year Python Project
# Submitted by: Harsh Kumar (RU-26-01439)

import pandas as pd
import matplotlib.pyplot as plt

# 1. Ask user for CSV file name
file_name = input("Enter CSV file path: ")

try:
    df = pd.read_csv(file_name)
except:
    print("File not found or error opening file.")
    exit()

# 2. Data Cleaning
# Remove duplicate records
initial_count = len(df)
df = df.drop_duplicates(subset=['Patient_ID'])
duplicates_removed = initial_count - len(df)

# Fill missing Age with median
missing_age_count = df['Age'].isna().sum()
if missing_age_count > 0:
    median_age = int(df['Age'].median())
    df['Age'] = df['Age'].fillna(median_age)
    print(f"Duplicates removed: {duplicates_removed}")
    print(f"Missing Age filled with median: {median_age}")
elif duplicates_removed > 0:
    print(f"Duplicates removed: {duplicates_removed}")

# Ensure Age is an integer
df['Age'] = df['Age'].astype(int)

# Convert dates to find Length of Stay
df['Admit_Date'] = pd.to_datetime(df['Admit_Date'])
df['Discharge_Date'] = pd.to_datetime(df['Discharge_Date'])
df['Length_of_Stay'] = (df['Discharge_Date'] - df['Admit_Date']).dt.days

# 3. Interactive Menu
print("\n--- Menu ---")
print("1. Department and Gender count")
print("2. Length of stay")
print("3. Stay and age groups")
print("4. Exit")

choice = input("\nEnter choice (1/2/3/4): ")

if choice == '1':
    # Department count
    dept_counts = df.groupby('Department')['Patient_ID'].count()
    parts = []
    for dept, count in dept_counts.items():
        parts.append(f"{dept}: {count}")
    print(" | ".join(parts))
    
    # Gender count
    gender_counts = df.groupby('Gender')['Patient_ID'].count()
    gender_parts = []
    for gender, count in gender_counts.items():
        gender_parts.append(f"{gender}: {count}")
    print("Gender Breakdown:", " | ".join(gender_parts))
    
    print(f"Total patients: {len(df)}")

elif choice == '2':
    # Length of stay
    for index, row in df.iterrows():
        print(f"{row['Patient_ID']}: {row['Length_of_Stay']} days")
    avg_stay = df['Length_of_Stay'].mean()
    print(f"Average stay: {avg_stay:.2f} days")

elif choice == '3':
    # Stay and age groups
    avg_stay = df['Length_of_Stay'].mean()
    print(f"Average stay: {avg_stay:.2f} days")

    # Counting age groups manually
    group_0_40 = 0
    group_41_60 = 0
    group_61_plus = 0

    for age in df['Age']:
        if age <= 40:
            group_0_40 += 1
        elif age <= 60:
            group_41_60 += 1
        else:
            group_61_plus += 1

    print(f"Age groups: 0-40: {group_0_40} | 41-60: {group_41_60} | 61+: {group_61_plus}")
    print("Bar chart displayed")

    # Simple bar chart
    labels = ['0-40', '41-60', '61+']
    counts = [group_0_40, group_41_60, group_61_plus]

    plt.bar(labels, counts, color='blue')
    plt.title('Patient Age Groups')
    plt.xlabel('Age Group')
    plt.ylabel('Number of Patients')
    plt.show()

elif choice == '4':
    print("Exiting...")
else:
    print("Invalid choice.")