# Disclaimer:

This software is provided for informational purposes only. As the developer, I am not responsible for any use of this Software, including any consequences arising from its use. Use of this Software is at your own risk.

Users who choose to use this Software should be cautious and careful, and understand that all actions they take using this Software are their own responsibility.

I do not endorse or support the use of this Software for any illegal purposes or for any purposes that infringe on the rights of others.

Finally, I want to emphasize that I do not provide any guarantees regarding the operation and functionality of this Software.


# Easy-vk-Spamer
A free and open-source Vkontakte spammer.
Built-in parsers for your friends and Vkontakte groups.
Targets are added to the target.txt file, and the main spammer works off that file.
image
The program launches your local Google Chrome. Only message sending is supported.
If you need additional functionality, please contact me on Telegram.

### Instructions
1. first way
  - shift + right-click - open cmd in directory
  ```
  pip install -r requirements.txt
  ```
  - Launch ui__Launch.pyw
  
2. second way using virtual env
  - start.bat


### Requirements
  - Google Chrome installed on the Windows drive
  - Windows only


### basic description 
  - Write a message, you can use emojis,
  address the person using the combination - ``` _имя_ ```
  IMPORTANT - there is a line break character, but your message will be displayed
  inside the program on one line. During operation, the line break character will work
  wherever you leave it.
  Messages will be sent randomly - one message to one person.

  - Add your account
  Important - log in to it through Google Chrome, otherwise
  an error with the phone number may occur.

  - Get group subscribers or friend links, both will be written
  to the target.txt file and the program will work off of them.
  IMPORTANT! - wait... parsing 2200 friends will take 5 minutes

  - Press start, the daily limit is 20 messages per account.
  Adding friends - 50 people per day.



### Demo mode
  it won't send messages or add friends
  it won't fill in old_perc
  mode - for preview,
  getting to know the program.

### Quiet mode
  Does not show the browser, but it is launched and
  it works more stably than without quiet mode.
  At the end, I recommend turning off Chrome through Task Manager.

### Accounts
  will automatically switch
  and continue sending messages, to leave
  one account in use, delete
  all accounts except the main one in the window
  Password + Login

### target.txt
  Links from the "Get group subscribers" button
  and "Get friend links" button will be added here.
  You can also add links manually, separated by a line break.

### old pers.txt
  This file will contain users who
  have already been processed, the program will never
  contact them again. You can delete links to reuse them.
  It also writes a report for each one.

### image
  Write a link to the image on the internet, to the final photo
  - https:// some image. com / cat.jpg
