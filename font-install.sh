#bin/bash
echo "Installing Truetype font support"
sudo apt-get install ttf-mscorefonts-installer

echo "Downloading font zip, and extracting"
wget http://dl.1001fonts.com/runes.zip && unzip runes.zip
echo
echo
echo "Creating /usr/share/fonts/truetype/runes"
sudo mkdir /usr/share/fonts/truetype/runes

echo "Moving Runes.ttf and Readme to /usr/share/fonts/truetype/runes"
sudo mv Runes.ttf /usr/share/fonts/truetype/runes
sudo mv 1001* /usr/share/fonts/runes

echo "Cleaning up..."
rm runes.zip

echo "Updating font cache"
sudo fc-cache -fv

echo
echo "Complete."







