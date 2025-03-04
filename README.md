# kise

Create a virtual environment. This will help manage your package installations without having to install the directly to your local machine or having to reconfigure or update existing packages within your local environment / machine.

To do this:
check the version of python you have installed:

if its less than python 3 run python -m venv myvenv
if its python 3 and above i.e upto python 3.7 then run python3 -m venv myvenv

replace myvenv with the desired name of your environment. For mine, I named it langing_venv

once the virtual environment has been configured / installed within your app, then you need to activate

For linux && macos: source myvenv/bin/activate

For windows: myvenv\Scripts\activate

Finally, you need to install necessary packages for the app. Since I just added all packages to the requirements.txt file. All you need to do is run pip install -r requirements.txt

When you have done this, you can now run your server
