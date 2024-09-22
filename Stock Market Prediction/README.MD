
# 📈 Stock Market Predictor App

This is a **Stock Market Predictor App** [Visit App](https://gouravsharma-stock-market-prediction.streamlit.app/) built using **Streamlit** and a pre-trained Machine Learning model. The app predicts stock prices based on input data such as **Opening Price**, **High Price**, **Low Price**, and **Volume**.

# ![Stock Market Predictor App](https://github.com/gouravsharma-00/Machine-Learning/blob/main/Stock%20Market%20Prediction/public/App_photo.PNG) <!-- Add a screenshot of the app here -->

## 🚀 Features
- Predicts stock prices based on historical data
- Provides risk-level indicators (High, Medium, Low Risk) based on predicted values
- Sleek and intuitive user interface for easy use
- Built using **Streamlit** for fast and interactive web-based predictions

## 🛠️ How to Run Locally

Follow the steps below to set up and run the Stock Market Predictor app on your local machine.

### 1. Clone the Repository
First, clone this repository to your local machine.

```bash
git clone https://github.com/your-username/stock-market-predictor.git
cd stock-market-predictor
```

### 2. Create a Virtual Environment (Optional but Recommended)
It is good practice to create a virtual environment to isolate dependencies.

```bash
python -m venv venv
```

Activate the virtual environment:

- For **Windows**:
    ```bash
    venv\Scripts\activate
    ```

- For **Mac/Linux**:
    ```bash
    source venv/bin/activate
    ```

### 3. Install Required Dependencies
Install all necessary Python libraries by running:

```bash
pip install -r requirements.txt
```

Ensure you have **Streamlit** installed:

```bash
pip install streamlit
```

### 4. Place the Pre-trained Model in the Right Directory
Download the pre-trained model file (`Stock_market_prediction.pkl`) and place it in the `./public/` directory of the repository. The model is required to make predictions.

### 5. Run the App
Launch the app by running:

```bash
streamlit run app.py
```

This will start a local server, and you can view the app by navigating to `http://localhost:8501` in your browser.

### 6. Interact with the App
You can now interact with the app by entering the stock market parameters like **Open Price**, **High Price**, **Low Price**, and **Volume**, and click **Predict** to get a prediction along with the risk assessment.

---

## 🔧 Required Libraries

- `streamlit==<version>` – Web framework to create interactive web applications.
- `joblib==<version>` – Library for loading the machine learning model.
- `pandas==<version>` – Used for handling the input data.
- `numpy==<version>` – Used for numerical operations in the background.

You can find the complete list of required libraries in the `requirements.txt` file.

## ✨ How It Works

The **Stock Market Predictor** app uses a pre-trained machine learning model to predict stock prices based on the following inputs:
- **Open Price**
- **High Price**
- **Low Price**
- **Volume**

Once the user enters the required values, the app passes the input data to the model to predict the closing stock price. The result is then displayed with a **Risk Indicator**:
- **High Risk**: The predicted stock price is low.
- **Low Risk**: The predicted stock price is safe.
- **Medium Risk**: The predicted stock price is in an uncertain range.

The risk levels are determined using predefined thresholds and are color-coded (e.g., Red for High Risk, Green for Low Risk).

## 📁 File Structure

```
├── app.py                   # Main app script
├── public/
│   └── Stock_market_prediction.pkl  # Pre-trained ML model
├── requirements.txt          # List of dependencies
├── README.md                 # Project documentation (This file)
└── screenshot.png            # Screenshot of the app (optional)
```

---

## 🔧 Future Improvements

- Add more stock features (e.g., Moving Average, Bollinger Bands) for more accurate predictions.
- Implement real-time stock data fetching using an API.
- Deploy the app online using Streamlit Cloud or Heroku.

---

## 💻 Contributing

Contributions, issues, and feature requests are welcome! Feel free to check the [issues page](https://github.com/your-username/stock-market-predictor/issues) if you want to contribute.

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
