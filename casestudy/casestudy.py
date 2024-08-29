import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
file_path = 'DEData.csv'
data = pd.read_csv(file_path)

# Cleaning and extracting relevant information
data.columns = ['Label', 'Count']
data['Label'] = data['Label'].str.strip()

# Extracting the total population with and without a disability
total_with_disability = data.iloc[2]['Count'].replace(',', '')
total_without_disability = data.iloc[13]['Count'].replace(',', '')

# Convert to numeric
total_with_disability = float(total_with_disability)
total_without_disability = float(total_without_disability)

# Manually extracting the relevant rows based on their positions
# "With a disability" section
with_disability_education = data.iloc[10:13]

# "Without a disability" section
without_disability_education = data.iloc[21:24]

# Convert the counts to numeric and sum them, then convert to millions
with_disability_total = with_disability_education['Count'].str.replace(',', '').astype(float).sum() / 1_000_000
without_disability_total = without_disability_education['Count'].str.replace(',', '').astype(float).sum() / 1_000_000

# Recalculate per capita as number of people with an associate's degree or higher per 1,000 people
per_thousand_with_disability = round((with_disability_total * 1_000_000) / total_with_disability * 1000)
per_thousand_without_disability = round((without_disability_total * 1_000_000) / total_without_disability * 1000)

# Original total population values
total_with_disability_million = total_with_disability / 1_000_000
total_without_disability_million = total_without_disability / 1_000_000

# Creating subplots with increased font size
fig, axes = plt.subplots(3, 1, figsize=(12, 18))

# Set a common font size for all plots
plt.rcParams.update({'font.size': 14})

# Plot 1: Total population with and without a disability
axes[0].bar(['With Disability', 'Without Disability'], 
            [total_with_disability_million, total_without_disability_million], 
            color=['blue', 'green'])
axes[0].set_title('Total Population With and Without a Disability')
axes[0].set_ylabel('Population (in millions)')
axes[0].text(0, total_with_disability_million + 1, f'{total_with_disability_million:.2f}M', ha='center', va='bottom')
axes[0].text(1, total_without_disability_million + 1, f'{total_without_disability_million:.2f}M', ha='center', va='bottom')
axes[0].set_ylim(0, max(total_with_disability_million, total_without_disability_million) + 5)

# Plot 2: Per capita with disability
axes[1].bar('With Disability', per_thousand_with_disability, color='blue')
axes[1].set_title('Per Capita with Associate\'s Degree or Higher (With Disability)')
axes[1].set_ylabel('Per 1,000 People')
axes[1].set_ylim(0, max(per_thousand_with_disability, per_thousand_without_disability) + 50)
axes[1].text(0, per_thousand_with_disability + 5, f'{per_thousand_with_disability}', ha='center', va='bottom')

# Plot 3: Per capita without disability
axes[2].bar('Without Disability', per_thousand_without_disability, color='green')
axes[2].set_title('Per Capita with Associate\'s Degree or Higher (Without Disability)')
axes[2].set_ylabel('Per 1,000 People')
axes[2].set_ylim(0, max(per_thousand_with_disability, per_thousand_without_disability) + 50)
axes[2].text(0, per_thousand_without_disability + 5, f'{per_thousand_without_disability}', ha='center', va='bottom')

# Adjust layout to prevent overlap
plt.tight_layout()

# Display the plots
plt.show()

