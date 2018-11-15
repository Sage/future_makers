### Ngrok
Ngrok provides a tunnel to your local machine so that it can receive messages from the internet. You'll need to runs this to be able to connect SnatchBot to the code running on your machine.

1. Download this [zip file](https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-windows-amd64.zip) to your desktop
1. Double-click on the zip file
1. Drag the ngrok.exe to your desktop
1. Open Command Prompt (Start -> Run -> cmd)
1. Change to the Desktop folder (`cd %USERPROFILE%\Desktop`)
1. Run the command (**remove the ./ from the front**):
    * ngrok.exe http 3001
1. Leave the command open (you can minimise the window)
1. If you've followed this instructions correctly then your command prompt window should look like this!  

![ngrok](https://user-images.githubusercontent.com/39263870/42217920-dddcf1d6-7ebe-11e8-8399-fd10dc2aa6d3.png)
The arrow in the above image is highlighting the "API Address", you will need this later for SnatchBot.
