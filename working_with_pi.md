# Working with the PI

An easy way of working with the Pi would be to connect it to the network with an Ethernet connection and then to use 
the secure shell server running on the Pi (ssh).
However, due to network management restrictions at TU Delft, this is not allowed.
As an alternative, you can use the serial pins (UART) on the Pi B+ board and the console cable to connect to a TUD machine or your laptop.
How to do this depends on the operating system of this computer.

We recommend you use Linux, either natively, in a virtualbox, or on one of the TUD computers at the
lab or your own laptop.
Especially for this lab it is very useful, because the RaspberryPi also runs Linux, and is installed
on a Linux partition type with a Linux ext2 filesystem.

Note that the serial connection will flush the output through the buffer during boot, so if you
connect after booting, you won't see anything appearing.
You can start typing the username nonetheless.

## Linux

In Linux there are two primary methods of working with the PI over the UART:

- Connect to the Pi, login, and create, compile, and run programs on the Pi.
  To open a tty connection directly, use `screen /dev/ttyUSB0 115200`.
  This will drop you in a Linux bash shell on the Pi where you can login and use all shell features.
  It won't allow you to copy files directly however, so you will either need to work on the Pi or
  to copy things through the clipboard into your editor of choice on the Pi (try `nano` or `vi`).
  You might need to use `sudo` to acquire the relevant rights if you use your own laptop.

- Develop programs locally, that is, on a TUD computer or your laptop, and run them on the Pi by copying files onto the sdcard.
  The sdcard is formatted with two partitions: a boot and the root filesystem.
  This option is not available on TUD computers, because you will need root access.
  You'll have to mount the second partition and move files to a location of your choice:

      # look at dmesg to find out the /dev/??? that belongs to the sdcard
      dmesg | tail

      # mount the device's 2nd partition
      # on my laptop it was /dev/mmcblk0p2
      sudo mount /dev/mmcblk0p2 /mnt

      # copy your source to the Pi home directory
      cp -R path/to/source /mnt/home/pi

  You'll still need to connect to the TTY using the above method to run things.

## Windows

The only way to work from Windows is by connecting [PuTTY](http://www.putty.org) to the right serial
port.

In case you are using your own Windows laptop, it is necessary to install the
corresponding drivers. In that case, if you have not already done so, install the PL2303 drivers.
These can be downloaded from [here](http://www.prolific.com.tw/US/ShowProduct.aspx?p_id=225&pcid=41)

Before you are able to connect to the device, you need to know to which communication port the
Raspberry Pi is connected.
You can find this by looking in the Ports section of the Windows Device Manager, which is accessible
through the Control Panel under System, or by right click inspection of the right device in "Devices and
Printers".

Inside PuTTY your can now simply select `serial`, set the speed to 115200, and enter the com port number.
