# Bot_DataCamp
Welcome everyone ! 
I made my first bot in order to gain experience on DataCamp through Daily Practice.

### Context
Earlier this year, I had a student access, thanks to my organisation to follow courses on **DataCamp**. We had to gain a minimum of 30,000 XP points but the deadline was coming to an end. So, I decided to focus on my training to reach the minimum as quick as possible. I found that the Daily Practice where the most efficient way to earn XP points because of the simple questions, with Introduction to Python or Introduction to R, and I could use shortcuts on my keyboard. After a little farming, I noticed that if you answer wrongly to a question it comes back and the order of the answer is randomized. This means that, if there is a single answer, at some point the first answer will be the correct one for any question. This is when I decided to code a bot to do this for me.

I was able to obtain around 800,000XP in approximately 10 hours. This was more than enough for my class and I ranked first among my class.

**Disclaimer** : I sent a message to DataCamp support and I haven't got an answer yet (18/04/2021). I decided to make this repo to share my experience and the fun I had building my little bot. :heart:

### Logic behind the bot

As explained in the previous section, this bot uses the keyboard and the mouse in order to select the postion of the accept button and to enable the shortcuts after reloading the page.

The questions are mainly Multiple Choice Questions (MCQ) and the rest of the questions are open-ended questions where we need to type the correct code. Some MCQ need two answers. The strategy of this bot is to answer **2** and **1** via the shortcuts and to skip the open-ended questions by reloading the page. When only one answer is needed, this will lead to finally choosing the first answer and, for the ones that require two answers, this will lead to choosing 1 and 2.

### How to use the bot

In order to use my bot, you need to enter the coordinates corresponding to the postion of the accept button on the site. You can also adapt the **delay** if your browser takes some time to reload the page. You need to setup your browser one the main monitor of your computer.

The bot start by a count down in order to let you select the browser and then you can leave the while-loop by pressing "Q".

N.B. : 

* My setup is composed of two monitors and apparently there is an [issue](https://github.com/asweigart/pyautogui/issues/321) when using locateOnScreen to detect an image on the second monitor. 
* The shortcut where the one on my AZERTY keyboard for Windows, these may need to ne changed for other configurations.

### Ideas for improvement :
* exploit the fact that the open-ended questions are limited and within a specific theme you will encounter the same questions after a while.
* test this bot on other topic to be sure that it is robust.
* add some statistics by counting and timing the number of Daily Practices finished.
* use a headless browser to make the bot quicker and to free the mouse and keyboard to do it on the background.

### Sources :
* [Kian Brose's YouTube](https://www.youtube.com/watch?v=YRAIUA-Oc1Y&t=47s&ab_channel=KianBrose) : he makes step by step videos that are perfect to start learning about botting in Python and other topics.
