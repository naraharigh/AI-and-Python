import pandas as pd
import numpy as np
import subprocess
import sys
import matplotlib.pyplot as plt
from statsmodels.tsa.seasonal import seasonal_decompose


def install_package(package_name):
    """Installs a Python package using pip."""
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", package_name])
        print(f"Successfully installed {package_name}")
    except subprocess.CalledProcessError as e:
        print(f"Error installing {package_name}: {e}")

# Example usage:
install_package("textblob")

# Generate synthetic data for customer suggestions
dates = pd.date_range(start='2023-01-01', periods=104, freq='W')
# Simulate a base number of weekly suggestions with an upward trend
suggestions = np.arange(104) * 0.5 + np.random.normal(50, 10, 104)
# Add some weekly seasonality
suggestions += 10 * np.sin(np.linspace(0, 4 * np.pi, 104))
# Ensure all counts are positive
suggestions[suggestions < 0] = 0

# Create a DataFrame
df = pd.DataFrame({'date': dates, 'suggestion_count': suggestions.round().astype(int)})
df.set_index('date', inplace=True)
print("Simulated Data Head:")
print(df.head())


# Plot the raw time series
plt.figure(figsize=(12, 6))
plt.plot(df.index, df['suggestion_count'])
plt.title('Customer Suggestions Over Time')
plt.xlabel('Date')
plt.ylabel('Number of Suggestions')
plt.grid(True)
plt.show()

# Decompose the time series into its components
decomposition = seasonal_decompose(df['suggestion_count'], model='additive', period=52) # Assuming yearly seasonality
fig = decomposition.plot()
fig.set_size_inches(12, 8)
plt.show()



from statsmodels.tsa.arima.model import ARIMA

# Split data into training and testing sets
train_size = int(len(df) * 0.8)
train_data = df[:train_size]
test_data = df[train_size:]

# Fit the ARIMA model (p,d,q parameters can be optimized)
model = ARIMA(train_data['suggestion_count'], order=(1, 1, 1))
fitted_model = model.fit()

# Make predictions on the test data
forecast_steps = len(test_data)
forecast = fitted_model.forecast(steps=forecast_steps)

# Plot the forecast
plt.figure(figsize=(12, 6))
plt.plot(train_data.index, train_data['suggestion_count'], label='Training Data')
plt.plot(test_data.index, test_data['suggestion_count'], color='orange', label='Test Data')
plt.plot(test_data.index, forecast, color='green', linestyle='--', label='Forecast')
plt.title('Customer Suggestions: ARIMA Forecast')
plt.xlabel('Date')
plt.ylabel('Number of Suggestions')
plt.legend()
plt.grid(True)
plt.show()


from textblob import TextBlob

# Assume we have a DataFrame with 'date' and 'suggestion_text' columns
# We will add a 'sentiment' column to our original synthetic data
df_text = df.copy()
df_text.reset_index(inplace=True)
df_text.rename(columns={'suggestion_count': 'suggestion_text'}, inplace=True)

# Generate some sample text data with varying sentiment
text_data = [
    "The new feature is amazing!", "I love this product.", "This is a great update.",
    "The product is okay, but could be better.", "I have mixed feelings.",
    "This is very disappointing.", "I'm very unhappy with the service.", "It has a lot of bugs."
] * (len(df_text) // 8)

# Pad the list if necessary
while len(text_data) < len(df_text):
    text_data.append("This is an average experience.")

df_text['suggestion_text'] = np.random.choice(text_data, size=len(df_text))

# Calculate sentiment scores for each suggestion
df_text['sentiment_score'] = df_text['suggestion_text'].apply(lambda text: TextBlob(text).sentiment.polarity)

# Aggregate sentiment by week for time series analysis
weekly_sentiment = df_text.resample('W', on='date')['sentiment_score'].mean()

# Plot the average sentiment over time
plt.figure(figsize=(12, 6))
plt.plot(weekly_sentiment.index, weekly_sentiment.values)
plt.title('Average Customer Sentiment Over Time')
plt.xlabel('Date')
plt.ylabel('Average Sentiment Score (Polarity)')
plt.axhline(y=0, color='r', linestyle='--') # Neutral line
plt.grid(True)
plt.show()

