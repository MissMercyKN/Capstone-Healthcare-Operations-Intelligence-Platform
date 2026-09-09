# Capstone Healthcare Operations Intelligence Platform

## Overview

The Healthcare Operations Intelligence Platform is an analytics and machine learning decision-support system designed to improve hospital operational visibility.

The platform integrates healthcare data, operational analytics, and predictive modeling to identify congestion risks and support proactive operational decisions.

---

## Project Objectives

The platform aims to:

- Monitor healthcare operational performance
- Analyze patient flow patterns
- Identify capacity constraints
- Predict operational congestion risk
- Support data-driven management decisions

---

## System Architecture

The platform follows an end-to-end analytics pipeline:

Healthcare Data Sources

↓

Operational Database

↓

Feature Engineering

↓

Machine Learning Model

↓

Streamlit Decision Support Dashboard

---

## Key Features

### Executive Operations Dashboard

Provides:

- Operational risk indicators
- Department performance comparison
- Waiting time analysis
- Capacity overview

### Patient Flow Analytics

Includes:

- Patient demand trends
- Waiting time analysis
- Treatment duration analysis
- Department comparisons

### Capacity Intelligence

Analyzes:

- Occupancy pressure
- Department capacity utilization
- Operational bottlenecks

### Predictive Risk Analytics

Uses machine learning to predict:

- Future operational congestion risk
- High-pressure operational periods

### Supply Chain Analytics

Monitors:

- Inventory levels
- Stock availability
- Supply risks

---

## Machine Learning Model

### Objective

Predict next-period operational congestion risk using current operational conditions.

### Models Evaluated

- Logistic Regression baseline
- Random Forest classifier

### Final Model

Random Forest Classifier

### Evaluation

Performance metrics include:

- Precision
- Recall
- F1 Score
- Confusion Matrix
- ROC-AUC

Final ROC-AUC:

0.81

---

## Important Predictors

The model identified the following operational drivers:

1. Occupancy Rate
2. Staff Availability
3. Staff Ratio
4. Patient Volume
5. Treatment Duration
6. Waiting Time

---

## Technology Stack

### Programming

- Python

### Analytics

- Pandas
- NumPy
- Plotly

### Machine Learning

- Scikit-learn
- Joblib

### Dashboard

- Streamlit

### Data Storage

- SQLite

---

## Repository Structure
