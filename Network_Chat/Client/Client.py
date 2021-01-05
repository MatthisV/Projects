
import socket
import threading



# Choosing Nickname
nickname = input("Choose your nickname: ")
if nickname == 'admin':
    password = input('Enter the password of admin account: ')

# Connecting To Server
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 55555))
stop = False

# Listening to Server and Sending Nickname
def receive():
    while True:
        global stop
        if stop:
            break
        try:
            # Receive Message From Server
            # If 'NICK' Send Nickname
            message = client.recv(1024).decode('ascii')
            if message == 'NICKNAME':
                client.send(nickname.encode('ascii'))
                next = client.recv(1024).decode('ascii')
                if next ==  'PASSWORD':
                    client.send(password.encode('ascii'))
                    if client.recv(1024).decode('ascii') == 'REFUSE':
                        print("Wrong password")
                        stop = True
                elif next == 'BAN':
                    print('This account is banned')

                    stop = True
            elif message.startswith('CLIENTFILE'):
                print('Receiving file...')
                filename="MyfileClient.txt"
                f = open(filename, "wb")
                l = client.recv(1024)
                while (l!=bytes(1)): 
                    f.write(l)
                    l = client.recv(1024)
                f.close()
                print("File Received")
            
            elif message.startswith('DOWNLOAD'):
                print('Downloading file...')
                mess=message.split(None,2)
                filename=mess[2]
                f = open(filename, "wb")
                l = client.recv(1024)
                while (l!=bytes(1)):
                    f.write(l)
                    l = client.recv(1024)
                f.close()
                print("File Downloaded")
            
            
            else:
                print(message)
        except:
            # Close Connection When Error
            print("You have been disconnected")
            client.close()
            break
# Sending Messages To Server
def write():
    while True:
        if stop:
            break
        message = f'{nickname}: {input("")}'
       
        if message[len(nickname)+2:].startswith(('/exit')):
                    client.send('EXIT'.encode('ascii'))
                    client.close()
 
        elif message[len(nickname)+2:].startswith('/userlist'):
            client.send('LISTUSER'.encode('ascii'))
 
    
        elif message[len(nickname)+2:].startswith(('/file')):
                    if message[len(nickname)+2:].startswith(('/filec')): 
                        filename=message[len(nickname)+2+7:]
                        client.send(('CLIENTFILE').encode('ascii'))
                        send_txt(filename)
                        client.send(bytes(1))
                    else:
                        filename=message[len(nickname)+2+6:]
                        client.send((f'FILE {message[len(nickname)+2+6:]}').encode('ascii'))
                        send_txt(filename)
                        client.send(bytes(1))
        
        elif message[len(nickname)+2:].startswith('/private'):
                client.send((f'PRIVATE {message[:len(nickname)]} {message[len(nickname)+2+9:]}').encode('ascii'))            
        
        elif message[len(nickname)+2:].startswith('/ring'):
                client.send(f'RING {message[len(nickname)+2+6:]}'.encode('ascii'))             
                    
        elif message[len(nickname)+2:].startswith('/listfile'):
                    client.send("LISTFILE".encode('ascii'))
                    
        elif message[len(nickname)+2:].startswith('/help'):
            client.send("HELP".encode('ascii'))
                    
       
        elif message[len(nickname)+2:].startswith('/download'):
            filename=message[len(nickname)+2+10:]
            client.send((f'DOWNLOAD {message[:len(nickname)]} {message[len(nickname)+2+10:]}').encode('ascii'))             
       
        
        elif message[len(nickname)+2:].startswith('/'):
            if nickname == 'admin':
                if message[len(nickname)+2:].startswith('/kick'):
                    client.send(f'KICK {message[len(nickname)+2+6:]}'.encode('ascii'))
                elif message[len(nickname)+2:].startswith('/ban'):
                    client.send(f'BAN {message[len(nickname)+2+5:]}'.encode('ascii'))
                elif message[len(nickname)+2:].startswith('/shutdown'):
                    client.send('SHUTDOWN'.encode('ascii'))
                elif message[len(nickname)+2:].startswith('/alert'):
                    client.send(f'ALERT {message[len(nickname)+2+7:]}'.encode('ascii'))
                
            else:
                print("You have to be an admin to use this command !")
        
        else:
            client.send(message.encode('ascii'))

def send_txt(filename):
    
    with open(filename,'rb') as f:
        l = f.read(1024)
        while (l):
            client.send(l)
            l = f.read(1024)
    print("Sent")
                      

# Starting Threads For Listening And Writing
receive_thread = threading.Thread(target=receive)
receive_thread.start()

write_thread = threading.Thread(target=write)
write_thread.start()