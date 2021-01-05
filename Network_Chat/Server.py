#implementing the server first we will need to import two libraries, namely socket and threading

import socket
import threading
from datetime import datetime
import os

# Connection Data
host = '127.0.0.1'
port = 55555

# Starting Server
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen(50)

# Lists For Clients and Their Nicknames
clients = []
nicknames = []
filelist= []


# Sending Messages To All Connected Clients
def broadcast(message):
    for client in clients:
        client.send(message)

# Handling Messages From Clients
def handle(client):
    while True:
        try:
            # Broadcasting Messages
            msg = message = client.recv(1024)
            
            if msg.decode('ascii').startswith('KICK'):
                if nicknames[clients.index(client)] == 'admin':
                    namekicked = msg.decode('ascii')[5:]
                    kickuser(namekicked)
                    log="An admin kicked {0}".format(str(namekicked))
                    appendlog(log) 
                else:
                    client.send('You don t have permission'.encode('ascii'))
            
            elif msg.decode('ascii').startswith('SHUTDOWN'):
                if nicknames[clients.index(client)]=='admin':
                    log="Server shutdown by {0}".format(clients.index(client))
                    print('The server has been closed by an admin')
                    return False
                else:
                    client.send('You don t have permission'.encode('ascii'))
            
            elif msg.decode('ascii').startswith('BAN'):
                if nicknames[clients.index(client)] == 'admin':
                    namebanned = msg.decode('ascii')[4:]
                    kickuser(namebanned)
                    with open('bans.txt','a') as f:
                        f.write(f'{namebanned}\n')
                    print("f'{namebanned}\n' was banned!")
                    log="An admin banned {0}".format(str(namebanned))
                    appendlog(log)
                else:
                    client.send('You don t have permission'.encode('ascii'))
            
            elif msg.decode('ascii').startswith('ALERT'):
                if nicknames[clients.index(client)] == 'admin':
                    alert = msg.decode('ascii')[6:]
                    mess='\t\t/!\ Alert: '+alert+' /!\ \t\t'
                    broadcast(mess.encode('ascii'))
                else:
                    client.send('You don t have permission'.encode('ascii'))
            
            elif msg.decode('ascii').startswith('FILE'):
                print('Receiving file...')
                filename=msg.decode('ascii')[5:]
                f = open(filename, "wb")
                filelist.append(filename)
                l = client.recv(1024)
                while (l!=bytes(1)): 
                        f.write(l)
                        l = client.recv(1024)
                f.close()
                print("File Received")
                log="A file was uploaded to the server: {0}".format(str(filename))
                appendlog(log)
                
            
            elif msg.decode('ascii').startswith('DOWNLOAD'):
                mess=msg.decode('ascii').split(None,2)
                filename=mess[2]
                if filename in filelist :
                    client.send((f'DOWNLOAD {filename}').encode('ascii'))
                    send_file(client,filename)
                    client.send(bytes(1))
                    print("File Downloaded by a Client")

                else:
                    client.send('File not found'.encode('ascii'))    
            
            
            elif msg.decode('ascii').startswith('CLIENTFILE'):
                filename="MyfileTemporary.txt"
                f = open(filename, "wb")
                l = client.recv(1024)
                while (l!=bytes(1)): 
                    f.write(l)
                    l = client.recv(1024) 
                f.close()
                broadcast(("CLIENTFILE").encode())
                send_txt(filename)
                os.remove("MyFileTemporary.txt")
                broadcast(bytes(1))
                print("File sent to clients")
                log="A file was sent to the clients"
                appendlog(log)
            
            
            elif msg.decode('ascii').startswith('LISTFILE'):
                client.send("There are {} file(s)".format(len(filelist)).encode('ascii'))
                for i in range (len(filelist)):
                    client.send(str(filelist[i]).encode('ascii'))
                
            
            elif msg.decode('ascii').startswith('LISTUSER'):
                client.send("There are {} user(s)".format(len(nicknames)).encode('ascii'))
                for i in range (len(nicknames)):
                    client.send(str(nicknames[i]).encode('ascii'))
                    client.send("\n".encode('ascii'))
                    
                    
            elif msg.decode('ascii').startswith('PRIVATE'):
                mess=msg.decode('ascii').split(None,3)
                sender=mess[1]
                dest=mess[2]
                content=mess[3]
                if dest in nicknames :
                    name_index = nicknames.index(dest)
                    clientdest = clients[name_index]
                    header="\nPrivate message from "+sender+": "
                    clientdest.send(header.encode('ascii'))
                    clientdest.send(content.encode('ascii'))

                else:
                    client.send('User not found'.encode('ascii'))

            elif msg.decode('ascii').startswith('RING'):
                ringuser=msg.decode('ascii')[5:]
                if ringuser in nicknames:
                    client.send('User is online'.encode('ascii'))
                else:
                    client.send('User is offline'.encode('ascii'))
            
            elif msg.decode('ascii').startswith('HELP'):
                instructions="\n \t Instruction list: \n "
                instructions+="/file FILENAME to send a file to the server\n"
                instructions+="/filec FILENAME to send a file to all the users\n"
                instructions+="/listfile to display all files for download\n"
                instructions+="/userlist displays the list of connected users\n"
                instructions+="/private USERNAME MESSAGE to send a private message \n"
                instructions+="/exit to leave the chat\n"
                instructions+="/ring USERNAME to check if a user is online\n"
                instructions+="/download FILENAME to download the named file\n"
                if nicknames[clients.index(client)]=='admin':
                    instructions+="\n\t Administrator Instructions:\n\n"
                    instructions+="/kick USERNAME kicks the selected user\n"
                    instructions+="/ban USERNAME bans the selected user\n"
                    instructions+="/shutdown stops the server\n"
                    instructions+="/alert MESSAGE sends an alert to all users\n"
                    client.send(instructions.encode('ascii'))
                else:
                    client.send(instructions.encode('ascii'))
            
            elif msg.decode('ascii').startswith('EXIT'):
                index = clients.index(client)
                client.send(("You have been disconnected").encode('ascii'))                
                client.close()
                clients.remove(client)
                nickname = nicknames[index]
                nicknames.remove(nickname)
                broadcast('{} left!'.format(nickname).encode('ascii'))
                print('{} left!'.format(nickname))
                log="{0} has exited the chat".format(str(nickname))
                appendlog(log)
                break

            else:
                broadcast(message)
        except:
            # Removing And Closing Clients
            index = clients.index(client)
            clients.remove(client)
            client.close()
            nickname = nicknames[index]
            broadcast('{} left!'.format(nickname).encode('ascii'))
            nicknames.remove(nickname)
            break


                
                
