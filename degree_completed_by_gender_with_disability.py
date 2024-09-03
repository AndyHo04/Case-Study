import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Increase the font size
plt.rcParams.update({"font.size": 14})

# Load the dataset
file_path = "data.json"
data = pd.read_json(file_path)
categories = ["High School", "Associates", "Bachelors", "Masters"]
x = np.arange(len(categories))

# Extract the relevant data
width = 0.35


# helper function for getting the key based on the disabled status
def get_disabled_key(disabled_status: bool) -> str:
    return "with_a_disability" if disabled_status else "no_disability"


# helper function for getting the degree information based on some parameters
def get_degree_info(gender: str, disabled: bool, degree: str) -> int:
    return data[gender][get_disabled_key(disabled)]["not_enrolled_in_school"][degree]


male = [
    get_degree_info("male", True, "high_school_graduate_(includes_equivalency)"),
    get_degree_info("male", True, "associate_degree"),
    get_degree_info("male", True, "bachelors_degree"),
    get_degree_info("male", True, "graduate_or_professional_degree"),
]
female = [
    get_degree_info("female", True, "high_school_graduate_(includes_equivalency)"),
    get_degree_info("female", True, "associate_degree"),
    get_degree_info("female", True, "bachelors_degree"),
    get_degree_info("female", True, "graduate_or_professional_degree"),
]

fix, ax = plt.subplots()
bars1 = ax.bar(x - width / 2, male, width, label="Male", color="blue")
bars2 = ax.bar(x + width / 2, female, width, label="Female", color="pink")

ax.set_xlabel("Education Received")
ax.set_ylabel("Number of People")
ax.set_xticks(x)
ax.set_xticklabels(categories)
ax.legend()

ax.grid(True, linestyle="--", alpha=0.5)

plt.title("Degree completed by gender with disability")
plt.ticklabel_format(style="plain", axis="y")
plt.show()
