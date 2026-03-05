# Nigeria to UK: The Healthcare Workforce Migration Audit
This repository contains the data science project for the Data Science Lab at Constructor University Bremen. Our research audits the migration cycle of Nigerian healthcare professionals—including doctors, nurses, and allied health workers—into the UK labor market.

## Project Overview
Nigeria is currently experiencing a critical healthcare emergency with a doctor-to-patient ratio of 1:9,083 and a significant nursing shortage. This project investigates the tension between Nigeria's internal economic pressures and the UK's active recruitment policies.

## The "Data Stories"
We investigate three critical aspects defining this migration:

Policy vs. Extraction: How UK visa policy and domestic labor shortages regulate the flow of Nigerian healthcare talent.

Skill Devaluation: The "Brain Waste" phenomenon, where highly qualified professionals are stuck in lower-tier Standard Occupational Classification (SOC) codes (e.g., qualified doctors working as care assistants).

Economic Synthesis: Whether the financial gain of remittances can truly compensate for the human capital deficit left in Nigerian hospitals.

## Navigation
For a detailed narrative and technical breakdown, see:

Introduction: The full data-driven story and conceptual framework.

Workplan: The technical roadmap, pair assignments (Coder/Data Steward), and research milestones.

## Repository Structure
This repository follows a structured analysis pipeline to ensure feasibility and reproducibility:

Plaintext
├── 01_Data_Raw/          # Immutable datasets (OECD, ONS, World Bank)
├── 02_Data_Processed/    # Cleaned data and SOC code mappings
├── 03_Scripts/           # Python scripts for regression and mapping
├── 04_Notebooks/         # Analytical chapters (sec1.ipynb, sec2.ipynb, etc.)
├── introduction.qmd      # Narrative landing page
└── WORKPLAN.md           # Task distribution and methodology

## How to Access
Narrative: View the Introduction for the project's foundational theory and research questions.

Methodology: Consult the Workplan for the specific data cleaning and analysis tasks assigned to each team pair.

Execution: Analysis is documented within the Jupyter Notebooks located in 04_Notebooks/.