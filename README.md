# Procedure

<!-- 
## vlc_virtual_env
Files for the VLC virtual env setup.


## microsoft terminal
Setup the microsoft terminal for the VLC anaconda virtual environment. -->
 
 

## ANACONDA
	• Install Anaconda
		○ https://www.anaconda.com/products/individual
	• Open anaconda3 prompt (powershell)
		○ Press the windows button and type "anaconda". Open it (powershell):
		
		○ On the command prompt that opened, see the base environment loaded
			§ with a "(base)", showing before the command line.
		○ Type "conda update conda" to update it.
			§ Press "y" for yes, when necessary.
		○ Go to the "anaconda_virtual_env\vlc_virtual_env" path, as in my case, type:
			§ cd "C:\Users\Pablo\Documents\GitHub\anaconda_virtual_env\vlc_virtual_env"
				□ Replace "C:\Users\Pablo\Documents\GitHub\" with your path
		
		○ Type the following to setup the VLC virtual environment:
			§ conda create --name vlc --file spec-file.txt python=3.8.3
			§ It will take some time, after downloading all necessary packages.
		○ Leave the base environment, with:
			§ conda deactivate
		○ The, open the vlc virtual env, type:
			§ conda activate vlc
		○ This will show now "(vlc)" instead of "(base)". Check the packages that you just installed with:
			§ conda list
		○ If you want to open a jupyter notebook in that environment, type:
			§ ipython kernel install --user --name=vlc
		○ Then, open it, with:
			§ jupyter notebook
			§ This will ask for a brownser to open.



## WINDOWS TERMINAL:

	• Setup of a custom windows terminal, to directly open the vlc env
	• Install windows Terminal
		○ Download it in the microsoft store.
	• Open the terminal, by windows button and typing "terminal". Open it: 
		
	• Open windoes terminal setting:
		
	• This opens a json file, on a notepad.
	• Open the file "C:\Users\Pablo\Documents\GitHub\anaconda_virtual_env\microsoft terminal\settings.json"
		○ Copy its contents, and paste on the notepad open with the Windows Terminal settings.
	• Replace all instances of:
		○ "C:\\Users\\Pablo\\anaconda3\\"
		○ With your path to the anaconda installation.
		○ This will setup the startup of vlc environment as default.
	• (optional) Replace all instances of:
		○ "C:/Users/Pablo/Documents/GitHub/anaconda_virtual_env/microsoft terminal/"
		○ With your path to "anaconda_virtual_env/microsoft terminal/"
		○ This will set a background image for therminal (change it alike).


## RUN CODE:

	• Update all conda packages:
		○ conda update --all
	• Before runnning the VLC simulator, install remaining packages. Run:
		○ "C:\Users\Pablo\Documents\GitHub\anaconda_virtual_env\vlc_virtual_env\install_other_packages.bat"
		○ Replace with your path..
	• To run the VLC simulator, go to:
		○ cd "C:\Users\Pablo\Documents\GitHub\vlc_simulator\VLC_devel\source\"
		○ Replace it with your path
	• And type:
		○ python.exe .\VLC.py


## DEVELOPMENT:

	• During development, whenever a new package is installed, add it to:
		○ "C:\Users\Pablo\Documents\GitHub\anaconda_virtual_env\vlc_virtual_env\install_other_packages.bat"
		○ Replace with your path..
		○ Add like: "pip install <NEW_PACKAGE>"
	• If a new package is installed through Anaconda, re-generate the "spec-file.txt". Go to:
		○ cd "C:\Users\Pablo\Documents\GitHub\anaconda_virtual_env\vlc_virtual_env"
		○ Replace with your path.. And run
		○ conda list --explicit > spec-file.txt
	• Then, commit all changes to the repo

