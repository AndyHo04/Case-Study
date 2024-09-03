import pandas as pd
import matplotlib.pyplot as plt

# Increase the font size
plt.rcParams.update({"font.size": 14})

# Load the dataset
data = pd.read_json("data.json")


# helper function for getting the key based on the disabled status
def get_disabled_key(disabled_status: bool) -> str:
    return "with_a_disability" if disabled_status else "no_disability"


# helper function for getting the degree information based on some parameters
def get_degree_info(disabled: bool, degree: str) -> int:
    male = data["male"][get_disabled_key(disabled)]["not_enrolled_in_school"][degree]
    female = data["female"][get_disabled_key(disabled)]["not_enrolled_in_school"][
        degree
    ]
    return male + female


# collect data for people with and without disabilities
with_disability_high_school = get_degree_info(
    True, "high_school_graduate_(includes_equivalency)"
)
with_disability_associates = get_degree_info(True, "associate_degree")
with_disability_bachelors = get_degree_info(True, "bachelors_degree")
with_disability_masters = get_degree_info(True, "graduate_or_professional_degree")

without_disability_high_school = get_degree_info(
    False, "high_school_graduate_(includes_equivalency)"
)
without_disability_associates = get_degree_info(False, "associate_degree")
without_disability_bachelors = get_degree_info(False, "bachelors_degree")
without_disability_masters = get_degree_info(False, "graduate_or_professional_degree")

# plot the data
data = [
    with_disability_high_school,
    with_disability_associates,
    with_disability_bachelors,
    with_disability_masters,
]
plt.plot(
    ["High School", "Associates", "Bachelors", "Masters"],
    data,
    label="With Disability",
    marker="o",
)

data = [
    without_disability_high_school,
    without_disability_associates,
    without_disability_bachelors,
    without_disability_masters,
]
plt.plot(
    ["High School", "Associates", "Bachelors", "Masters"],
    data,
    label="Without Disability",
    marker="o",
)

# add labels and title
plt.title("Discrepancy in education obtained based on disability status")
plt.ticklabel_format(style="plain", axis="y")

# display the plot
plt.legend()
plt.show()
