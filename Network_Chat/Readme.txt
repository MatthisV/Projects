GROUP MEMBER: VILLENEUVE Matthis, SOUNDARA Hary, VERMEULEN Barthelemy, ZAIDI Zack

The folder already contains the database (test.db), so there is no need to launch the createtable.py
We joined the file for you to see how we created the database.
The log.txt file also has the previous logs, so when launching the server it will write after the existing logs,
allowing you to see what happened previously.

To launch the chat:
Check the server IP and Port (for one of our computer, the IP needs to be '127.0.0.1' and port '55555'
Once your server address and port are correect in the Server.py file, open the Client.py
Modify the address and port on the 'client.connect('....','.....')' line to match your Server.py address.
Launch the Server.py, it should open a shell and show 'Server is waiting...'
Launch the Client.py, enter an username that is in the database and its correct password.
If you fail, you won't be able to connect.

Once logged in, you can use the chat freely, open as many Client as you want to test, 
but be aware that if you want to move files between clients or with the server,
the clients and the server all have to be launched from different folders, or the files will be transferred
from the same folders, and thus erasing themselves.
For example, put the Server.py in a Server folder, one copy of Client.py in CLIENT1 folder, and
another Client.py copy in a CLIENT2 folder so that it simulates 3 different machines.