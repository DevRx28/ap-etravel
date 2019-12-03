Etravel website using django and Materialize CSS
------------------------------------

This is an e-travel website made with Django framework and Materialize CSS.

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License in the LICENSE.md file for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.

Features:
1. Has over a dozen flight options (including connecting flights).
1. Has over a dozen hotel options including booking for multiple days.
1. Users can create account/login using their email IDs and Google Accounts (OAuth).
1. Users can view their booking history and store payment information.
1. Transactions are mocked using invalidated Debit/Credit Cards as a payment options.


#### HOW TO USE THIS PROGRAM

######	I	PURPOSE
######	II	SYSTEM REQUIREMENTS
######	III	INSTALLATION
######	IV	EXECUTION 
######	V	SUPPORT

####	I	PURPOSE

This program aims to mimic an etravel website which can be deployed and scaled with ease. 

####	II	SYSTEM REQUIREMENTS
   
   This program was made and tested on Ubuntu 18.04 and 19.04 virtual machines on windows 10 hosts (Build 1903) with the following specifications:

	Atleast an Intel Core i5 or Ryzen 5
	At least 8 GB RAM (of which at least 4 GB alotted to virtual machine)
	VBoxSVGA or similar graphics controller with at least 128 MB memory for the virtual machines.

   Any system that can run Ubuntu 16.04 either natively or in a virtual machine should be able to run this website just fine.

####	III	INSTALLATION
	
This website does not require any installation as it comes with its own virtual environment with all packages installed.
However, if you are running a windows machine, we recommend that you you install Ubuntu in a virtual machine by using either VirtualBox or Windows Hyper-V.
Functionality should be consistent for any Posix-based system, although prior testing has only been done on Ubuntu.
	
####	IV	EXECUTION
	
To avoid any compatibility issues, we recommend that this website be executed in a Posix-based system.

First, download the zip archive from github. Extract it and navigate to the folder it was extracted to. Navigate to the "etravel" folder within it. You should be able to see a manage.py file. Open a terminal window in that folder. Then run the following lines of code:

###### Prerequisites:

- Python 3
- Pip (package manager)

If you do not have the above prerequisites installed, run the following commands.

```
sudo apt install python3
sudo apt install python-pip
sudo apt install virtualenv
```

###### Setting up the environment

Step 1 -

Navigate to your home directory (root) and enter the following commands to create the virtual environment.

```
virtualenv etravel
cd ~/etravel
```
Then activate the environment using:

```
source ./bin/activate
```
Once the environment is activated, create a copy of requirements.txt in the 'oscar' directory and run:

```
pip3 install -r requirements.txt
```

Once the 'etravel' directory is populated with the required libraries, create a local copy of the folders in this repository. This can be done through either git or downloading a zipped version. Then replace the files in that folder with the contents of this repo.

Then run `python3 ~/etravel/manage.py runserver` to start the django server.

Finally, navigate to either 127.0.0.1:8000 or localhost:8000 on your web browser and the website should be up and running.


####	V	SUPPORT
	
If you have issues with running the code or need technical support in general with
issues relating to running the program, you can get in touch with the developers at:

adhiraj.srivastava_asp20@ashoka.edu.in, 
daksh.baheti_asp20@ashoka.edu.in, 
devvrat.raghav_asp20@ashoka.edu.in, 
skzafar.ali_asp20@ashoka.edu.in
shivam.sahu_asp20@ashoka.edu.in
