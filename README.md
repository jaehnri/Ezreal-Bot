# EzrealBot
Selenium based bot that eternally pokes people on Facebook.

## How can I run it?

Firstly, you need to install selenium:
 - `pip install selenium`
 
Secondly, you need to download the chrome driver at https://chromedriver.chromium.org/.

On Linux/macOS, unzip the executable and move it to `\usr\local\bin`.  
On Windows, unzip the executable and move it to `\Python27\Scripts`.  

Open `ezreal_bot.py` with your favorite text editor and substitute the variables `fb_email` and `fb_pwd` with your Facebook e-mail and password, respectively.  

Run this program by executing `python ezreal_bot.py` in your project folder.

Cheers!

Obs: if you have two factor authentication enabled on your Facebook profile, this bot won't be able to log in your account. Please, disable it in order to run this project.
