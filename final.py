import speech_recognition as sr
import pyttsx3
import datetime
import os
import random
import wikipedia
import webbrowser
import calendar
import subprocess
import requests
import smtplib
import pyjokes
import winshell
import pywhatkit as kit
from selenium import webdriver
import warnings
from time import sleep


from selenium.webdriver.common.by import By
warnings.filterwarnings("ignore")

engine = pyttsx3.init('sapi5')
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)

def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()

def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        r.phrase_threshold = 1
        audio = r.listen(source, timeout=5, phrase_time_limit=5)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said: {query}")


    except sr.WaitTimeoutError as e:
        print("Timeout; {0}".format(e))
    except Exception as e:
        speak("say that again please...")
        return "none"

    return query



def wish():
    hour = int(datetime.datetime.now().hour)

    if hour>=0 and hour<=12:
        speak("good morning")
    elif hour>12 and hour<18:
        speak("good afternoon")
    else:
        speak("good evening")
    speak("i am galaxy. please tell me how can i help you")

def today_date():
    now = datetime.datetime.now()
    date_now = datetime.datetime.today()
    week_now = calendar.day_name[date_now.weekday()]
    month_now = now.month
    day_now = now.day

    months = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December",
    ]

    ordinals = [
        "1st",
        "2nd",
        "3rd",
        "4th",
        "5th",
        "6th",
        "7th",
        "8th",
        "9th",
        "10th",
        "11th",
        "12th",
        "13th",
        "14th",
        "15th",
        "16th",
        "17th",
        "18th",
        "19th",
        "20th",
        "21st",
        "22nd",
        "23rd",
        "24th",
        "25th",
        "26th",
        "27th",
        "28th",
        "29th",
        "30th",
        "31st",
    ]

    return "Today is " + week_now + ", " + months[month_now - 1] + " the " + ordinals[day_now - 1] + "."

def note(text):
    date = datetime.datetime.now()
    file_name = str(date).replace(":", "-") + "-note.txt"
    with open(file_name, "w") as f:
        f.write(text)

    subprocess.Popen(["notepad.exe", file_name])

def send_email(to, content):
    server = smtplib.SMTP("smtp.gmail.com", 587)

    server.ehlo()
    server.starttls()

    # Enable low security in gmail
    server.login("email", 'pass')
    server.sendmail("email", to, content)
    server.close()

