==================
Circuit Playground
==================

Make lights blink and other stuff with a Circuit Playground board.


Mounting Storage
================

After plugging in the board via USB, check *dmesg* output to determine
the storage device.

You can check the drive info as so::

  $ sudo blkid /dev/sdb1
  /dev/sdb1: SEC_TYPE="msdos" LABEL="CIRCUITPY" UUID="4921-8571" TYPE="vfat"

You can then mount the drive as so::

  $ sudo mount LABEL="CIRCUITPY" /mnt
