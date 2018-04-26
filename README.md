# Sage FutureMakers Code Examples

Welcome the the Sage Future Makers Github repository. This is where you'll find code examples to help with connecting your Chatfuel Chatbot with Microsoft's Congnitive Services. 

We also have a getting started guide to help you with setting up your computer and running the code. 

## Examples
We have several examples for you to look at:

* Facial Recognition ([face.py](https://github.com/Sage/future_makers/blob/master/face.py))
* Search (using Bing) ([search.py](https://github.com/Sage/future_makers/blob/master/search.py))
* Text Analytics ([text_analytics.py](https://github.com/Sage/future_makers/blob/master/text_analytics.py))
* Translation ([text_analytics.py](https://github.com/Sage/future_makers/blob/master/translation.py))
* Vision ([vision.py](https://github.com/Sage/future_makers/blob/master/vision.py))

### Getting the examples
1. Download this [zip file](https://github.com/Sage/future_makers/archive/master.zip) to your desktop
1. Double-click on the zip file
1. Drag the folder to your desktop
1. Open **Visual Studio Code**
1. Click File -> Open Folder and choose the **future_makers** folder on your desktop

### Running the examples
1. Double-click on any file you are interested in
1. Sign up for the service using the link at the top of the source code file
1. Find your subscription keys (under Resource Management in the Azure Portal)
1. Replace the placeholder **SUBSCRIPTION_KEY** in the source code file (within the make_api_request method)
1. Click the Debug menu (at the top) and choose Start Debugging -> Python

## Prerequisites
### Azure
All examples use Microsoft's Azure services

1. Sign up for a free Azure account
1. Create any cognitive services (using the link at the top of the source code file)

### Ngrok
Ngrok provides a tunnel to your local machine so that it can receive messages from the internet.

1. Download this [zip file](https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-windows-amd64.zip) to your desktop
1. Double-click on the zip file
1. Drag the ngrok.exe to your desktop
1. Open Command Prompt (Start -> Run -> cmd)
1. Change to the Desktop folder (`cd %USERPROFILE%\Desktop`)
1. Open the ngrok Get Started [page](https://dashboard.ngrok.com/get-started)
1. Run the two commands (**remove the ./ from the front**):
    * ngrok authtoken YOUR_AUTH_TOKEN_HERE
    * ngrok http 80
1. Leave the command open (you can minimise the window)
