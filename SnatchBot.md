## SnatchBot
[Snatchbot](https://snatchbot.me/) is the online software that we will be using to build and test the ChatBots. They have already built out documentation to help users with creating their own ChatBot, this can be found [here](https://support.snatchbot.me/docs). However, we have also given instructions below on how to complete some of the simpler tasks and as a quick guide. 

We've broken the instructions down into three main areas

1. [Getting Started](#getting-started)
1. [User responses](#user-responses)
1. [Connecting to an API](#connecting-to-an-api)
1. [Plugins](#snatchbot-plugins)

### Getting Started
After setting up your account and logging in, you will be taken to the Dashboard and on the left hand side of the screen you will see the toolbar. It looks like this - 

![toolbar](https://user-images.githubusercontent.com/39263870/41412687-b9863148-6fd8-11e8-85d2-096cec186528.png)

To create your first Bot -
1. Click on "My Bots"
1. Click on "Create Bot"
1. Name your Bot, give it a description (e.g. This ChatBot will guess a person's age based upon a picture of them) and also upload an image that best represents the use case of this ChatBot. You MUST use an image to be able to create a bot. After its creation you will be taken to this screen - 

![newbotbuilt](https://user-images.githubusercontent.com/39263870/41413552-593eefa2-6fdb-11e8-9aa1-ca8e8c0c4b77.png)

You can now flesh out the ChatBot, with 'Interactions'. These are the way in which the Bot will communicate with the user. There are many different types of interactions, you find a list of them and what they do [here.](https://support.snatchbot.me/docs/interactions)
Lets begin with a simple text message (Bot Statement) that the user will recieve. As its our ChatBots first message we'll have it as a welcome message.
1. Click on the blue circular plus button.
1. Click "Choose Interaction Type" and select "Bot Statement"
1. You will now be able to name your Interaction. The more descriptive the name the better for easier identification as you build the Bot out and it becomes more complex. When you've decided upon a name click the + button. 
When the interaction has been created you can click upon it and it will bring up the editing tools. You can then write the welcome message that the user will recieve. 

![exampleinteraction](https://user-images.githubusercontent.com/39263870/41415514-a83b6cfc-6fe0-11e8-9264-a3dff3c5b120.png)

You can test the ChatBot to ensure that your interaction is functioning as intended by clicking on "Test this Bot" in the top right hand corner. On the right hand screen a messaging window will open, imitating what the user would see. 

![firstinteractiontestbot](https://user-images.githubusercontent.com/39263870/41415776-45a20b0e-6fe1-11e8-8d89-f863aa85e5b3.png)

Congratulations, you have now created your first ChatBot. 

### Linking Interactions

In order to build out your ChatBot you'll want to link interactions to one another. 

![connectionwelcomemessage](https://user-images.githubusercontent.com/39263870/41417359-08bc872e-6fe5-11e8-9c33-37b46be5df29.png)

In the Image above you can see that I've built out two more Bot Statements called "Step One" & "Step Two". Using the editing tools, specifically the connection section, on the "Welcome Message" I've set it up so that if the user was to reply "hello" to the welcome message it would advance to "Step One".

![welcome-stepone](https://user-images.githubusercontent.com/39263870/41417853-634370bc-6fe6-11e8-8c82-7a121dd72427.png)

Using this idea of connections its possible to build it the ChatBot and you can then include the other interactions that we spoke about earlier. 

### User responses 

When building your Chatbot, it's likely that at some point you'll want your bot to make reference to something the user has told your bot. Lets say your bot asks the user their name, you might want it to refer to the user by name from then on. In order to do this, Snatchbot uses something called **Prior Responses**. The tool is located directly above the Bot's message. 

![priorresponses](https://user-images.githubusercontent.com/39263870/41533102-809bfb58-72f1-11e8-9135-3f8c405cd2d9.png)

This drop down menu gives you the commands that will pull the user responses. These commands need to go within the square brackets [].

[ResponseTo interaction=ID fallback=TEXT] is the command you will need. 

This function takes the response text from an Interaction that you specify by using its ID number. So, for example, [ResponseTo interaction= 285344] takes the response from the Interaction number 285344. You’ll find the interaction ID list for your current bot at the top right of your Interaction editing window.

![interactionsdropdown](https://user-images.githubusercontent.com/39263870/41533623-5cbe718c-72f3-11e8-9cce-321b1a314937.png)

The response data that is used will be the whole of the user's response. Within the command you can also see 'fallback=text', this is the text the user will recieve if something goes wrong, such as the ID being non-exsistent or there being no response. You should change it from 'TEXT' to something more appropriate like 'Sorry, something went wrong. We should start again'

Example:

Interaction ID 1: Hello! What is your name?  
Interaction ID 2: Nice to meet you, [ResponseTo interaction=1 fallback=Something has gone wrong. Let’s start over].

Result:

Bot: Hello! What is your name?  
User: Mary.  
Bot: Nice to meet you, Mary.  

Or

Bot: Hello! What is your name?  
User: %757!  
Bot: Nice to meet you, Something has gone wrong. Let’s start over.  
Bot: Hello! What is your name?  

### Connecting to an API

1.  In order to connect your Snatchbot to an API you will first need to run Ngrok. You can find out what Ngrok is and how to run it on the laptop you are using [here](samples.md).

1.  After you've got Ngrok running correctly (If you're having problems getting Ngrok running, grab one of the volunteers), then you'll want to add the "JSON API" interaction within SnatchBot. 

1.  You'll then need to provide SnatchBot with the address of your API. Your address can be found within the command prompt window you are using to run Ngrok. We highlighted where to find the address in the same place we describe how to get Ngrok running. 

1.  When you have provided SnatchBot with the correct Ngrok address you'll want to run the code within Visual Studio. You can run the code by starting to "Debug". This is under the drop menu at the top of the screen. 

1.  Select Python. If you have done this correctly then a terminal will open on the bottom half of the screen, this lets you know that the code is running. If you are having problems grab one of the volunteers. 

### SnatchBot Plugins

If you'd like to build your bot out a bit more then you can make use of another one of SnatchBots in-built features - Plugins. By now you will have noticed that next to interactions there is also a choice to select plugins. We add plugins the same way we add interactions but instead these result in a different outcome. Lets have a look at one of them.

1.  We're going to add giphy to our chatbot. So we'll add giphy the same way we would add an interaction. Once we've added and selected giphy we'll be presented with this screen. 
![untitled](https://user-images.githubusercontent.com/39263870/42686369-97ba7cec-868d-11e8-8201-24d43e78c618.png)
As you can see, SnatchBot automatically fills in the messages that the Bot would send, you can change this if you'd like. Unlike interactions you can also see that along the top there are buttons for Step One, Step Two and Step Three. 

1.  Before being able to use Giphy you'll have to make sure that you have a connection to the plugin. This is done the same was as you connect interactions to one another. 

1.  When you have connected the interactions. You should test the bot to see the result the user would get. You should see something like this!
![2](https://user-images.githubusercontent.com/39263870/42688687-3d10110a-8695-11e8-9e23-f9c9513ae3d2.png)

1.  You now have a working Plugin! Give a play with some of the others and have a think about how they could be useful in your chatbot!



