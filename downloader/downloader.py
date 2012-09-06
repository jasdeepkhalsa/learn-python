#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#       Downloader.py
#       
#       Copyright 2012 JasdeepKhalsa <jasdeepharibhajan@jasdeepharibhajan>
#       
#       This program is free software; you can redistribute it and/or modify
#       it under the terms of the GNU General Public License as published by
#       the Free Software Foundation; either version 2 of the License, or
#       (at your option) any later version.
#       
#       This program is distributed in the hope that it will be useful,
#       but WITHOUT ANY WARRANTY; without even the implied warranty of
#       MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#       GNU General Public License for more details.
#       
#       You should have received a copy of the GNU General Public License
#       along with this program; if not, write to the Free Software
#       Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#       MA 02110-1301, USA.
import urllib
download_dir = "./"
def main():
  f = open("download.txt","r")
  for url in f:
    try:
      print "Downloading...", url
      filename_list = url.split("/")
      filename = filename_list[-1]
      filepath = download_dir+filename
      urllib.urlretrieve(url,filepath)
      print "Downloaded to:", filepath
    except IOError:
      print "Error:", IOError
      print "Cannot Download:", url

if __name__ == '__main__':
	main()
