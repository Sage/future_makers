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

### Creating your first Bot
After setting up your account and logging in, you will be taken to the Dashboard and on the left hand side of the screen you will see the toolbar. It looks like this - 
![toolbar](https://user-images.githubusercontent.com/39263870/41412687-b9863148-6fd8-11e8-85d2-096cec186528.png)


