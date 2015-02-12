#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright © 2014 Sébastien Gross <seb•ɑƬ•chezwam•ɖɵʈ•org>
# Created: 2015-02-10
# Last changed: 2015-02-12 20:32:54
#
# This program is free software. It comes without any warranty, to
# the extent permitted by applicable law. You can redistribute it
# and/or modify it under the terms of the Do What The Fuck You Want
# To Public License, Version 2, as published by Sam Hocevar. See
# http://sam.zoy.org/wtfpl/COPYING for more details.
#
# This file is not part of Ansible

import re
import fnmatch


def match_hosts(string, expr, use_regex=False):
    '''Match STRING against all expression from EXPR and return True is at least
    one match has been done or if EXPR is undefined.

    EXPR can either be a string or a list.

    If USE_REGEX is True, regular expression is used instead of fnmach.
    '''
    if not expr:
        return True

    if type(expr) != type([]):
        expr = [ expr ]

    if use_regex:
        ret = [ True for r in expr if re.match( r'^%s$' % r, string) ]
    else:
        ret = [ True for r in expr if fnmatch.fnmatch(string, r) ]
    return any(ret)


class FilterModule(object):
    ''' Ansible custom extra filters.'''

    def filters(self):
        return {
            'match_hosts': match_hosts,
        }
    
