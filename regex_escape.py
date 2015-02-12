#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright © 2014 Sébastien Gross <seb•ɑƬ•chezwam•ɖɵʈ•org>
# Created: 2015-02-10
# Last changed: 2015-02-12 20:33:20
#
# This program is free software. It comes without any warranty, to
# the extent permitted by applicable law. You can redistribute it
# and/or modify it under the terms of the Do What The Fuck You Want
# To Public License, Version 2, as published by Sam Hocevar. See
# http://sam.zoy.org/wtfpl/COPYING for more details.
#
# This file is not part of Ansible

import re

def regexp_escape(string):
    '''Escape all regular expressions special characters from STRING.

To escape special characters within a regex, use the "regex_escape" filter::

    # convert '^f.*o(.*)$' to '\^f\.\*o\(\.\*\)\$'
    {{ '^f.*o(.*)$' | regex_escape() }}
'''
    return re.escape(string)


class FilterModule(object):
    '''Ansible extra jinja2 filters'''

    def filters(self):
        return {
            'regexp_escape': regexp_escape,
        }
