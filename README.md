# PwManager
Tried to develop a simple password manager using fernet.

To use the password manager you first need to run the setup.py file. 
Afterwards run the PwManager script and you are good to go.

The setup file will generate a fernet key for you. You have to strip the b' at the start and the ' at the end to use it propely. 
Store this key in a file on a USB stick for example. At least not on the same pc because with it someone could reverse the encryption of you passwords and use them.
The account names are not encrypted just the passwords.

I still have to formate the print statements. At the moment the print outs are all over the place.

I am aware that some functions have to be refined if you find issues with the programm pls report them.
