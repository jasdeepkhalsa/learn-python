#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#       domaincheck.py
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
#       
#       
import re
import urllib

def main():
  domain_name = raw_input("Enter a domain name: ")
  tld = raw_input("co.uk or com: ")
  domaincheckURL = "https://cp.domaincheck.co.uk/hspc/domains.php?action=check_domains&domain_selection_type=single&dm_action=register_new&domain_name=%s&tld=%s" %(domain_name, tld)
  domaincheckResult = urllib.urlopen(domaincheckURL).read()
  #open("text.html","w").writelines(domaincheckResult)
  domaincheckPatternNotAvailable = '<span class="Error">(%s.%s)</span>' % (domain_name, tld)
  domaincheckPatternAvailable = '<td>\s*(%s.%s)\s*</td>' % (domain_name, tld)
  for x in re.findall(domaincheckPatternNotAvailable,domaincheckResult,flags=re.DOTALL):
    print x
    print "Not Available"
  for x in re.findall(domaincheckPatternAvailable,domaincheckResult,flags=re.DOTALL):
    print x
    print "Available"

if __name__ == '__main__':
	main()

