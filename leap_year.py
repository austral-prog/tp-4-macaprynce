def leap_year():

  year=int(input("ingrese un año:"))
  if (year%400==0):
    print("el año es bisiesto")
  elif (year%4==0 and year%100!=0):
    print("el año ingresado no es bisiesto")
  else:
    print("el año ingresado no es bisiesto")

leap_year() 
