````markdown
# 💻 Laptop Price Prediction Model

A machine learning project that predicts laptop prices based on hardware specifications using regression algorithms such as **Linear Regression**, **Support Vector Regression (SVR)**, and **Random Forest**.

Built and fine-tuned by [Satyam Bhagat](https://github.com/satyam2006-cmd).

---

## 📊 Project Overview

With the rise of online laptop marketplaces, estimating the right price based on specifications can be tricky. This model helps:

- Understand how features like RAM, CPU, and GPU affect price.
- Predict laptop prices in **Euros** for given specs.
- Train multiple ML models and choose the best-performing one.

---

## 🗃️ Dataset

- **Source:** `laptop_prices.csv`
- **Rows:** ~1,700
- **Target Variable:** `Price_euros`
- **Key Features:**
  - RAM
  - Weight
  - Screen Size
  - CPU Brand
  - GPU Brand
  - HDD/SSD
  - Touchscreen
  - IPS Display
  - Operating System

---

## ⚙️ Installation

1. **Clone the repo**
   ```bash
   git clone https://github.com/satyam2006-cmd/Laptop-Price-Prediction-Model.git
   cd Laptop-Price-Prediction-Model
````

2. **Install required packages**

   ```bash
   pip install -r requirements.txt
   ```

3. **Run the notebook**

   ```bash
   jupyter notebook Laptop_Price_Prediction.ipynb
   ```

---

## 🧠 Models Used

| Model                   | R² Score     |
| ----------------------- | ------------ |
| Linear Regression       | \~0.83       |
| Support Vector Machine  | \~0.75       |
| Random Forest Regressor | **\~0.88** ✅ |

* The best performance was achieved by the **Random Forest Regressor**, making it the final model used for prediction.

---

## 📌 Workflow

1. **Data Cleaning**

   * Remove irrelevant columns
   * Fix anomalies in features
   * Convert text-based specs to numeric (e.g., `Yes/No`, `Intel/AMD`)
2. **Feature Engineering**

   * Create new binary features (`Touchscreen`, `IPS`)
   * Encode categorical variables (`LabelEncoder`, `OneHotEncoder`)
3. **Model Training**

   * Compare Linear, SVR, and Random Forest regressors
   * Evaluate using R² and cross-validation
4. **Prediction**

   * Accepts custom laptop specs and predicts price

---

## 🧪 Sample Prediction

```python
query = np.array(['HP', 'Notebook', 'Intel Core i5 7th Gen', '8GB', '1TB HDD', 
                  'Windows 10', 'Intel HD Graphics 620', '15.6', 'No', 'No', '2.1'])

# Preprocess and reshape for prediction
input_data = preprocess(query)
predicted_price = model.predict(input_data)
print(f"Predicted Price: {predicted_price[0]:.2f} Euros")
```

---

## 📦 Requirements

* Python 3.8+
* pandas
* numpy
* matplotlib / seaborn
* scikit-learn
* Jupyter Notebook

You can install them via:

```bash
pip install -r requirements.txt
```

---

## 🧠 Enhancements (Optional)

* [ ] Deploy as Flask web app for user interaction.
* [ ] Add Streamlit dashboard for visual predictions.
* [ ] Save model using `joblib` or `pickle`.
* [ ] Host on **Render**, **Heroku**, or **Vercel**.
* [ ] Add voting system for user feedback on predictions.

---

## 🙋‍♂️ Author

**Satyam Bhagat**

* GitHub: [@satyam2006-cmd](https://github.com/satyam2006-cmd)

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

---

## 💬 Feedback

Feel free to create an issue or pull request. Star ⭐ the repo if you found it helpful!

```

---

Let me know if you want:
- A downloadable version
- To automatically upload it to your repo
- Diagram or screenshot section added
```
