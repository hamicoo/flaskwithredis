# flaskwithredis
in this simple example, I tried to show the role of cache in the wrapper of the web service and I also used Elastic APM  for watching the status of the wrapper.
my architecture for this aim is something like the image below.
this code is a simple wrapper on an online dictionary API, you can use it in your use case especially when you have more readers than your writers.
when you see green meesage it shows you get it from API and when you see orange message it means you get it from Redis.
<br>
<img src="https://img.techpowerup.org/201004/screenshot468.png" alt="2W6DN4.md.png" border="3">