def pizza():
    driver = webdriver.Chrome(r"C:\...\chromedriver.exe") # location of your webdriver
    driver.maximize_window()
    speak("Opening Dominos")

    driver.get('https://www.dominos.co.in/') # open the site
    sleep(2)

    speak("Getting ready to order")
    driver.find_element(by=By.LINK_TEXT, value="ORDER ONLINE NOW").click() # click on order now button
    sleep(2)

    speak("Finding your location")
    driver.find_element(by=By.CLASS_NAME, value="srch-cnt-srch-inpt").click() # click on the location search
    sleep(2)

    location = "" # Enter your location

    speak("Entering your location")
    driver.find_element(by=By.XPATH,
        value="//*[@id='__next']/div/div[1]/div[2]/div/div[1]/div/div[3]/div/div[1]/div[2]/div[1]/div[1]/input"
    ).send_keys(location) # send text to location search input field
    sleep(2)

    driver.find_element(by=By.CLASS_NAME, value="lst-wrpr").click()
    sleep(10)

    try:
       driver.find_element(by=By.CLASS_NAME, value="prf-grp-txt").click()
       sleep(10)
    except:
        speak("your location could not be found, please try again later")
        exit()

    speak("Logging in")
    phone_num = "" # Enter your phone number

    driver.find_element(by=By.XPATH,
     value="//*[@id='__next']/div/div/div[1]/div[1]/div/div[3]/div[3]/div[2]/div/div[3]/div/div/div/div[2]/div/form/div[1]/div[2]/input").send_keys(phone_num)
    sleep(2)

    driver.find_element(by=By.XPATH,
     value="//*[@id='__next']/div/div/div[1]/div[1]/div/div[3]/div[3]/div[2]/div/div[3]/div/div/div/div[2]/div/form/div[2]/input").click()
    sleep(2)

    speak("what is your OTP")
    sleep(5)

    otp_log = take_command()

    driver.find_element(by=By.XPATH,
     value="//*[@id='__next']/div/div/div[1]/div[1]/div/div[3]/div[3]/div[2]/div/div[3]/div/div/div/div[2]/div/div/div/div[1]/input").send_keys(
         otp_log) # paste the OTP into the text field
    sleep(2)

    driver.find_element(by=By.XPATH,
        value="//*[@id='__next']/div/div/div[1]/div[1]/div/div[3]/div[3]/div[2]/div/div[3]/div/div/div/div[2]/div/div/div/div[2]/div[2]/button/span"
    ).click() # summit OTP
    sleep(2)

    speak("Do you want me to order from your favorites?")
    query_fav = take_command()

    if "yes" in query_fav:
        try:
            driver.find_element(by=By.XPATH,
               value="//*[@id='mn-lft']/div[2]/div/div[3]/div/div/div[2]/div[3]/div/button/span"
            ).click() # Add your favorite pizza
            sleep(1)
        except:
            speak("the entered OTP is incorrect.")
            exit()

        speak("Adding your favourites to cart")

        speak("Do you want me to add extra cheese to your pizza?")
        ex_cheese = take_command()
        if "yes" in ex_cheese:
            speak("Extra cheese added")
            driver.find_element(by=By.XPATH,
               value="//*[@id='mn-lft']/div[2]/div/div[1]/div/div/div[2]/div[3]/div[2]/button/span"
            ).click() # Add extra cheese
        elif "no" in ex_cheese:
            driver.find_element(by=By.XPATH,
                value="//*[@id='mn-lft']/div[2]/div/div[1]/div/div/div[2]/div[3]/div[1]/button/span"
            ).click()
        else:
            speak("I don't know that")
            driver.find_element(by=By.XPATH,
                 value="//*[@id='mn-lft']/div[2]/div/div[1]/div/div/div[2]/div[3]/div[1]/button/span"
            ).click()

        driver.find_element(by=By.XPATH,
             value="//*[@id='mn-lft']/div[10]/div/div[2]/div/div/div[2]/div[2]/div/button/span"
        ).click() # Add a pepsi
        sleep(2)

        speak("Would you like to increase the quantity?")
        qty = take_command()
        qty_pizza = 0
        qty_pepsi = 0
        if "yes" in qty:
            speak("Would you like to increase the quantity of pizza?")
            wh_qty = take_command()
            if "yes" in wh_qty:
                speak("How many more pizzas would you like to add? ")
                try:
                    qty_pizza = take_command()
                    qty_pizza = int(qty_pizza)
                    if qty_pizza > 0:
                        talk_piz = f"Adding {qty_pizza} more pizzas"
                        speak(talk_piz)
                        for i in range(qty_pizza):
                            driver.find_element(by=By.XPATH,
                               value="//*[@id='__next']/div/div/div[1]/div[2]/div[2]/div[2]/div[2]/div/div/div[1]/div/div/div/div[2]/div/div/div[2]/div"
                            ).click()
                except:
                    speak("I don't know that")
            else:
                pass

            speak("Would you like to increase the quantity of pepsi?")
            pep_qty = take_command()
            if "yes" in pep_qty:
                speak("How many more pepsis would you like to add? ")
                try:
                    qty_pepsi = take_command()
                    qty_pepsi = int(qty_pepsi)
                    if qty_pepsi > 0:
                        talk_pep = f"Adding {qty_pepsi} more pepsis"
                        speak(talk_pep)
                        for i in range(qty_pepsi):
                            driver.find_element(by=By.XPATH,
                                value="//*[@id='__next']/div/div/div[1]/div[2]/div[2]/div[2]/div[2]/div/div/div[1]/div[2]/div/div/div[2]/div/div/div[2]/div"
                            ).click()
                except:
                    speak("I don't know that")
            else:
                 pass
        elif "no" in qty:
            pass

        total_pizza = qty_pizza + 1
        total_pepsi = qty_pepsi + 1
        tell_num = f"this is your list of orders. {total_pizza} Pizzas and {total_pepsi} Pepsis. Do you want to checkout?"
        speak(tell_num)
        check_order = take_command()
        if "yes" in check_order:
            speak("checking out")
            driver.find_element(by=By.XPATH,
                value="//*[@id='__next']/div/div/div[1]/div[2]/div[2]/div[2]/div[2]/div/div/div[2]/div[2]/button/span"
            ).click() # click on checkout button
            sleep(2)
            total = driver.find_element(by=By.XPATH,
                        value="//*[@id='__next']/div/div[1]/div[2]/div[3]/div[2]/div/div[6]/div/div/div[5]/span[2]/span"
            )
            total_price = f'total price is {total.text}'
            speak(total_price)
            sleep(2)
        else:
            exit()

        speak("Placing your order")
        driver.find_element(by=By.XPATH,
            value="//*[@id='__next']/div/div[1]/div[2]/div[3]/div[2]/div/div[6]/div/div/div[7]/button/span"
        ).click() # click on place order button
        sleep(4)

        try:
         speak("add address")

         driver.find_element(by=By.XPATH,
            value="//*[@id='__next']/div/div[1]/div[2]/div[3]/div[2]/div/div[3]/div/div[3]/div/div/form/div/div[1]/div[1]/div/input"
         ).click()
         sleep(3)

         first_name = "" # Your first name

         driver.find_element(by=By.XPATH,
            value="//*[@id='__next']/div/div[1]/div[2]/div[3]/div[2]/div/div[3]/div/div[3]/div/div/form/div/div[1]/div[1]/div/input"
         ).send_keys(first_name)
         sleep(3)

         driver.find_element(by=By.XPATH,
            value="//*[@id='__next']/div/div[1]/div[2]/div[3]/div[2]/div/div[3]/div/div[3]/div/div/form/div/div[1]/div[2]/div/input"
         ).click() # Add your first name
         sleep(3)

         last_name = "" # your last name

         driver.find_element(by=By.XPATH,
            value="//*[@id='__next']/div/div[1]/div[2]/div[3]/div[2]/div/div[3]/div/div[3]/div/div/form/div/div[1]/div[2]/div/input"
         ).send_keys(last_name) 
         sleep(3)

         driver.find_element(by=By.XPATH,
            value="//*[@id='__next']/div/div[1]/div[2]/div[3]/div[2]/div/div[3]/div/div[3]/div/div/form/div/div[2]/div/div/input"
         ).click() # Add your last name
         sleep(3)

         e_mail = "" # your e_mail

         driver.find_element(by=By.XPATH,
            value="//*[@id='__next']/div/div[1]/div[2]/div[3]/div[2]/div/div[3]/div/div[3]/div/div/form/div/div[2]/div/div/input"
         ).send_keys(e_mail) 
         sleep(3)

         driver.find_element(by=By.XPATH,
            value="//*[@id='__next']/div/div[1]/div[2]/div[3]/div[2]/div/div[3]/div/div[3]/div/div/form/div/div[3]/div[1]/div/input"
         ).click() # Add your email
         sleep(3)

         addr = "" # your address

         driver.find_element(by=By.XPATH,
            value="//*[@id='__next']/div/div[1]/div[2]/div[3]/div[2]/div/div[3]/div/div[3]/div/div/form/div/div[3]/div[1]/div/input"
         ).send_keys(addr)
         sleep(3)

         driver.find_element(by=By.XPATH,
            value="//*[@id='__next']/div/div[1]/div[2]/div[3]/div[2]/div/div[3]/div/div[3]/div/div/form/div/div[3]/div[2]/div/input"
         ).click() # Add address
         sleep(3)

         house_no = "" # your house no.

         driver.find_element(by=By.XPATH,
            value="//*[@id='__next']/div/div[1]/div[2]/div[3]/div[2]/div/div[3]/div/div[3]/div/div/form/div/div[3]/div[2]/div/input"
         ).send_keys(house_no) # Add house no.
         sleep(3)


         speak("saving your location")
         driver.find_element(by=By.XPATH,
            value="//*[@id='__next']/div/div[1]/div[2]/div[3]/div[2]/div/div[3]/div/div[3]/div/div/div[3]/div/div/input"
         ).click() # save your location
         sleep(2)
        except:
            speak("store is currently offline.")

        speak("Do you want to confirm your order?")
        confirm = take_command()
        if "yes" in confirm:
            speak("placeing your order")
            driver.find_element(by=By.XPATH,
                value="//*[@id='__next']/div/div[1]/div[2]/div/div[1]/div[2]/div/div[2]/div/div[2]/button"
            ).click() # Place order
            sleep(2)
            speak("Your order is places successfully. Wait for Dominos to deliver your order. Enjoy your day!")
        else:
            exit()

    else:
        exit()




