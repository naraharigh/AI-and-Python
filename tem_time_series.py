import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import subprocess
import sys
from statsmodels.tsa.seasonal import seasonal_decompose
from statsmodels.tsa.statespace.sarimax import SARIMAX



def install_package(package_name):
    """Installs a Python package using pip."""
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", package_name])
        print(f"Successfully installed {package_name}")
    except subprocess.CalledProcessError as e:
        print(f"Error installing {package_name}: {e}")

# Example usage:
# install_package("sklearn")


# Generate synthetic weather data (daily temperature)
dates = pd.date_range(start='2020-01-01', end='2024-12-31', freq='D')
n_points = len(dates)

# Create a clear trend and yearly seasonality
trend = np.linspace(0, 5, n_points)
seasonality = 15 * np.sin(2 * np.pi * dates.dayofyear / 365.25)
noise = np.random.normal(0, 2, n_points)
temperature = 10 + trend + seasonality + noise

# Create a DataFrame
df = pd.DataFrame({'temperature': temperature}, index=dates)

print("Simulated Weather Data Head:")
print(df.head())


# Plot the raw time series
plt.figure(figsize=(12, 6))
plt.plot(df.index, df['temperature'])
plt.title('Daily Temperatures Over Time (Simulated)')
plt.xlabel('Date')
plt.ylabel('Temperature (°C)')
plt.grid(True)
plt.show()

# Decompose the time series
decomposition = seasonal_decompose(df['temperature'], model='additive', period=365)
fig = decomposition.plot()
fig.set_size_inches(12, 8)
plt.show()


# Split the data into training and testing sets
train_end = '2024-06-30'
train_data = df.loc[:train_end, 'temperature']
test_data = df.loc[train_end:, 'temperature']

# Define and fit the SARIMA model
# (p, d, q) are non-seasonal parameters
# (P, D, Q, S) are seasonal parameters (S=365 for daily data)
model = SARIMAX(train_data, order=(1, 1, 1), seasonal_order=(1, 1, 1, 365))
fitted_model = model.fit(disp=False)

# Make predictions on the test data
start = len(train_data)
end = len(train_data) + len(test_data) - 1
predictions = fitted_model.predict(start=start, end=end, dynamic=False)

# Evaluate the model
# from sklearn.metrics import mean_squared_error
# rmse = np.sqrt(mean_squared_error(test_data, predictions))
# print(f"Root Mean Squared Error (RMSE): {rmse:.2f}")

# Plot the predictions vs actual data
plt.figure(figsize=(12, 6))
plt.plot(train_data.index, train_data.values, label='Training Data')
plt.plot(test_data.index, test_data.values, color='orange', label='Actual Test Data')
plt.plot(test_data.index, predictions.values, color='green', linestyle='--', label='SARIMA Predictions')
plt.title('SARIMA Forecast vs. Actual Temperatures')
plt.xlabel('Date')
plt.ylabel('Temperature (°C)')
plt.legend()
plt.grid(True)
plt.show()


# Forecast future temperatures for the next 6 months
forecast_steps = 365 // 2  # 6 months
forecast = fitted_model.get_forecast(steps=forecast_steps)
forecast_df = forecast.summary_frame()

# Plot the forecast
plt.figure(figsize=(12, 6))
plt.plot(df.index, df['temperature'], label='Historical Data')
plt.plot(forecast_df.index, forecast_df['mean'], color='red', linestyle='--', label='Future Forecast')
plt.fill_between(forecast_df.index,
                 forecast_df['mean_ci_lower'],
                 forecast_df['mean_ci_upper'],
                 color='pink', alpha=0.3, label='Confidence Interval')
plt.title('Weather Forecast for the Next 6 Months')
plt.xlabel('Date')
plt.ylabel('Temperature (°C)')
plt.legend()
plt.grid(True)
plt.show()
