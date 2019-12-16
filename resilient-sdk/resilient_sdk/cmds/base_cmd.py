#!/usr/bin/env python
# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2019. All Rights Reserved.

import argparse
from resilient import ensure_unicode


class BaseCmd(object):
    """
    Base Class for implementing a resilient-sdk command e.g. codegen
    Sub classes must set/implement:
        -   CMD_NAME
        -   CMD_HELP
        -   setup(self)
        -   execute_comment(self, args)

    On initialization, it sets self.parser, then calls the sub-classes' setup method.
    This allows us to add custom command line args for each sub_command.
    See codegen.py for an example.
    """

    CMD_NAME = None
    CMD_HELP = None
    CMD_USAGE = None
    CMD_DESCRIPTION = None
    CMD_USE_COMMON_PARSER_ARGS = False  # Set this to True in sub class to include the common_parser arguments

    def __init__(self, sub_parser):

        assert self.CMD_NAME
        assert self.CMD_HELP

        if self.CMD_USE_COMMON_PARSER_ARGS:
            self.parser = sub_parser.add_parser(self.CMD_NAME, help=self.CMD_HELP, parents=self._get_common_parser())
        else:
            self.parser = sub_parser.add_parser(self.CMD_NAME, help=self.CMD_HELP)

        self.setup()

    def setup(self):
        """Sub classes should implement this method"""
        raise NotImplementedError()

    def execute_command(self, args):
        """Sub classes should implement this method"""
        raise NotImplementedError()

    @staticmethod
    def _get_common_parser():
        """
        Create a 'common parser' with all below arguments

        :return: A single argparse.ArgumentParser in a List
        :rtype: List
        """
        common_parser = argparse.ArgumentParser(add_help=False)

        common_parser.add_argument("-f", "--function",
                                   type=ensure_unicode,
                                   help="Generate code for the specified function(s)",
                                   nargs="*")

        common_parser.add_argument("-m", "--messagedestination",
                                   type=ensure_unicode,
                                   help="Generate code for all functions that use the specified message destination(s)",
                                   nargs="*")

        common_parser.add_argument("--workflow",
                                   type=ensure_unicode,
                                   help="Include customization data for workflow(s)",
                                   nargs="*")

        common_parser.add_argument("--rule",
                                   type=ensure_unicode,
                                   help="Include customization data for rule(s)",
                                   nargs="*")

        common_parser.add_argument("--field",
                                   type=ensure_unicode,
                                   help="Include customization data for custom incident field(s)",
                                   nargs="*")

        common_parser.add_argument("--datatable",
                                   type=ensure_unicode,
                                   help="Include customization data for datatable(s)",
                                   nargs="*")

        common_parser.add_argument("--task",
                                   type=ensure_unicode,
                                   help="Include customization data for automatic task(s)",
                                   nargs="*")

        common_parser.add_argument("--script",
                                   type=ensure_unicode,
                                   help="Include customization data for script(s)",
                                   nargs="*")

        common_parser.add_argument("--artifacttype",
                                   type=ensure_unicode,
                                   help="Include customization data for artifact types(s)",
                                   nargs="*")

        common_parser.add_argument("--exportfile",
                                   type=ensure_unicode,
                                   help="Generate based on organization export file (.res)")

        common_parser.add_argument("-o", "--output",
                                   type=ensure_unicode,
                                   help="Path to output file")

        return [common_parser]
