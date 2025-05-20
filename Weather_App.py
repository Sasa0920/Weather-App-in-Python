import requests
import tkinter as tk
from PIL import Image,ImageTk


def get_weather():

  city_name=city_entry.get()
  api_key="ae210187f4c35aa11053d145bd62334e"
  url=f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&units=metric"

  response=requests.get(url)

  print(response.status_code)
  print(response.json())


  if response.status_code==200:
    data=response.json()
    temperature=data["main"]["temp"]
    pressure=data["main"]["pressure"]
    humidity=data["main"]["humidity"]
    temp_min=data["main"]["temp_min"]
    temp_max=data["main"]["temp_max"]
    weather_description=data["weather"][0]["description"]

    #print(f"Temperature : {temperature}°C")
    #print(f"Pressure : {pressure}hPa")
    #print(f"Humidity : {humidity}%")
    #print(f"Minimum Temperature : {temp_min}°C")
    #print(f"Maximum Temperature : {temp_max}°C")
    #print(f"Weather Description : {weather_description}")

    weather_text=(
      f"Temperature : {temperature}°C\n"
      f"Pressure : {pressure}hPa\n"
      f"Humidity : {humidity}%\n"
      f"Minimum Temperature : {temp_min}°C\n"
      f"Maximum Temperature : {temp_max}°C\n"
      f"Weather Description : {weather_description}"
    )
    weather_info.config(text=weather_text)

  else:
    #print("City is not found.Please try again.")
    weather_info.config(text="City is not found.Please try again.")
#if __name__=="__main__":
#  city_name=input("Enter the city name: ")
#  print(f"Now,you can see the current weather details of {city_name}")
#  get_weather()
  

#GUI design

root = tk.Tk()
root.title("Weather App")
root.geometry("500x400")
root.config(bg="white")

left_frame=tk.Frame(root,width="250",height="400",bg="#d2c3ff")
left_frame.pack(side="left")

image=Image.open("background.png")
image=image.resize((130,130))
weather_image=ImageTk.PhotoImage(image)

image_label=tk.Label(root,image=weather_image,bg="#d2c3ff")
image_label.place(x=55,y=70)

label=tk.Label(root,text="Weather App",bg="#d2c3ff",font=("Helvetica", 18,"bold"),fg="#815bf6")
label.pack()
label.place(x=50,y=250)

entry_label=tk.Label(root,text="Enter the city name : ",bg="white",font=("Helvetica", 14,"bold"),fg="#815bf6")
entry_label.pack()
entry_label.place(x=280,y=70)

city_entry=tk.Entry(root,bg="#e6ddfd")
city_entry.pack(pady=30)
city_entry.place(x=310,y=120)

button=tk.Button(root,text="Get Weather",command=get_weather,bg="#815bf6",fg="white",width="20")
button.pack()
button.place(x=300,y=170)

weather_info=tk.Label(root,text="",bg="white",width="25",height="10",fg="blue")
weather_info.pack()
weather_info.place(x=285,y=210)

root.mainloop()
  
