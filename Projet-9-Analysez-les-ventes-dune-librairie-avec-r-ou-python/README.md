# Analysis of Sales and Customer Behavior - Lapage Bookstore

## 📌 About the Project
This project provides a comprehensive analysis of the online sales performance and customer purchasing behavior for the **Lapage Bookstore** since its launch, covering the period from **March 2021 to February 2023**[cite: 18]. 

The primary aim of this study is to evaluate overall revenue trends, identify key customer segments, analyze product category popularity, and uncover actionable insights to guide future business strategies[cite: 18].

---

## 🎯 Key Objectives & Issues
* **Sales Performance Tracking:** Analyze monthly turnover, transaction volume, and product movements over time[cite: 18].
* **Customer Segmentation & Behavior:** Understand purchasing habits across age groups and genders, focusing on transaction frequency and average basket size[cite: 18].
* **Product & Category Breakdown:** Determine revenue concentration across book categories and spot top/bottom performing items[cite: 18].
* **Business Recommendations:** Address anomalies (such as sales drops) and propose data-backed strategies to improve customer retention and basket value[cite: 18].

---

## 📊 Dataset Overview
The analysis is based on raw website extraction data combining three main tables[cite: 18]:

1. **Customers (`customers`)**[cite: 18]
   * **Scope:** 8,621 customer entries[cite: 18].
   * **Attributes:** `client_id`, `sex`, `birth`[cite: 18].
2. **Products (`products`)**[cite: 18]
   * **Scope:** 3,286 book references[cite: 18].
   * **Attributes:** `id_prod`, `price`, `categ`[cite: 18].
3. **Transactions (`transactions`)**[cite: 18]
   * **Scope:** 1,048,575 transaction records[cite: 18].
   * **Attributes:** `id_prod`, `date`, `session_id`, `client_id`[cite: 18].

> **Data Pipeline Note:** Merging these datasets yielded a consolidated dataset of 687,534 valid transaction lines[cite: 18]. A total of 4 B2B outlier accounts were excluded for statistical consistency[cite: 18].

---

## 🔍 Key Findings

* **Revenue Distribution:** Book Categories 0 and 1 generate nearly 77% of total revenue[cite: 18].
* **Revenue Inequality:** A Gini index of 0.398 demonstrates moderate revenue concentration among top buyers[cite: 18].
* **Demographic Patterns:**
  * **Younger Buyers (< 30 years):** Feature significantly higher average basket values but lower transaction frequency[cite: 18].
  * **Mid-Aged Buyers (30–50 years):** Buy more frequently but spend less per transaction[cite: 18].
  * **Category Preference:** Younger buyers prefer Category 2 books (average age: 22.8 years), whereas Category 1 appeals to older audiences (average age: 49.8 years)[cite: 18].

---

## 💡 Strategic Recommendations

* **Investigate Anomalies:** Conduct a detailed audit to determine the cause of the sudden drop in active clients and transactions in February 2023[cite: 18].
* **Loyalty Programs for Young Adults (<30):** Implement targeted loyalty perks to increase purchase frequency[cite: 18].
* **Upselling Strategies (30–50 Age Group):** Introduce personalized bundle recommendations to raise average order value[cite: 18].
