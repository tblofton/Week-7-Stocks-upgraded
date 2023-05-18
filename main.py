stock_prices = { 
  'SPOT': 132.39,
  'TSLA': 158.48,
  'AMZN': 110.00, 
  'AMD': 86.77,
  'PINS': 27.73, 
  'BABA': 83.99, 
  'PLUG': 9.10, 
  'PFE': 38.38, 
  'T': 17.55, 
  'CCL': 8.84
}

def main():
  intro()
  
  while True:
    user_ticker = input('Please enter a ticker symbol: ').upper()
    
    if user_ticker in stock_prices:
      price = stock_prices[user_ticker]
      print(f"The current price of {user_ticker} is ${price}")
      
      invest = input(f'Would you like to invest in {user_ticker}? (y/n): ')
      
      if invest.lower() == 'y':
        investment = float(input('How much would you like to invest?: '))
        number_of_stocks = int(investment // price)
        print(f'You can buy {number_of_stocks} stocks of {user_ticker} at the current price.')
      else:
        print('Thank you!')
        print('Good-Bye!')
        break
        
    else:
      print(f"Sorry, {user_ticker} was not found among Trending Tickers.")
      print('Please try again!')
      print()
  
    more_search = input('Would you like to search for more stocks? (y/n): ')
    
    if more_search.lower() == 'n':
      print('Thank you!')
      print('Good-Bye!')
      break

def intro(): 
  print('Hello!')
  print('Use this program to search Trending Tickers')
  print()
  
main()