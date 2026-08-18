import numpy as np
import pandas as pd

# Make the results reproducible
np.random.seed(42)

# Number of participants
N = 500

# Patient IDs
patient_ids = [
    f"P{str(i).zfill(4)}"
    for i in range(1, N + 1)
]

# Age
age = np.random.normal(48, 12, N).round().astype(int)
age = np.clip(age, 18, 80)

# Sex
sex = np.random.choice(
    ["Male", "Female"],
    size=N,
    p=[0.48, 0.52]
)

# Treatment group
treatment = np.random.choice(
    ["Drug A", "Placebo"],
    size=N,
    p=[0.5, 0.5]
)

# Baseline biomarker
baseline_biomarker = np.random.normal(
    100,
    15,
    N
).round(2)

# Change in biomarker
# Drug A is designed to produce a larger reduction
change = np.where(
    treatment == "Drug A",
    np.random.normal(-25, 10, N),
    np.random.normal(-10, 10, N)
)

# Week 12 biomarker
week12_biomarker = (
    baseline_biomarker + change
).round(2)

# Treatment response
response_probability = np.where(
    treatment == "Drug A",
    0.72,
    0.52
)

response = np.where(
    np.random.random(N) < response_probability,
    "Yes",
    "No"
)

# Adverse events
adverse_event_probability = np.where(
    treatment == "Drug A",
    0.18,
    0.12
)

adverse_event = np.where(
    np.random.random(N) < adverse_event_probability,
    "Yes",
    "No"
)

# Create DataFrame
df = pd.DataFrame({
    "patient_id": patient_ids,
    "age": age,
    "sex": sex,
    "treatment_group": treatment,
    "baseline_biomarker": baseline_biomarker,
    "week12_biomarker": week12_biomarker,
    "response": response,
    "adverse_event": adverse_event
})

# --------------------------------------------------
# Intentionally introduce some data-quality problems
# --------------------------------------------------

# Missing values
missing_indices = np.random.choice(
    df.index,
    size=15,
    replace=False
)

df.loc[
    missing_indices[:8],
    "week12_biomarker"
] = np.nan

df.loc[
    missing_indices[8:],
    "age"
] = np.nan

# Duplicate records
duplicates = df.sample(
    5,
    random_state=42
)

df = pd.concat(
    [df, duplicates],
    ignore_index=True
)

# Save raw dataset
output_path = "data/raw/clinical_trial_raw.csv"

df.to_csv(
    output_path,
    index=False
)

print("Synthetic clinical trial dataset created!")
print(f"Rows: {len(df)}")
print(f"Columns: {len(df.columns)}")
print(f"Saved to: {output_path}")

print("\nFirst 5 rows:")
print(df.head())

print("\nMissing values:")
print(df.isnull().sum())

print("\nDuplicate rows:")
print(df.duplicated().sum())