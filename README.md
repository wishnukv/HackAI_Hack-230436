# Currency Exchange Rate Notifier

This Python script allows you to monitor currency exchange rates and receive notifications when they cross certain threshold values. It uses the ExchangeRates API to fetch the latest exchange rates and a simple GUI implemented using Tkinter for user interaction.

## Prerequisites

Before running this script, make sure you have the following prerequisites installed:
- Python 3.x
- Requests library (install it using `pip install requests`)
- Tkinter (usually included with Python installations)

## Getting Started

1. Clone this repository to your local machine or download the script.

2. install pipenv and install uagents along with it 

3. Run the script:

4. The GUI will open, allowing you to enter the source currency, destination currency,upper threshold,lower threshold and amount for conversion. The script will continuously monitor the exchange rate and notify you if it crosses the specified thresholds.

## Features

- Fetches the latest exchange rates from the ExchangeRates API.
- Provides a GUI for user input and interaction.
- Sends notifications when the exchange rate crosses the upper or lower thresholds.

## Notes

- This program uses data from the ExchangeRates API. Ensure you have a stable internet connection for accurate exchange rate information.