# Receiving / Listening Function
def receive():
    while True:
        # Accept Connection
        client, address = server.accept()
        print("Connected with {}".format(str(address)))

        # Request And Store Nickname
        client.send('NICKNAME'.encode('ascii'))
        nickname = client.recv(1024).decode('ascii')
        log="{0} connected with {1}".format(str(nickname),str(address))
        appendlog(log)        

        with open('bans.txt','r') as f:
            bans = f.readlines()
        if nickname+'\n' in bans :
            client.send('BAN'.encode('ascii'))
            log="{0} tried to connect with {1} but was banned".format(str(nickname),str(address))
            appendlog(log)        

            client.close()
            continue

        if nickname == 'admin':
            client.send('PASSWORD'.encode('ascii'))
            password = client.recv(1024).decode('ascii')

            if password != 'adminadmin':
                client.send('REFUSE'.encode('ascii'))
                client.close()
                log="{0} tried to connect with {1} as admin but failed to give password".format(str(nickname),str(address))
                appendlog(log) 
                continue

        nicknames.append(nickname)
        clients.append(client)

        # Print And Broadcast Nickname
        print("Nickname is {}".format(nickname))
        broadcast("{} joined!".format(nickname).encode('ascii'))
        client.send('Connected to server!'.encode('ascii'))

        # Start Handling Thread For Client
        thread = threading.Thread(target=handle, args=(client,))
        thread.start()
        
        
        
        
        
        

def send_txt(filename):
    
    with open(filename,'rb') as f:
        l = f.read(1024)
        while (l):
            broadcast(l)
            l = f.read(1024)
        
def kickuser(name):
    if name in nicknames :
        name_index = nicknames.index(name)
        clientkicked = clients[name_index]
        clients.remove(clientkicked)
        clientkicked.send('You were kicked by the admin !'.encode('ascii'))
        clientkicked.close()
        nicknames.remove(name)
        broadcast(f'{name} was kicked by the admin'.encode('ascii'))

def send_file(client,filename):
    with open(filename,'rb') as f:
        l = f.read(1024)
        while (l):
            client.send(l)
            l = f.read(1024)

def appendlog(string):
    log=open("log.txt",'a+')
    log.write(str(datetime.now().strftime("<%m/%d/%Y %H:%M:%S>")))
    log.write("\n"+str(string)+"\n\n")
    log.close()
    
print('Server is waiting...')
receive()

