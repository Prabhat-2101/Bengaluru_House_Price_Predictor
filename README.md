# 🏡 Bengaluru House Price Predictor (ML Pipeline)

This project predicts house prices in **Bengaluru** using machine
learning. It includes preprocessing like **BHK extraction, sqft
conversion, encoding, scaling, and outlier handling**.

## 🚀 Features

-   Predict price from **Location, BHK, and Square Feet**
-   Handles range values like `1200-1500 sqft`
-   One‑hot encoding applied **after train‑test split**
-   Feature scaling using `StandardScaler`
-   Supports Linear Regression, Ridge, Lasso, Random Forest, and XGBoost
-   Metrics: **R², RMSE, MAE**

## 🧠 Tech Stack

  Type       Tools
  ---------- --------------------------------------
  Language   Python
  ML         Scikit‑Learn, Pandas, NumPy, XGBoost
  Notebook   Jupyter (`.ipynb`)

## 📂 Project Structure

    Project/
    │── house_price_prediction.ipynb
    │── house_price_predictor_lr.pkl
    │── main.py
    │── utils.py
    │── data/
    │── images/
    │── columns.txt
    │── locations.txt
    │── requirements.txt
    │── README.md

## 🔧 Setup

``` sh
git clone <repo_link>
pip install -r requirements.txt
jupyter notebook house_price_prediction.ipynb
```

## 🏗 Pipeline

1.  Load & clean data\
2.  Extract BHK\
3.  Convert sqft → numeric\
4.  Train‑test split\
5.  Encode → Align → Scale\
6.  Train & evaluate\
7.  Save model

## 🤝 Future Scope

-   Build API (FastAPI/Flask)
-   Deploy on AWS (EC2/Lambda)
-   Add rental prediction

## ✍ Author

**Prabhat Kumar Raj**\