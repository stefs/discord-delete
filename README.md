# discord-delete
> This is a very low level project and you probably have to understand the code to make it work. I 
> only made this for my personal use, but maybe someone finds it helpful.

This is a script which deletes all your own messages from a conversation by automatically 
interacting with the Discord GUI. For this [PyAutoGUI](https://github.com/asweigart/pyautogui) is 
used, available on PyPi as `pyautogui`. It takes screenshots to find messages and buttons.

Before running, add a cropped screenshot of your Discord name as file `template_name.png` in order 
to locate messages from your account.

Please make sure the template image files match your Discord zoom level. The distance in x-direction
between the name tag and the delete menu is hard coded, because it cannot be identified visually, so 
please make sure the value is appropriate for the width of your Discord window.

To stop the script at any time, the PyAutoGUI fail-save mechanism of moving the mouse cursor to the 
upper left corner of the screen is available.

## Example output
```
[...]
Delete message 50 ... done (4.3 seconds per message)
Delete message 51 ... done (4.3 seconds per message)
Delete message 52 ... done (4.3 seconds per message)
Delete message 53 ... no message found
Scroll ... done
Delete message 53 ... done (4.3 seconds per message)
Delete message 54 ... done (4.3 seconds per message)
Delete message 55 ... done (4.3 seconds per message)
Delete message 56 ...
```
