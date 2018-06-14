# Sage FutureMakers

Welcome the the Sage Future Makers Github repository.

## Bot Examples

To get started using some bots, take a look at these examples:

* [Mitskuku](https://www.pandorabots.com/mitsuku/)
* [DoNotPay](https://www.donotpay.com/)

## Code Examples

This is where you'll find code examples to help with connecting your Snatchbot Chatbot with Microsoft's Congnitive Services. 

We also have a getting started guide to help you with setting up your computer and running the code. 

## Examples
We have several examples for you to look at:

* Translation ([text_analytics.py](https://github.com/Sage/future_makers/blob/master/translation.py))
* Vision ([vision.py](https://github.com/Sage/future_makers/blob/master/vision.py))
* Face Detection ([face.py](https://github.com/Sage/future_makers/blob/master/face.py))

### Getting the examples
1. Download this [zip file](https://github.com/Sage/future_makers/archive/master.zip) to your desktop
1. Double-click on the zip file
1. Drag the folder to your desktop
1. Open **Visual Studio Code**
1. Click File -> Open Folder and choose the **future_makers** folder on your desktop

### Running the examples
1. Double-click on any file you are interested in
1. You'll need a subscription key, one of the Sage volunteers will be able to provide you with one 
1. Replace the placeholder **SUBSCRIPTION_KEY** in the source code file (within the make_api_request method)
1. You may also have to change the host name (eg westcentralus.api.cognitive.microsoft.com) to match your Azure service
1. Click the Debug menu (at the top) and choose Start Debugging -> Python
1. Optional - try setting a breakpoint

### Ngrok
Ngrok provides a tunnel to your local machine so that it can receive messages from the internet. You'll need to runs    this to be able to connect Chatfuel to the code running on your machine.

1. Download this [zip file](https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-windows-amd64.zip) to your desktop
1. Double-click on the zip file
1. Drag the ngrok.exe to your desktop
1. Open Command Prompt (Start -> Run -> cmd)
1. Change to the Desktop folder (`cd %USERPROFILE%\Desktop`)
1. Run the command (**remove the ./ from the front**):
    * ngrok.exe http 3001
1. Leave the command open (you can minimise the window)

## SnatchBot
[Snatchbot](https://snatchbot.me/) is the online software that we will be using to build and test the ChatBots. They have already built out documentation to help users with creating their own ChatBot, this can be found [here](https://support.snatchbot.me/docs). However, we have also given instructions below on how to complete some of the simpler tasks and as a quick guide. 

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









