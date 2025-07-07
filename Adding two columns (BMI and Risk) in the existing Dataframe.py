import pandas as pd

# Read the CSV file into a DataFrame
try:
    df = pd.read_csv("weight_height.csv")
except FileNotFoundError:
    print("The file 'weight_height.csv' was not found. Please check the file path.")
    exit()

# Print the columns to check for any discrepancies

print("Columns in DataFrame:", df.columns)

# Strip whitespace from column names

df.columns = df.columns.str.strip()

# Check if the required columns exist

required_columns = ['Name', 'Age', 'Gender', 'Height_cm', 'Weight_kg']
for col in required_columns:
    if col not in df.columns:
        print(f"Column '{col}' is missing from the DataFrame.")
        exit()

# Calculate BMI
df['BMI'] = df['Weight_kg'] / (df['Height_cm'] / 100) ** 2

# Define a function to determine the risk category based on BMI
def determine_risk(bmi):
    if bmi < 18.5:
        return 'Nutrient deficient'
    elif 18.5 <= bmi < 24.9:
        return 'Lower risk'
    elif 25 <= bmi < 29.9:
        return 'Heart disease risk'
    elif 30 <= bmi < 34.9:
        return 'Higher risk of diabetes, heart disease'
    elif bmi >= 40:
        return 'Serious health condition risk'
    else:
        return 'Unknown'

# function to create the Risk column
df['Risk'] = df['BMI'].apply(determine_risk)

# Display the updated DataFrame
print(df)

# Save the updated DataFrame to a new CSV file
df.to_csv("updated_weight_height.csv", index=False)
