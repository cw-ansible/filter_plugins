#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright © 2014 Sébastien Gross <seb•ɑƬ•chezwam•ɖɵʈ•org>
# Created: 2015-02-10
# Last changed: 2015-06-19 12:54:43
#
# This program is free software. It comes without any warranty, to
# the extent permitted by applicable law. You can redistribute it
# and/or modify it under the terms of the Do What The Fuck You Want
# To Public License, Version 2, as published by Sam Hocevar. See
# http://sam.zoy.org/wtfpl/COPYING for more details.
#
# This file is not part of Ansible

import os
import re
import fnmatch
import ansible

def custom_store(file, hostvars):
    '''Find a 'file' in custom storage as defined by 'custom_path'.

File is looked up in:
 - 'inventory_hostname_short'
 - 'group_names'
 - all.yml

If not found, or if 'hostvars' is None, returns 'file'.

hostvars should be: hostvars[ansible_hostname].

Example:
  - ssh_key: '{{ lookup("file", "/credentials/john.pub" | custom_store(hostvars[ansible_hostname])) }}'
'''
    #print hostvars
    if hostvars is None:
        return file
    for p in [ hostvars['inventory_hostname_short'] ] + hostvars['group_names'] + [ 'all' ]:
        ret = os.path.normpath((hostvars['custom_path'] % ('store', p)) + file)
        if os.path.exists(ret):
            return ret
    return file

import pprint
class FilterModule(object):
    ''' Ansible core jinja2 filters '''
    
    def filters(self):
        return {
            'custom_store': custom_store,
        }

if __name__ == "__main__":
    match()
    
