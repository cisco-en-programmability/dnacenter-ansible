#!/usr/bin/env python
from __future__ import (absolute_import, division, print_function)
__metaclass__ = type


class AnsibleDNACException(Exception):
    """Base class for all Ansible DNAC package exceptions."""

    pass


class InvalidFunction(AnsibleDNACException):
    pass


class StateNotSupported(AnsibleDNACException):
    pass


class NoMatchingOperation(AnsibleDNACException):
    pass


class MultipleOperations(AnsibleDNACException):
    pass
