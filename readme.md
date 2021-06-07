# Barebones web-push notification experiment

This repo contains a barebones web push notification experiment that lets you understand the concept better. 

**The code ins intentionally written badly since the purpose of this code is to show how the whole damn thing works in a barebones system and not how to build a scalable notification server**

## how to test

- Run `python server.py`
- Navigate to https://localhost:4443
- Click on subscribe and give permission to the browser for notifications
    - You will immediately get a test notification. If not, click on subscribe again.
  -  The subscription will be written to sub.info. Only one client is handled for now. 
- Execute `python sendNotification.py` from within the `cgi-bin` directory to send a notification to the browser


## known issues
- works only with firefox since chrome does not support self signed certs for service worker registration.

## keys

dummy keys for the test are generated with https://vapidkeys.com/
