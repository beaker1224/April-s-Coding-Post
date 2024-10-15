print("Welcome to our app! This app is made to help you quit your addictions to bad things. ")
addiction = input("What is your addiction? (Like smoking, drinking, vaping, etc.) ")

if addiction == "drinking":
    print("Ok, I see. ")
Q1 = input("Would you like to know the pros and cons of drinking, or would you like help to break your drinking habit? (a = pros and cons, b = breaking drinking habit.) ")

if Q1 == "a":
    quit = input("Ok, the pros for drinking is that you might feel really relaxed. This is actually one of the main reasons that people drink. Some people feel stressed out, and they might want to escape their problems. But, this might cause a severe aftermath. If you start drinking too much, it might increase the chances of stroke and heart disease. Would you like to know how to stop drinking if you started? (yes/no) ")
if Q1 == "b":
   quit = input("So you want to quit drinking, right? Well, I understand it might be hard. We suggest you try drinking smaller amounts of alcohol, or to try to see a doctor about it. We're rooting for you! (Press 'enter' or 'return' to quit this app.) ")
if quit == "yes":
    print("So you want to quit drinking, right? Well, I understand it might be hard. We suggest you try drinking smaller amounts of alcohol, or to try to see a doctor about it. We're rooting for you! ")
if quit == "no":
    print("Ok, thank you for trying our app! We hope you were satisfied with the responses. ")

#-----second part (smoking)-----#
if addiction == "smoking":
    print("Ok, I see. ")
Q2 = input("Would you like to know the pros and cons of smoking, or would you like help to break your smoking habit? (a = pros and cons, b = smoking/drinking habit.) ")

if Q2 == "a":
    quit2 = input("Ok, the pros for smoking is that you might feel really good when doing it. The nicotine changes the system in your brain to give you more dopamine, making you feel really relaxed. Now, you might be thinking of smoking, but just because it feels good, doesn't mean it is good. Smoking causes severe lung problems, and might increase the odds of getting cancer and diabetes. Would you like to quit smoking if you started? (yes/no) ")
if Q2 == "b":
    quit2 = input("So you want to quit smoking, right? Well, I understand it might be hard. We suggest you try to see a professional about it, but you must listen to the doctor. Remember, it's never too late to quit smoking! (Press 'enter' or 'return' to quit this app.)")
if quit2 == "yes":
    print("So you want to quit smoking, right? Well, I understand it might be hard. We suggest you try to see a professional about it, but you must listen to the doctor. Remember, it's never too late to quit smoking! ")
if quit2 == "no":
    print("Ok, thank you for trying our app! We hope you were satisfied with the responses. ")
#-----third part (vaping)-----#