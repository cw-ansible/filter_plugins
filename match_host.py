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
    
