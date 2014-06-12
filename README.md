Installation:
	1.) Install dependencies from /FuseGUI/dependencies
	2.) Drag /FuseGUI/dist/FuseGUI.app to /Applications

Note: 	If there are problems after step 2, build the application from source. 
		In terminal:
			sudo pip install -U py2app
			cd /...<parent directories>.../FuseGUI
			python setup.py py2app
		Then try moving the newer /FuseGUI/dist/FuseGUI.app to /Applications.