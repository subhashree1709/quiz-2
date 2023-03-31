import socket
from threading import Thread
from tkinter import *

nickname= input('CHOOSE YOUR NICKNAME: ')

client= socket.socket(socket.AF_INET,socket.SOCK_STREAM)
ip_address= '127.0.0.1'
port= 8000
client.connect((ip_address,port))

print('connected to server...')


def write():
    while True:
        message= '{}: {}'.format(nickname,input(''))
        client.send(message.encdoe('utf-8'))

recieve_thread= Thread(target=recieve)
recieve_thread.start()
write_thread= Thread(target=write)
write_thread.start()

class GUI:
    def __init__(self):
        self.Window()= Tk()
        self.Window.withdraw()

        self.login= Toplevel()
        self.login.title('login')


    def recieve(self):
      while True:
        try:
            message= client.recv(2048).decode('utf-8')
            if message== 'NICKNAME':
                client.send(self.name.encode('utf-8'))
            else :
                print(message)
        except:
            print('an error occured')
            client.close()
            break

self.Window.configure(bg= 'lightblue')
self.Window.resize(300,300)

login_label= Label(self.Window,text='Please login to continue',fg='black',bg='lightblue',font=('Helvetica 14 bold',12),bd=1)
login_label.place(x=140,y=250)
        
       
gui= GUI()

name_label= Label(self.Window,text='name: ',fg='black',bg='lightblue',font=('Calibri',12),bd=1)
name_label.place(x=20,y=90)

user_name= Entry(self.Window,text='',bd=2,width=22)
user_name.place(x=150,y=92)


self.go= Button(self.login,
                text= 'CONTINUE',
                font= 'Helvetica 14 Bold',
                command= lambda: self.goAhead(self.entryname.get()))

def goAhead(self,name):
    self.login.destroy()
    self.name= name
    rcv= Thread(target=self.recieve)
    rcv.start()