#bin/bash
#echo "Installing Truetype font support"
#sudo apt-get install ttf-mscorefonts-installer
#Installer presumes this is already installed for sudoless installation

echo "Downloading font zip, and extracting"
wget http://dl.1001fonts.com/runes.zip && unzip runes.zip
echo
echo

echo "Moving Runes.ttf and Readme to ~/.fonts/"
mv Runes.ttf ~/.fonts/
mv 1001* ~/.fonts/

echo "Cleaning up..."
rm runes.zip

echo "Updating font cache"
fc-cache -fv

echo
echo "Complete."







