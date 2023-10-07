# Currency Exchange Rate Notifier
Currency Exchange Monitor & Alert Agent is a user-friendly tool that is designed to help users to interact with the Exchange Rates .This application has used  uAgent libraries to create and to be informed about the changes in  currency rates .

Currency Exchange Monitor and Alert system is a software solution built using the uAgent library, designed to provide users with real-time currency exchange rate monitoring and customised alerts. the following are the key features it provides:
flexibility in choosing currency, Users can conveniently choose a currency they wish to monitor according to their preference. it allows u to choose one or more foreign currencies. the system ensures to provide you with timely accurate updates in the exchange rate data. it helps you to retrieve even the minute changes in the data. we provide a seamless connection with the currency exchange API. 
users can conveniently personalise and set their preferred thresholds for the alerts. users can input the preferred values to obtain alerts in real time. the rates are monitored in real time providing you with a reliable information to make timely decisions.

This Python script allows you to monitor currency exchange rates and receive notifications when they cross certain threshold values. It uses the ExchangeRates API to fetch the latest exchange rates and a simple GUI implemented using Tkinter for user interaction.

## Prerequisites

Before running this script, make sure you have the following prerequisites installed:
- Python 3
- Requests library (install it using `pip install requests`)
- Tkinter (usually included with Python installations)
- uAgents library(install it using `pipenv install uagents`


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
