#
# Example file for working with date information
#
from datetime import date
from datetime import time
from datetime import datetime

def main():
  ## DATE OBJECTS
  # Get today's date from the simple today() method from the date class
  # today = date.today()
  # print("A data de hoje é ", today)

  # print out the date's individual components
  # print("Componentes da data: ", today.day, today.month, today.year)
  
  # retrieve today's weekday (0=Monday, 6=Sunday)
  # print("O dia da semana hoje é: ", today.weekday())
  # days=["mon", "tue", "wed", "thu", "fri", "sat", "sun"]
  # print("que é dia da semana: ", days[today.weekday()])
  
  ## DATETIME OBJECTS
  # Get today's date from the datetime class
  today = datetime.now()
  print("a data de hoje é: ", today)
  
  # Get the current time
  t= datetime.time(datetime.now())
  print("A hora exata de hoje é: ", t)

 

  
if __name__ == "__main__":
  main();
  