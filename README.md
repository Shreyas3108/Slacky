# Slacky
A mini twitter like site! 

Description :- 
---
A twitter-like site built for seemingless discussions within an organization or group. The key features include using Hashtags , Retweet (share[once in 24 hours]) , recommend users along with the flexibility to extend into building bots within as well as collect data for analysis. 

## Tools used :- 
---
1. Django 
2. Django Rest API 
3. Bootstrap 
4. Jquery 
5. HTML 

## Use Case :- 
---
![usecase](https://github.com/Shreyas3108/Slacky/blob/master/usecase.png)


## Working :- 
The first page is the login page where credentials are used :- 

![login page](https://github.com/Shreyas3108/Slacky/blob/master/output/login.png)

After signing in , the home page is displayed at first. 

![home page](https://github.com/Shreyas3108/Slacky/blob/master/output/home.png)

The working can be seen by adding the tweet "Time to say Cheese #hashtag Cheese!

![Cheese!](https://github.com/Shreyas3108/Slacky/blob/master/output/homewithtweet.png)

The profile page after clicking the user below the tweet (logged in from another id) 

![Profile](https://github.com/Shreyas3108/Slacky/blob/master/output/profilepage.png)

Let's Follow! 

![New Follower!](https://github.com/Shreyas3108/Slacky/blob/master/output/followadd.png)

Retweeting the tweet! 
![Retweet!](https://github.com/Shreyas3108/Slacky/blob/master/output/retweetresult.png)

Just searching randomly! 

![Search overall](https://github.com/Shreyas3108/Slacky/blob/master/output/searchoverall.png)
![Specific](https://github.com/Shreyas3108/Slacky/blob/master/output/searchtweet.png)


## How to use :- 
---
First clone the repository onto your computer by using this command. 
   ```$ git clone https://github.com/Shreyas3108/Slacky.git```


after which ,Open the terminal and type this command 
>$ cd socmed

>$ source bin/activate

>$ cd src

>$ python manage.py makemigarations 

>$ python manage.py migrate

>$   python manage.py runserver
       
You could then go to the login page by going to this URL
(http://127.0.0.1:8000/login)

Use the credentials to access the database :- 
user :- shrey2 
password :- github1234 

You could create more users too! and start posting. 

## Known Bugs :- 
---
1. For the purpose of extension (not a complete site yet) few links haven't been assigned. 
2. Reply function doesn't work and needs integration with the file inside. 

## Future Extensions :- 
----

The major extension would be to make a bot and deploy it using cloud services , also create chat to specific users and using data from tweets to find recomended users/page to follow.   


  
   

