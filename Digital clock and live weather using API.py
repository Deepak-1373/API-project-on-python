import requests, json 
from time import *
from tkinter import *  

api_key = "8d479be2eaa5a82cbb089191160cda0c"
  

base_url = "http://api.openweathermap.org/data/2.5/weather?"
  

city_name = "delhi"

complete_url = base_url + "appid=" + api_key + "&q=" + city_name 
  
# get method of requests module 
# return response object 
response = requests.get(complete_url) 
  
# json method of response object  
# convert json format data into 
# python format data 
x = response.json() 
  
# Now x contains list of nested dictionaries 
# Check the value of "cod" key is equal to 
# "404", means city is found otherwise, 
# city is not found 
if x["cod"] != "404": 
  
  
    y = x["main"] 
  
   
    current_temperature = y["temp"] 
  
 
    current_pressure = y["pressure"] 
   
    current_humidiy = y["humidity"] 
  
    z = x["weather"] 
    weather_description = z[0]["description"] 
    
temp=str(current_temperature)
press= str(current_pressure) 
humid=str(current_humidiy)
a=str(weather_description)


 
window = Tk()
 
window.title("weather")
window.geometry('500x300')
window.config(bg='yellow')



lbl = Label(window, text=" ",font=("Arial Bold", 14),bg='yellow')
lbl.grid(column=0, row=6)

 
  
lbl = Label(window, text="The Current temperature in Kelvin= ",font=("Arial Bold", 14),bg='yellow')
lbl.grid(column=16, row=2)
lbl = Label(window, text=temp,font=("Arial Bold", 14),bg='yellow')
lbl.grid(column=20, row=2)



lbl = Label(window, text="The current pressure in pha unit is = ",font=("Arial Bold", 14),bg='yellow')
lbl.grid(column=16, row=3) 
lbl = Label(window, text=press,font=("Arial Bold", 14),bg='yellow')
lbl.grid(column=20, row=3) 



lbl = Label(window, text="The current humidity in percentage is = ",font=("Arial Bold", 14),bg='yellow')
lbl.grid(column=16, row=4)
lbl = Label(window, text=humid,font=("Arial Bold", 14),bg='yellow')
lbl.grid(column=20, row=4) 


lbl = Label(window, text="The weather is ",font=("Arial Bold", 14),bg='yellow')
lbl.grid(column=16, row=5)
lbl = Label(window, text=a,font=("Arial Bold", 14),bg='yellow')
lbl.grid(column=20, row=5)


lbl = Label(window, text="The current time   ",font=("Arial Bold", 14),bg='yellow')
lbl = Label(window, font=('calibri', 40, 'bold'),background='yellow',foreground='blue')
lbl.grid(column=16, row=0) 
 
 
string = strftime('%H:%M:%S %p')
lbl.config(text=string)
lbl.after(1000, time)


window.mainloop()    
