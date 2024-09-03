import pandas as pd
import matplotlib.pyplot as plt

# Increase the font size
plt.rcParams.update({"font.size": 14})

# Load the dataset
file_path = "data.json"
data = pd.read_json(file_path)

# Extract the relevant data
total_male_with_disability = data["male"]["with_a_disability"]["total"]
total_female_with_disability = data["female"]["with_a_disability"]["total"]
total_male_without_disability = data["male"]["no_disability"]["total"]
total_female_without_disability = data["female"]["no_disability"]["total"]

data = [
    total_male_with_disability,
    total_male_without_disability,
    total_female_with_disability,
    total_female_without_disability,
]

# Create labels for the pie chart
labels = [
    f"{label} ({'{:,}'.format(data[i])})"
    for i, label in enumerate(
        [
            "Males With Disability",
            "Males Without Disability",
            "Females With Disability",
            "Females Without Disability",
        ]
    )
]

# Create the pie chart
plt.pie(
    data,
    labels=labels,
    autopct="%1.1f%%",
    colors=["#9AFFFF", "#7BF6F6", "#FF9A9A", "#FF7B7B"],
)
plt.title("Total Population With and Without a Disability (ages of 18 - 34)")

# Display the plot
plt.show()
