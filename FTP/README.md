#High-level approach
The program creates two sockets, the control socket is responsible for sending FTP requests and receiving FTP requests. The data socket is responsible for downloading any data or uploading any data. The program runs on command line that support operations such as making directories, file deletion, copying files and moving files within the FTP server.


#Challenges I faced
When I run my code, the server would sometimes send the PASV message. I tried debugging what was the issue and it took awhile. So it made it really difficult to build other parts of the code when the data channel couldn't open up because the server wasn't receiving the PASV message

#Overview of how I tested my code
I just used the server to check if my code worked out or not. So it was just a lot of continuous run the python code and check if the server responded the way I wanted it to.
