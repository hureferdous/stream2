while True:
       try:
           number = int(input("what's your fav number hoss?\n"))
           print(18/number)
           break
       except ValueError:
           print("make sure and center a number")
       except ZeroDivitionError:
           print("Don't pick zero")
       except:
             break
       finally:
              print("loop complete")