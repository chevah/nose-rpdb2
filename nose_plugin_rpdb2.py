# Copyright (c) 2012 Adi Roiban.
# See LICENSE for details.
"""
This plugin provides the ``--rpdb2`` option. The ``--rpdb2`` option will drop
the test runner into rpdb2 remote debugger when it encounters an
error or a failure.
"""

import sys
from nose.plugins.base import Plugin

class RPDB2Plugin(Plugin):
    """
    Nose pluging for using rpdb2 remote debugger.
    """
    name = 'rpdb2'
    score = 10  # run last, among builtins

    enabled = False
    password = 'password'
    timeout = 30

    def options(self, parser, env):
        """
        Register commandline options.
        """
        super(RPDB2Plugin, self).options(parser, env=env)
        parser.add_option(
            "--rpdb2", action="store_true", dest="rpdb2_enabled",
            default=env.get('NOSE_RPDB2', False),
            help="Drop into rpdb2 on errors or failures.",
            )
        parser.add_option(
            "--rpdb2-password", action="store", type="string",
            dest="rpdb2_password",
            default=self.password,
            help="Password used by the rpdb2 session.",
            )
        parser.add_option(
            "--rpdb2-timeout", action="store", type="int",
             dest="rpdb2_timeout",
            default=self.timeout,
            help="Timeout used by the rpdb2 session.",
            )

    def configure(self, options, config):
        """
        Configure the pluggin.
        """
        super(RPDB2Plugin, self).configure(options, config)
        self.config = config
        self.enabled = options.rpdb2_enabled
        self.password = options.rpdb2_password
        self.timeout = options.rpdb2_timeout

    def addError(self, test, err):
        """
        Enter ipdb on errors.
        """
        self.startRemoteDebugger(err)

    def addFailure(self, test, err):
        """
        Enter ipdb on failures.
        """
        self.startRemoteDebugger(err)

    def startRemoteDebugger(self, err):
        """
        Launch the rpdb2 session.
        """
        import rpdb2
        stdout = sys.stdout
        sys.stdout = sys.__stdout__
        sys.stdout.write(
            'You have %d seconds to connect to the remote debugger using '
            '"%s" password.' % (self.timeout, self.password))
        try:
            rpdb2.start_embedded_debugger(
                self.password, timeout=self.timeout, fAllowRemote=True)
        finally:
            sys.stdout = stdout