if __name__ == "__main__":
    wish()
    while True:


        query = take_command().lower()

        #logic building for tasks

        if "open notepad" in query:
            npath = "C:\...." # Notepad link
            os.startfile(npath)

        elif "open command prompt" in query:
            os.system("start cmd")

        elif "date" in query or "day" in query or "month" in query:
            get_today = today_date()
            speak(" " + get_today)

        elif "time" in query:
            now = datetime.datetime.now()
            meridiem = ""
            if now.hour >= 12:
                meridiem = "p.m"
                hour = now.hour - 12
            else:
                meridiem = "a.m"
                hour = now.hour

            if now.minute < 10:
                minute = "0" + str(now.minute)
            else:
                minute = str(now.minute)
            speak(" " + "It is " + str(hour) + ":" + minute + " " + meridiem + " .")

        elif "play music" in query:
            music_dir = "C\..." # Any Music link
            songs = os.listdir(music_dir)
            rd = random.choice(songs)
            os.startfile(os.path.join(music_dir, rd))

        elif "wikipedia" in query:
            speak("searching wikipedia...")
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query, sentences=2)
            speak("according to wikipedia")
            speak(results)
            print(results)

        elif "youtube" in query.lower():
            ind = query.lower().split().index("youtube")
            search = query.split()[ind + 1:]
            webbrowser.open(
                "http://www.youtube.com/results?search_query=" +
                "+".join(search)
            )
            speak("Opening " + str(search) + " on youtube")


        elif "open google" in query:
            speak("what should i search on google")
            cm = take_command().lower()
            webbrowser.open(f"{cm}")

        elif "who are you" in query or "define yourself" in query:
            speak("Hello, I am an Galaxy. Your Assistant. I am here to make your life easier. You can command me to perform various tasks such as asking questions or opening applications etcetera")

        elif "made you" in query or "created you" in query:
            speak("I was created by YOUR NAME")

        elif "your name" in query:
            speak("My name is Galaxy")

        elif "why do you exist" in query or "why did you come to this word" in query:
            speak("It is a secret")

        elif "how are you" in query:
            speak("I am awesome, Thank you")
            speak("\nHow are you?")

        elif "fine" in query or "good" in query:
            speak("It's good to know that your fine")

        elif "exit" in query or "quit" in query:
            speak("thanks for using me, have a good day")
            exit()

        elif "make a note" in query:
            speak("What would you like me to write down?")
            note_text = take_command()
            note(note_text)
            speak("I have made a note of that.")

        elif "what is the weather in" in query:
            key = "c6a1963e86c5e6a51f290480743c03c3"
            weather_url = "https://api.openweathermap.org/data/2.5/weather?"
            ind = query.split().index("in")
            location = query.split()[ind + 1:]
            location = "".join(location)
            url = weather_url + "appid=" + key + "&q=" + location
            js = requests.get(url).json()
            if js["cod"] != "404":
                weather = js["main"]
                temperature = weather["temp"]
                temperature = temperature - 273.15
                humidity = weather["humidity"]
                desc = js["weather"][0]["description"]
                weatherResponse = " The temperature in Celcius is " + str(temperature) + " The humidity is " + str(
                    humidity) + " and The weather description is " + str(desc)
                speak(weatherResponse)
            else:
                speak("City Not Found")

        elif "send email" in query:
            try:
                speak("What should I say?")
                content = take_command().lower()
                speak("whom should i send")
                to = input("Enter To Address: ")


                send_email(to, content)
                speak("Email has been sent !")
            except Exception as e:
                print(e)
                speak("I am not able to send this email")

        elif "open" in query.lower():
            if "chrome" in query.lower():
                speak("Opening Google Chrome")
                os.startfile(
                    r"C:\..." #Chrome Application link
                )

            elif "vs code" in query.lower():
                   speak("Opening Visual Studio Code")
                   os.startfile(
                        r"C:\..." # VS Code link
                   )

            elif "youtube" in query.lower():
                speak("Opening Youtube\n")
                webbrowser.open("https://youtube.com/")

            else:
                speak("Application not available")

        elif "search" in query.lower():
            ind = query.lower().split().index("search")
            search = query.split()[ind + 1:]
            webbrowser.open(
                "https://www.google.com/search?q=" + "+".join(search))
            speak("Searching " + str(search) + " on google")


        elif "joke" in query:
            speak(pyjokes.get_joke())

        elif "empty recycle bin" in query:
            winshell.recycle_bin().empty(
                confirm=True, show_progress=False, sound=True
            )
            speak("Recycle Bin Emptied")

        elif "send message" in query:
            kit.sendwhatmsg_instantly("  ", "call me urgent") # Add contact number

        elif "where is" in query:
            ind = query.lower().split().index("is")
            location = query.split()[ind + 1:]
            url = "https://www.google.com/maps/place/" + "".join(location)
            speak("This is where " + str(location) + " is.")
            webbrowser.open(url)

        elif "order a pizza" in query or "pizza" in query:
            pizza()