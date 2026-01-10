
# Food Crop Price Prediction (2012–2015)
### Linear Regression Assignment - Week 6

This project focuses on analyzing historical food crop prices in Kenya and building a predictive model using Linear Regression to estimate commodity values based on volume, variety, and temporal features.

## 📋 Table of Contents
- [Project Overview](#project-overview)
- [Dataset Description](#dataset-description)
- [Installation & Setup](#installation--setup)
- [Project Workflow](#project-workflow)
- [Model Performance](#model-performance)
- [Key Insights](#key-insights)

## 🎯 Project Overview
The objective of this assignment is to perform exploratory data analysis (EDA), rigorous data cleaning, and feature engineering on agricultural commodity data to build a supervised learning model that predicts the price (`Values_in_Ksh`).

## 📊 Dataset Description
The dataset contains records of food crop commodities from 2012 to 2015 with the following features:
- **Produce_Variety**: General category (Horticulture, Cereals, Legumes, Roots & Tubers).
- **Commodity_Type**: Specific crop name (e.g., Cabbages, Dry Maize, Rosecoco Beans).
- **Unit**: The packaging or measurement unit (e.g., Ext Bag, Bag, Med Bunch).
- **Volume_in_Kgs**: The weight of the item in Kilograms.
- **Values_in_Ksh**: The market price (Target Variable).
- **Date**: Timestamp of the market record.