from forex_python.bitcoin import BtcConverter *
b = BtcConverter()  
b.get_latest_price('EUR')
import datetime,decimal

def get_latest_price():
    sum = 0
    b = BtcConverter() 
    for i in range(1,31):
        date_obj = datetime.datetime(2022, 1, i)
        sum += b.get_previous_price('EUR', date_obj)
        avg_bitcoin = sum
        print("Avg.Price : ", round(avg_bitcoin), "EUR")
        result = b.get_latest_price('EUR')
        print("Current Price: ", round(result), "EUR")
        increse = (result - avg_bitcoin)/avg_bitcoin * 100
        print("increse: ", round(increse), "%")
        break

get_bitcoin()
