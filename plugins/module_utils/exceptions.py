#!/usr/bin/env python


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
