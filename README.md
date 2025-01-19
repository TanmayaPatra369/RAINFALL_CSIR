# Rainfall Prediction Using Machine Learning 

## Documentation

You can access the related documentation [here](https://docs.google.com/document/d/16p8UUPCuUkwHRi5bispmXUEPQqchXkXe/edit?usp=drive_link&ouid=104398427413822736555&rtpof=true&sd=true).

## Overview

This project aims to predict rainfall based on historical data using machine learning algorithms. The model is designed to assist in weather forecasting and improve accuracy in predicting rainfall patterns, benefiting agriculture, disaster management, and water resource management.

## Features

- Predicts the amount of rainfall based on various meteorological features.
- Uses machine learning algorithms to analyze historical weather data.
- Provides visualizations of the data and predictions.

## Technologies Used

- **Python** (for data processing and model building)
- **Pandas** (for data manipulation)
- **Scikit-learn** (for machine learning models)
- **Matplotlib/Seaborn** (for data visualization)
- **Jupyter Notebooks** (for exploratory analysis and documentation)

## Installation

### Requirements

- Python 3.6 or above
- Pandas
- Numpy
- Scikit-learn
- Matplotlib
- Seaborn

### Steps

1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/yourusername/rainfall-prediction.git
   ```

2. Navigate to the project directory:

   ```bash
   cd rainfall-prediction
   ```

3. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Run the Jupyter notebook to explore the data and train the model:

   ```bash
   jupyter notebook
   ```

## Usage

- Import the dataset and perform data cleaning.
- Train multiple machine learning models (e.g., Linear Regression, Random Forest, etc.).
- Evaluate the performance of each model using metrics like RMSE, MAE, and R².
- Use the trained model to make predictions on new weather data.

## Dataset
- You can access the Dataset [here](https://drive.google.com/file/d/15iHz0Lv3ODvSi0vEZXXsWB1__svYbYOs/view?usp=drive_link).
- The dataset used in this project contains historical weather data, including features like temperature, humidity, wind speed, and more.
- Data is publicly available or custom-made for this project.

## Example Predictions

- Display prediction results here.

## Results and Analysis

After training and evaluating multiple models, the Random Forest model and XGBoost achieved the best performance with an RMSE of 0.83 and an R² of 0.82.

### Visualizations

1. **Rainfall Prediction vs Actual Rainfall:**
   - Plot comparing predicted rainfall with actual rainfall.

2. **Feature Importance:**
   - Graph showing the importance of each feature in the model.

3. **Training and Validation Error:**
   - A graph showing how the training and validation errors change as the model is trained.

## Contributing

Feel free to fork this repository, contribute, or report issues. Contributions are always welcome!

1. Fork the repository
2. Create a new branch
3. Make your changes
4. Commit your changes
5. Push to your forked repository
6. Create a pull request

## License

This project is licensed under the CSIR License - see the [LICENSE](LICENSE) file for details.
