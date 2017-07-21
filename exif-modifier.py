#!/usr/bin/env python
# -*- coding: utf-8 -*-

############################################################################################################
#### Makes photos great again
#### Written by Vladimir Yakovlev <i@vyakovlev.com>
#### Version 0.1.2
############################################################################################################

import os
import sys
import datetime
import time
import fnmatch
# you probably need to run "pip install ExifRead" before go
import exifread

# i will walk deeper from your entry point (./) to find all items i can fix
for root, dirs, files in os.walk('./', topdown=False):
   # walk thru all files
   for file in files:
      fullname_old = os.path.join(root, file)
      fullname = os.path.join(root, file.lower())

      # rename files to lowercase first
      if fullname != fullname_old:
         os.rename(fullname_old,fullname)
         print "INFO: renamed upper-case %s to lower-case %s" % (fullname_old,fullname)

      # for .jpg file
      if fnmatch.fnmatch(file, '*.jpg'):
         image = open(fullname, 'rb')
         tags = exifread.process_file(image) # this is not dangerous: no tags - no issues

         # determine date/time from EXIF data: from best match to worst
         exit_date_str = None
         if 'EXIF DateTimeOriginal' in tags:
            exit_date_str = str(tags['EXIF DateTimeOriginal'])
         elif 'EXIF DateTimeDigitized' in tags:
            exit_date_str = str(tags['EXIF DateTimeDigitized'])
         elif 'Image DateTime' in tags:
            exit_date_str = str(tags['Image DateTime'])

         if exit_date_str == None:
            print "WARNING: no EXIF date/time data found in %s - please add manually (see README)" % fullname
         else:
            try:
               # convert time to computer-readable
               exif_time = time.mktime(datetime.datetime.strptime(exit_date_str, '%Y:%m:%d %H:%M:%S').timetuple())
            except (OverflowError,ValueError):
               print "WARNING: incorrect EXIF date/time in %s: %s - please correct manually (see README)" % (fullname,exit_date_str)
               continue
            # get mtime from file in seconds from epoch
            mtime = os.path.getmtime(fullname)
            # mtime and time from EXIF should be more or less the same
            diff = abs(mtime-exif_time) # abs of seconds between dates
            if diff > 172800: # over two days difference?
               print "INFO: mtime and EXIF time of %s differ (>%s secs) - will update now from %s to %s" % (fullname,diff,time.ctime(mtime),time.ctime(exif_time))
               os.utime(fullname,(exif_time,exif_time))