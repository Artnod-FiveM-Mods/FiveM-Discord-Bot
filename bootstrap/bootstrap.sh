#!/bin/bash
VERSION=1

if [ `id -u` -ne 0 ]; then
	echo "This script has to be run as root!"
	exit 1
fi
RUNINSTALL=0
APTDEPENDENCIES="python3 python3-pip"
PIPDEPENDENCIES="discord lxml requests"
if [ -n "$(command -v apt-get)" ]; then
	ISDEBIAN=1
else
	ISDEBIAN=0
fi

showHelp() {
	echo "fivem Discord Bot bootstrapper version $VERSION"
	echo
	echo "Usage: ./bootstrap.sh [-h] -i"
	echo "Parameters:"
	echo "  -h   Print this help screen and exit"
	echo "  -i   Required to actually start the installation"
}

intro() {
	echo
	echo "fivem Discord Bot bootstrapper"
	echo
	echo "This will install a fivem Discord Bot according to the information"
	echo
	# read -p "Press enter to continue"
	echo -e "\n=============================================================\n"
}

nonDebianWarning() {
	if [ $ISDEBIAN -eq 0 ]; then
		echo "NOTE: It seems like this system is not based on Debian."
		echo "Although installation of the scripts"
		echo "will work the bot scripts will probably"
		echo "fail because of missing dependencies. Make sure you check"
		echo "the website regarding the prerequisites"
		echo
		echo "Do you want to continue anyway?"
		select yn in "Yes" "No"; do
			case $yn in
				Yes)
					echo "Continuing..."
					break;;
				No)
					echo "Aborting."
					exit 0
					;;
			esac
		done
		echo -e "\n=============================================================\n"
	fi
}

installAptDeps() {
	echo -e "Installing dependencies\n"
	apt-get update -y
	apt-get install -y $APTDEPENDENCIES
	echo -e "\n=============================================================\n"
}

installPipDeps() {
	echo -e "Installing optional dependencies\n"
	pip3 install $PIPDEPENDENCIES
	echo -e "\n=============================================================\n"
}

checkSetupDeps() {
	for DEP in screen python3 python3-pip; do
		which $DEP > /dev/null 2>&1
		if [ $? -ne 0 ]; then
			echo "\"$DEP\" not installed. Please install it and run this script again."
			exit 1
		fi
	done
	
}


installBotScripts() {
	echo -e "Downloading and installing bot scripts"
	echo "  - Download scripts"
	wget -nv -q --show-progress https://github.com/Artnod-FiveM-Mods/FiveM-Discord-Bot/archive/master.zip -O /tmp/DiscordBot.zip

	echo "  - Extract scripts"
	TMPPATH=`mktemp -d`
	unzip -q /tmp/DiscordBot.zip -d $TMPPATH
	cp -R $TMPPATH/7dtd_discordBot-master/scripts/* /

	chown root:root -R /usr/local/bin/fivembot
	chmod 775 -R /usr/local/bin/fivembot
	chown root:root /etc/init.d/discord_bot
	chown root:root /etc/init.d/discord_hook
	chmod 755 /etc/init.d/discord_bot	
	chmod 755 /etc/init.d/discord_hook

	rm -R $TMPPATH
	rm /tmp/DiscordBot.zip

	echo "  - Enable deamon"
	update-rc.d discord_bot defaults
	update-rc.d discord_hook defaults
	systemctl daemon-reload
	echo -e "\n=============================================================\n"
}

finish() {
	if [ $ISDEBIAN -eq 0 ]; then
		echo
		echo "You are not running a Debian based distribution."
		echo "The following things should manually be checked:"
		echo " - Existence of prerequsities"
		echo " - Running the init-script on boot"
	else
		echo -e "ALL DONE"
	fi
}

main() {
	intro
	nonDebianWarning
	if [ $ISDEBIAN -eq 1 ]; then
		installAptDeps
		installPipDeps
	else
		checkSetupDeps
	fi
	installBotScripts
	finish
}

if [ -z $1 ]; then
	showHelp
	exit 0
fi
while getopts "hcoi" opt; do
	case "$opt" in
		h)
			showHelp
			exit 0
			;;
		i)
			RUNINSTALL=1
			;;
	esac
done
if [ $RUNINSTALL -eq 1 ]; then
	main
fi
