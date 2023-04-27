Our code stores and gives the stored value depending on the request.
It is like a loop that handles requests and responses from all replicas. 
Actions are also depended on whether the replica is a leader. If the 
replica is not a leader, and the election timer is not up, an election 
would start. During the election the replica would send out requests for
other replica's vote to become leader. If it receives a vote, it is stored
in a list to keep track of the number of votes and which replica has voted
for them. In handling the vote message, conditions of becoming a leader would
be applied. If the replica has the majority of votes it becomes leader.
Otherwise, if the replica is a leader which means there will be no election, 
the replica sends an Append Entry to other replicas which resets the state of 
the replica, votes, changes the term and leader depending on whcih replica 
has the highest term. This is to make sure the replica sending the Append Entry 
is actually a leader. After the election, depending on the request and whether 
the replica is a leader, the replica would perform the request of either storing 
data, returning data, or send a redirect message there will be a redirect.

A list of properties/features that we thought was good:
- How we handled our requests or responses. Our HandleResponse method.
- Can handle all the response/message/requests from other replicas
- Storing votes in a list
- Keeping track of the leader

Something that we had trouble with was understanding how handle the time for the
election. Throughout the code we were not sure how to utilize time.time() to help
identify whether it has reached the election's time out.

We tested our code by using the run command in the terminal. By using this, we
were able to identify what is missing in our code with the errors or information
given when running the simulator. 