# Fuel Consumption Prediction Model

This project predicts fuel consumption for flights based on the following features:
- Number of passengers
- Distance traveled
- Flight duration
- Aircraft type

The machine learning model has been integrated into a web application using **Streamlit**, allowing for an easy-to-use interface for users to input flight details and get an estimate of the fuel consumption.

## Table of Contents
1. [Features](#features)
2. [Model Development](#model-development)
3. [Web Application](#web-application)
4. [Installation](#installation)
5. [Running the App](#running-the-app)
6. [Contributing](#contributing)

## Features
- Predicts fuel consumption using multiple features: passengers, distance, duration, and aircraft type.
- Interactive web app built using **Streamlit** for easy usage.
- The app allows users to input flight information and view fuel consumption predictions in real-time.

## Model Development
The model was developed using Python and various machine learning libraries like `scikit-learn`. The dataset used for training is provided in the `public/` folder. It consists of flight-related data including the number of passengers, distance traveled, flight duration, and aircraft type. The development process is documented in the Jupyter notebook (`model_development.ipynb`) located in the `public/` folder.

## Web Application
The web application is built using **Streamlit**. Streamlit is an open-source Python framework that allows developers to build interactive web applications for machine learning models.

The main file for running the application is `App.py`, and it uses the pre-trained model to make predictions on the user's input.

## Installation

Follow these steps to set up the project on your local machine:

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/fuel-consumption-predictor.git
   cd fuel-consumption-predictor
   ```

2. Install the required dependencies:
   It's recommended to use a virtual environment to manage dependencies. You can install \`virtualenv\` if you haven't already:

   ```bash
   pip install virtualenv
   ```

   Create and activate the virtual environment:
   ```bash
   virtualenv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

   Install the dependencies listed in the \`requirements.txt\` file:
   ```bash
   pip install -r requirements.txt
   ```

3. Ensure you have **Streamlit** installed:
   ```bash
   pip install streamlit
   ```

## Running the App

Once all the dependencies are installed, you can run the app with the following command:

```bash
streamlit run App.py
```

This will start a local web server, and you can access the web app by navigating to the link provided in the terminal (usually \`http://localhost:8501/\`).

## Data

The dataset used for training the model is located in the `public/` folder. It is in CSV format (`data.csv`), and the Jupyter notebook used for developing the machine learning model is also provided (`model_development.ipynb`).

## Contributing

Feel free to open issues and contribute to this project by creating pull requests. Any contributions, whether it's bug fixes, new features, or improving documentation, are welcome!

---

Enjoy predicting fuel consumption effortlessly with our interactive web app!
