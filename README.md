# EXIF modifier - make your photos great again!

Did you ever copy some photos to your new laptop or a streaming server, and (boom!) they all got modified a few seconds ago, but not in May, 98th? And your favorite photo manager treats them taken today? Our maybe you have several thousands photos like these?

It was the case for me, when I lost (occasionally, of course) modification time (aka mtime) of almost 40k photos... My favourite [Plex.tv](https://plex.tv) confirmed all they were taken today.

# Lost? Found!

As a Python newbie I decided to help myself and write a small tool, that can fix these "defects" for me (yeah, I'm lazy and know it.) Some debugging hours and now this tool helps me and my friends. We just run a small script that does the job for us. Would you like to join us?

# How does it work?

The script `exif-modifier.py` scans all items under a folder where it is run and does:

* converts any upper-case letter in a filename to lower-case, so `MyPhoto123.JPG` becomes `myphoto123.jpg` (this section can be commented, of course, but saves you from many other issues on the other side)
- gets *best* date/time match from EXIF (meta) data (e.g. your camera may set several timestamps on a photo, but one date/time is *more* likely to be actual, than others)
- changes ctime/mtime to EXIF data (so your .jpg is 11 of May, 98th again, not today); file's modification date/time will be changed if EXIF and OS date/time differ greatly (at least *two* days)

# Examples and usage instructions

> Install `ExifRead` Python library by `$ pip install ExifRead` before you go for the very first time

* either clone the project or save `exif-modifier.py` somewhere (say, `/tmp/exif-modifier.py`)
- walk into your photos directory (e.g., `$ cd ~/Documents/my-photos`)
- run the script, e.g. `$ /tmp/exif-modifier.py`
- check output: INFO - some actions were done and you are good, WARNING - incorrect EXIF block in .jpg or it is absent, see some hints below
- you are done!

# Hints

Sometimes you have incorrect EXIF data in a .jpg or it does not exist at all. What to do?

* install `exiftool`, e.g. run `$ brew install exiftool` on Mac OS
- run `$ exiftool -CreateDate='2012:01:05 21:01:06' -'DateTimeOriginal'='2012:01:05 21:01:06' myphoto.jpg` to change/add EXIF data in `myphoto.jpg` to 21:01 of 5th of January, 2012
- re-run `exif-modifier.py` (see above)

# Hooray!

That's it. No more magic. Your photos are great again. Enjoy and don't hesitate to react me at i@vyakovlev.com in case of any difficulties.

## Licenses and agreements

MIT, 2017 [Vladimir Yakovlev](https://vyakovlev.com)