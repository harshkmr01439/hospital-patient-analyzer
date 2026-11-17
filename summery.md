# Project Summary

**Name:** Harsh Kumar  
**ERP ID:** RU-26-01439  
**Project:** Hospital Patient Data Analyzer (PS No. 13)

## 1. Problem Statement
Hospital records often have duplicate entries, missing patient ages, and raw date strings. The problem was to clean this data, remove duplicates, fill missing values, calculate the length of stay for each patient, and show the data in groups (by department, gender, and age) using a menu-driven program.

## 2. Solution to the Problem
To solve this problem, I created a Python program that acts as a data analyzer. 
- The program first asks the user for the CSV file and reads it.
- It cleans the data by finding and deleting duplicate Patient IDs.
- It searches for missing ages and fills them with the median age so the data remains accurate.
- It converts the admission and discharge dates into proper time formats and subtracts them to calculate exactly how many days each patient stayed in the hospital.
- Finally, it provides an interactive menu where the user can view the total patients by department and gender, see average stay times, and view a visual bar chart of patient age groups.

## 3. How I Implemented It (Technical Details)
- **Language & Libraries:** Python 3, Pandas, and Matplotlib.
- **Data Cleaning:** Used `.drop_duplicates(subset=['Patient_ID'])` to remove repeated rows and `.fillna()` to put the median age in empty cells.
- **Calculations:** Used `pd.to_datetime()` to convert dates for subtraction, and `.groupby()` to count patients in each department and gender.
- **Visualization:** Used a basic `for` loop with `if-else` conditions to sort patients into age groups (0-40, 41-60, 61+) and plotted them using `plt.bar()`.

## 4. Problems Faced & Solutions

| Problems I Faced | The Solution I Used |
| :--- | :--- |
| Subtracting dates gave an error because Python read them as normal text strings. | I used `pd.to_datetime()` to convert the text into real dates before subtracting. This also correctly calculated `0 days` for same-day discharge. |
| Blank age values (`NaN`) were breaking the age group calculations and graphs. | I calculated the median integer age from the available data and used `.fillna()` to replace the empty spaces instead of using 0. |
| The `.groupby()` output looked like a default Pandas table, but the assignment required a format like `Cardiology: 2 \| Ortho: 1`. | I used a `for` loop to extract the grouped data and joined the text using `" \| ".join()` to match the required output format. |

## 5. How the Code Works (Inputs and Outputs)

When we run the program, here is step-by-step what input we give and what output we get:

### Option 1: Department and Gender Count
* **Input:** The program asks for a choice. I type `1` and press Enter.
* **Output:** It groups the patients and prints out exactly how many patients are in Cardiology, Ortho, etc., and shows the breakdown of Male and Female patients.

![Option 1 Screenshot]<img width="608" height="346" alt="option1_screenshot (1)" src="https://github.com/user-attachments/assets/9fffb7e2-22da-45b8-8781-d15428c1fe32" />


### Option 2: Length of Stay
* **Input:** I type `2` and press Enter.
* **Output:** It prints every Patient ID, shows exactly how many days they stayed in the hospital, and calculates the overall average stay for everyone.

![Option 2 Screenshot]<img width="613" height="335" alt="option2_screenshot" src="https://github.com/user-attachments/assets/9cf5ced8-7198-4338-8832-52fceabfbeda" />


### Option 3: Stay and Age Groups (Chart)
* **Input:** I type `3` and press Enter.
* **Output:** It counts how many patients fall into the age groups 0-40, 41-60, and 61+. Then, a separate window pops up showing a Matplotlib bar graph of these ages.

![Option 3 Screenshot]<img width="608" height="342" alt="option3_screenshot" src="https://github.com/user-attachments/assets/add5ab79-480d-41c1-a516-a439164362fd" />


### Option 4: Exit Program
* **Input:** I type `4` and press Enter.
* **Output:** The program prints "Exiting..." and safely closes the application.

![Option 4 Screenshot]<img width="608" height="341" alt="option4_screenshot" src="https://github.com/user-attachments/assets/ba5c1ac1-7aec-4207-a539-74e376a957ad" />
