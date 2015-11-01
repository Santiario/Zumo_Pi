# Sumo_Pi
School project where we made a robot by combining an Arduino Sumo shield and a Raspberry Pi.

#Getting Started with Zumo-Pi#
Your Zumo robot is now driven by a Raspberry Pi processor, which provides considerably more power and
programming possibilities than the Arduino. It comes fully loaded with Python (versions 2 and 3) and all
of the important packages for connecting Python to your robot’s sensors and motors. You should be able to
take these connections for granted and focus most of your effort on standard Python programming.
However, there are a few preliminary activities that you will need to perform:

1. Insert the micro-SD card that comes with your robot into the slot on the front of your Raspberry Pi.
Your student assistants can assist you, if the card has not already been inserted on your robot. Some
come pre-installed.

2. Connect your robot to the internet via an ethernet cable.

3. Connect your robot to a power source and turn it on. It is important that this is done AFTER
connecting to the ethernet, not before. As soon as your robot is powered up, it will automatically
receive an IP address from one of IDI’s servers.

4. You will need to know your robot’s (current) IP address. To find it, go to the following site:
folk.ntnu.no/haakongi/TDT4113/get ip from mac.php.
At this site, use the MAC address for your robot’s Raspberry Pi (given to you with the robot) to look
up your IP address. Here are typical examples of MAC and IP addresses:
5Of course, this simple example assumes that all obstacles are above ground. It does not account for holes or ravines that
the robot would probably benefit from avoiding.

MAC: b8:27:eb:1a:36:50
IP: 129.241.111.162

5. Use the IP address for connecting the robot to your laptop via the internet.
Note that you will be given BOTH the MAC and IP addresses when you receive your robot. However, that
IP address will only work when you are in the P-15 lab. If you are working anywhere else, you will need to go
through the process above each time you begin a new session with the robot. That session may include many
connects and disconnects between laptop and robot, but each disconnect will NOT necessitate acquiring a
new IP address, as long as you remain in approximately the same physical location (e.g., the same room in
a building).

From your laptop, you can access the robot using the ’ssh’ command from a terminal window. Simply type:
ssh pi@<your IP address>
So with the IP address above, this is: ssh pi@129.241.111.162
You must use the default username (pi) and password (raspberry) to log on the first time. To save a lot of
hassles when using Python on the robot, logon to the root instead of the pi catalog by doing:
ssh root@<your IP address>
This saves you from prefixing a lot of commands with ”sudo”, and, more importantly, it lets you open up a
Python environment (from the terminal) and begin sending different commands to the robot’s sensors and
motors. The same default password of ”raspberry” applies to the root.
To personalize your robot, you can add a username, such as ”monte”, by typing:
sudo useradd monte
sudo passwd monte
Then, when requested by UNIX, you can enter a new password for user ”monte”; then, in the future, you
can access the robot from your laptop via:
ssh monte@<your IP address>
To change the root password, just do:

sudo passwd
and enter the new password as requested by UNIX.

Note that the robot comes with the directory /home/pi. You will probably want to add at least one new
directory, such as ”robot”, where you can store all of your robot code. For example, assume that we create
/home/pi/robot as our main robot directory.
To transfer files back and forth between this directory and the laptop, there are several options, but many
will require you to install additional software on the robot’s Raspberry Pi. A simple approach involves using
FTP (actually SFTP). The process is quite straightforward (and fully supported by your robot already):
1. Open a terminal window on your laptop and navigate to it’s robot directory, e.g. mylaptop/robot.
2. From that directory, type ”sftp root@<your IP address>”. Once you have entered the root password,
use UNIX commands such as ls and pwd to figure out where you are in the robot’s file tree, and then
use cd to navigate to the robot directory (e.g. /home/pi/robot).
3. Once in the proper robot directory on the Raspberry Pi, you have a direct connection between it and
the corresponding directory on your laptop. So put and get commands to SFTP will transfer files
from laptop to robot, and robot to laptop, respectively.
For instance, to transfer my controller.py from the laptop to the robot, type ”put my controller.py”.
And to transfer the ”image.png” file from the robot to your laptop, type ”get image.png”.
When you have transfered all relevant files to the robot, navigate to /home/pi/robot and type ”python3” on
the command line. Now you can enter Python commands at the terminal window, just like in a PyCharm
terminal window. To run any of the demos in the file robodemo.py, such as dancer, simply type:
>>> from robodemo import *
>>> dancer()

##Special for Windows Users##
If you are using a Windows machine, access to the Raspberry Pi is slightly different, but still quite easy.

###Putty###
Windows does not have built-in support for ssh from the command line, so you will need some 3rd-party
software. A good alternative is putty, which you can download here:
http://www.chiark.greenend.org.uk/?sgtatham/putty/download.html
Warning: Due to problems with the tilde (?), you may need to directly TYPE the above URL (or at least
the tilde) into your browser. Cutting and pasting the URL from this document may give a broken link due
to differences in tildes between browsers and some PDF documents.
When you open putty, you get a window with a ”Host Name” field (i.e. IP address). Just enter root@<your
IP address> and click ”Open”. This opens a terminal window on the Raspberry Pi, where you can log in
and begin running commands.

###Filezilla###
You will also need a mechanism for transfering files between the Raspberry Pi and Windows, which does not
support command-line sftp. Filezilla is a good tool for the job:
https://filezilla-project.org/download.php?type=client

Open Filezilla and choose File ?Site Manager, then use ”New Site” to create a site, whose information can
be entered or changed on the right side of the site manager. The host is the IP address of your Raspberry
Pi, the port is 22, and the protocol is SFTP. The logon type is Normal, and the username and password are
those that you’ve set for your Raspberry Pi. Just click ”Connect” to open the connection, at which point
two windows will appear: your PC on the left and the Raspberry Pi on the right. Now you can drag and
drop files between the two windows.


