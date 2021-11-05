#! /bin/sh

echo "Setting up Seeing Box..."

ln -s /home/pi/SeeingBox/SeeingBox.sh /etc/init.d/SeeingBox.sh
update-rc.d SeeingBox.sh defaults
/etc/init.d/SeeingBox.sh start

ln -s /home/pi/SeeingBox/SeeingBox-onoff.sh /etc/init.d/SeeingBox-onoff.sh
update-rc.d SeeingBox-onoff.sh defaults
/etc/init.d/SeeingBox-onoff.sh start

echo "All done. Enjoy!"

exit 0