# CAPI-63: How Configure Event Handler 


When there is an event in CAPI, it is necessary to handle these events and synchronize the changes with Notion. An abstraction of the solution is the following process:
1. An event occurs.
2. The relevant data from the event will be sent to a queue
3. When a message is received in the queue, the listener will perform an action with the data. 
4. The message is deleted from the queue

