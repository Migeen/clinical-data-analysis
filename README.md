# Clinical Trial Efficacy and Safety Analysis

![Python](https://img.shields.io/badge/Python-3.x-blue)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-orange)
![SciPy](https://img.shields.io/badge/SciPy-Statistics-green)
![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-orange)

## Project Overview

This project demonstrates an end-to-end analysis of a synthetic
clinical trial dataset comparing a treatment group (Drug A) with
a placebo group.

The analysis focuses on treatment efficacy, participant
characteristics, biomarker changes, treatment response, adverse
events, data quality, and basic statistical testing.

> **Important:** All data used in this project is synthetic and
> does not contain real patient information.

## Objectives

The project was created to demonstrate:

- Data cleaning and quality assessment
- Exploratory data analysis
- Descriptive statistics
- Clinical trial-style data analysis
- Data visualization
- Statistical hypothesis testing
- Analytical interpretation and communication

## Dataset

The synthetic dataset contains 500 unique participants and
includes the following variables:

| Variable | Description |
|---|---|
| `patient_id` | Unique participant identifier |
| `age` | Participant age |
| `sex` | Participant sex |
| `treatment_group` | Drug A or placebo |
| `baseline_biomarker` | Biomarker measurement at baseline |
| `week12_biomarker` | Biomarker measurement at Week 12 |
| `response` | Treatment response |
| `adverse_event` | Whether an adverse event occurred |

The raw dataset intentionally contains duplicate records and
missing values to demonstrate a realistic data-cleaning workflow.

## Technologies

- Python
- Pandas
- NumPy
- SciPy
- Matplotlib
- Seaborn
- Jupyter Notebook
- Git/GitHub

## Analysis Workflow

```text
Raw Clinical Trial Data
        ↓
Data Quality Assessment
        ↓
Data Cleaning
        ↓
Exploratory Data Analysis
        ↓
Efficacy Analysis
        ↓
Safety Analysis
        ↓
Statistical Testing
        ↓
Visualization
        ↓
Clinical Interpretation

How to Run

git clone <YOUR-GITHUB-REPOSITORY-URL>
cd clinical-data-analysis

Create a Virtual Environment
python3 -m venv .venv
source .venv/bin/activate

Install dependencies
pip install -r requirements.txt

Generate Synthetic Dataset
python src/generate_data.py

Open the analysis notebook
notebooks/clinical_trial_analysis.ipynb