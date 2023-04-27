Some challenges we've faced was figuring how the receiver would know that it has received all
the packets. Trying to debug our code was a hassle as well because we did not make use of helper
functions. Instead we typed almost all of our code under the run function.

Even though our code was able to pass a fair amount of tests, we believe that it could've been better
legibility and efficiency wise. Althought some properties/features of our design that we think is good are holding all the sent and ack packets held in a dictionary that has been useful for keeping hold of packets.

We used a lot of the printing statements to check the number of acks and sent packets the sender and recv has received and identifying what is stored in certain variables.