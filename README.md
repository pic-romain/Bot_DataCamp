# Bot_DataCamp
Welcome everyone ! 
I made my first bot in order to gain experience on DataCamp through Daily Practice.

Earlier this year, I had a student access, thanks to my organisation to follow courses on **DataCamp**. We had to gain a minimum of 30,000 XP points but the deadline was coming to an end. So, I decided to focus on my training to reach the minimum as quick as possible. I found that the Daily Practice where the most efficient way to earn XP points because of the simple questions, with Introduction to Python or Introduction to R, and I could use shortcuts on my keyboard. After a little farming, I noticed that if you answer wrongly to a question it comes back and the order of the answer is randomized. This means that, if there is a single answer, at some point the first answer will be the correct one for any question. This is when I decided to code a bot to do this for me.

**Disclaimer** : I sent a message to DataCamp support and I haven't got an answer yet (18/04/2021). I decided to make this repo to share my experience and the fun I had building my little bot. :heart:

My setup is composed of two monitors and apparently there is an [issue](https://github.com/asweigart/pyautogui/issues/321) when using locateOnScreen to detect an image on the second monitor. 

Ideas for improvement :
* exploit the fact that the open-ended questions are limited and within a specific theme you will encounter the same questions after a while.
* test this bot on other topic to be sure that it is robust.
* add some statistics by counting and timing the number of Daily Practices finished.
* use a headless browser to make the bot quicker and to free the mouse and keyboard to do it on the background.


