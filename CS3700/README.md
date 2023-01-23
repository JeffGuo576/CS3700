High-level approach
The program create sockets to connect to the server. The program will change the type of socket depending if it requires TLS or not. In order to start, it requires to send a hello message to the server to get a response. After that we store the ID and make multiple guesses until we find the secret word. After that the server sends a response bye with the secret flag.

Challenges 
I am definitely not familiar with python so I basically brute force through it all. In addition, I struggled to understand the documentation for sockets and just had a terrible time figuring out how it worked. The project was very new to me but definitely learned a lot

Guessing strategy
My guessing strategy was just using marks to my advantage. I just used the marks to remove words that could not be possibly the word and then recursively guessed again until it got the word correctly.

Testing
A lot of my testing was using print statements or just running the python file to the server to check for any problems.
