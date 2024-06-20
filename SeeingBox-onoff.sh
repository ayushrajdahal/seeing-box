#! /bin/sh

### BEGIN INIT INFO
# Provides:          SeeingBox-onoff.py
# Required-Start:    $remote_fs $syslog
# Required-Stop:     $remote_fs $syslog
# Default-Start:     2 3 4 5
# Default-Stop:      0 1 6
# Description:       Init script to start and stop SeeingBox-onoff.py
### END INIT INFO

# Place any commands here that should be executed before the init script actions
# Currently, no pre-actions are needed

# Define actions based on the first argument passed to the script
case "$1" in
  start)
    # Action to perform when 'start' is passed
    echo "Starting SeeingBox-onoff.py"
    # Run the SeeingBox-onoff.py script in the background
    /home/pi/z/SeeingBox-onoff.py &
    ;;
  stop)
    # Action to perform when 'stop' is passed
    echo "Stopping SeeingBox-onoff.py"
    # Kill the process running SeeingBox-onoff.py
    pkill -f /home/pi/z/SeeingBox-onoff.py
    ;;
  *)
    # Default action when the script is not passed 'start' or 'stop'
    echo "Usage: /etc/init.d/SeeingBox-onoff.sh {start|stop}"
    exit 1
    ;;
esac

# Exit the script with a success status
exit 0
