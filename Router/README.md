Teresa Liang, Jeffrey Guo

High level approach
The program forwards data to the appropriate neighbor, updating the forwarding table
with new routes. Also supports for message types such as update, data, dump and withdraw
messages. Data messages determine the best route to send the data to by using longest prefix,
localpref, selfOrigin, ASPath, origin and the lowest ip.

Challenges we faced
We faced a lot of challenges such as understanding the tests, examples and how functions
were suppose to be implemented.

Testing
A lot of our testing was just using the command ./run configs/test-file and checking the terminal
to see if the routes were being sent to the right place. Other than that, we just use print
statements to check what routes were being sent and errors within our code.