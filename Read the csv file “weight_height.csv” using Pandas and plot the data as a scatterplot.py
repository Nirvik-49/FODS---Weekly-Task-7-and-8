import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV file
data = pd.read_csv("weight_height.csv")

# Display the first few rows of the dataframe
print(data.head())

# Create scatter plots
plt.figure(figsize=(15, 10))

# Scatter plot: Weight vs Height
plt.subplot(2, 2, 1)
plt.scatter(data['Height_cm'], data['Weight_kg'], color='blue')
plt.title('Weight vs Height')
plt.xlabel('Height (cm)')
plt.ylabel('Weight (kg)')

# Scatter plot: Age vs Weight
plt.subplot(2, 2, 2)
plt.scatter(data['Age'], data['Weight_kg'], color='green')
plt.title('Age vs Weight')
plt.xlabel('Age (years)')
plt.ylabel('Weight (kg)')

# Scatter plot: Height vs Age
plt.subplot(2, 2, 3)
plt.scatter(data['Height_cm'], data['Age'], color='red')
plt.title('Height vs Age')
plt.xlabel('Height (cm)')
plt.ylabel('Age (years)')

# Scatter plot: Gender vs Height
plt.subplot(2, 2, 4)
gender_colors = {'Male': 'blue', 'Female': 'pink'}
plt.scatter(data['Height_cm'], data['Gender'].map(gender_colors), color=data['Gender'].map(gender_colors))
plt.title('Gender vs Height')
plt.xlabel('Height (cm)')
plt.ylabel('Gender')

# Adjust layout
plt.tight_layout()
plt.show()
