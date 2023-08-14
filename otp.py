from email.message import EmailMessage
from tkinter import *
from tkinter.ttk import *
import random
import smtplib


#the email and the password of the sender   
email_sender = 'e971162@gmail.com'
passes = 'znwyumbfknquecqw'
#to create the OTP number
OTP = ''.join(str(random.randint(0,9)) for i in range(6))


def connection():
    reciever = get_mail.get()
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(email_sender, passes)
    server.sendmail(email_sender, reciever, OTP)     
    server.quit()
    print("OTP is sent successfully")
   
def check_OTP():
    code = get_code.get()
    if OTP == code:
       a = Label(window, text="Successful verification!", background="yellowgreen", foreground="green", font="Arial 22 bold").place(x=150,y=275)
    else :
      a = Label(window, text="Failed to verify", background="yellowgreen", foreground="red", font="Arial 22 bold").place(x=190,y=275)
      
#create the window
window = Tk(className='Verification')
window.geometry("600x350")
window.configure(background='yellowgreen')
#to get the email of the reciever
label_email = Label(window , text="Write your email:" , background='green', foreground='white' , font='Arial 18 bold').place(x=15,y=40)
get_mail = StringVar()
write_email = Entry(window ,textvariable= get_mail ,background="white" , foreground="green" , width=27 , font='Arial 17 bold').place(x=230,y=40)

send_button = Button(window , text="SEND ME OTP" , width=20, command=connection ).place(x=230,y=110)
#to write the recieved OTP 
label_code = Label(window, text='recieved OTP:', background='green', foreground='white', font='Arial 16 bold').place(x=100,y=180)
get_code = StringVar()
write_code = Entry(window ,textvariable=get_code ,background='white', foreground='green', width=16, font='Arial 15 bold').place(x=260,y=180)

verify_button = Button(window, text='verify',command=check_OTP ,width=15).place(x=250,y=240)


window.mainloop()
