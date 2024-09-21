from datetime import date
import forex_python.converter


year = int(input("please enter bitcoin Buying  year as number:"))

month = int(input("please enter bitcoin Buying month as number:")) 

day = int(input("please enter bitcoin Buying day as number:"))

amount = float(input("please enter the amount of dollars you paid: "))

buy_date = date(year, month, day)


bitcoin_buy_price = get_bitcoin_price_on_date(buy_date)

bitcoin_past_amount = amount / bitcoin_buy_price

c = forex_python.converter.CurrencyRates()
bitcoin_now_price = c.get_rate('USD', 'BTC')

now_imaginary_amount = bitcoin_now_price * bitcoin_past_amount

print("if you bought bitcoin on ", day, "/", month, "/", year, "for", amount, "dollars, you would have had", now_imaginary_amount, "dollars right now" )

