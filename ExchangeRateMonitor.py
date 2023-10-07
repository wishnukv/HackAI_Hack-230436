
import requests
import sys
from dateutil.parser import parse 
import tkinter as tk
from tkinter import ttk
from ttkthemes import ThemedStyle
from tkinter import messagebox

from uagents import Agent, Context
timeragent = Agent(name="timeragent", seed="timeragent recovery phrase")
@timeragent.on_interval(period=300)
#function to give the notifications when it crosses the threshold value
async def timer(upper_threshold,lower_threshold):
	source_currency = source_currency_entry.get()
	destination_currency = destination_currency_entry.get()
	last_updated_datetime, exchange_rate = convert_currency_erapi(source_currency, destination_currency, amount)
	if exchange_rate > upper_threshold:
        	messagebox.showwarning("Warning", f"The exchange rate is above the upper threshold of {upper_threshold}")
	elif exchange_rate < lower_threshold:
		messagebox.showwarning("Warning", f"The exchange rate is below the lower threshold of {lower_threshold}")
upper_threshold=0.0
lower_threshold=0.0
source_currency=""
destination_currency=""
#function to get exchange rates from the api
def get_all_exchange_rates_erapi(src):
    url = f"https://open.er-api.com/v6/latest/{src}"
    data = requests.get(url).json()
    if data["result"] == "success":
        last_updated_datetime = parse(data["time_last_update_utc"])
        exchange_rates = data["rates"]
    return last_updated_datetime, exchange_rates
#to get the coversion  values with source, destination currencies
def convert_currency_erapi(src, dst, amount):
    last_updated_datetime, exchange_rates = get_all_exchange_rates_erapi(src)
    return last_updated_datetime, exchange_rates[dst] * amount
#function to make the conversion 
def convert():
    source_currency = source_currency_entry.get()
    destination_currency = destination_currency_entry.get()
    amount = float(amount_entry.get())
    upper_threshold = float(upper_threshold_entry.get())
    lower_threshold = float(lower_threshold_entry.get())

    last_updated_datetime, exchange_rate = convert_currency_erapi(source_currency, destination_currency, amount)
    result_label.config(text=f"Last updated datetime: {last_updated_datetime}")
    result_label.config(text=f"{amount} {source_currency} = {exchange_rate} {destination_currency}")

    # Check if the exchange rate exceeds the upper or lower threshold
    if exchange_rate > upper_threshold:
        messagebox.showwarning("Warning", f"The exchange rate is above the upper threshold of {upper_threshold}")
    elif exchange_rate < lower_threshold:
        messagebox.showwarning("Warning", f"The exchange rate is below the lower threshold of {lower_threshold}")
# code for gui implementation using tkinker
root = tk.Tk()
root.title("Currency Converter")

# Apply the Clam theme
style = ThemedStyle(root)
style.set_theme("clam")

source_currency_label = ttk.Label(root, text="Source Currency:")
source_currency_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")
source_currency_entry = ttk.Entry(root)
source_currency_entry.grid(row=0, column=1, padx=5, pady=5)
source_currency_entry.insert(0, "USD")

destination_currency_label = ttk.Label(root, text="Destination Currency:")
destination_currency_label.grid(row=1, column=0, padx=5, pady=5, sticky="w")
destination_currency_entry = ttk.Entry(root)
destination_currency_entry.grid(row=1, column=1, padx=5, pady=5)
destination_currency_entry.insert(0, "EUR")

amount_label = ttk.Label(root, text="Amount:")
amount_label.grid(row=2, column=0, padx=5, pady=5, sticky="w")
amount_entry = ttk.Entry(root)
amount_entry.grid(row=2, column=1, padx=5, pady=5)
amount_entry.insert(0, "1.0")

# Add the upper and lower threshold entries
upper_threshold_label = ttk.Label(root, text="Upper Threshold:")
upper_threshold_label.grid(row=3, column=0, padx=5, pady=5, sticky="w")
upper_threshold_entry = ttk.Entry(root)
upper_threshold_entry.grid(row=3, column=1, padx=5, pady=5)
upper_threshold_entry.insert(0, "0.0")

lower_threshold_label = ttk.Label(root, text="Lower Threshold:")
lower_threshold_label.grid(row=4, column=0, padx=5, pady=5, sticky="w")
lower_threshold_entry = ttk.Entry(root)
lower_threshold_entry.grid(row=4, column=1, padx=5, pady=5)
lower_threshold_entry.insert(0, "0.0")

convert_button = ttk.Button(root, text="Convert", command=convert)
convert_button.grid(row=5,columnspan=3)

result_label = ttk.Label(root,text="")
result_label.grid(row=6,columnspan=3)

root.mainloop()
#running the agent
if __name__ == "__main__":
    timeragent.run()
    
    
# this program uses api from exchangerates api 

