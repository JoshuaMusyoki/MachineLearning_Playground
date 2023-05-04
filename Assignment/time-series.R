# An exampleof time series data
data <- c(10, 20, 30, 40, 50, 60)

# Create a time series object
ts_data <- ts(data, frequency = 1)

# Print the time series object
ts_data

# Example code to check if a time series is stationary using ADF test
library(tseries)

# Example time series data
data <- c(10, 20, 30, 40, 50, 60)

# Run ADF test
adf.test(data)

# Output:
# Augmented Dickey-Fuller Test
# 
# data:  data
# Dickey-Fuller = -1.775, Lag order = 0, p-value = 0.3928
# alternative hypothesis: stationary

# Example code to convert a non-stationary time series into a stationary time series
library(tseries)

# Example non-stationary time series data
non_stationary_data <- c(10, 20, 30, 40, 50, 60)

# Take the first difference of the time series data
stationary_data <- diff(non_stationary_data)

# Print the stationary time series object
stationary_data


# Example code to determine p and q of an ARIMA model
library(forecast)

# Example time series data
data <- c(10, 20, 30, 40, 50, 60)

# Determine the values of p and q
auto.arima(data)


