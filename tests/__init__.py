# -*- coding: utf-8 -*-
"""
    tests/__init__.py

"""
import unittest

import trytond.tests.test_tryton

from tests.test_party import TestParty


def suite():
    """
    Define suite
    """
    test_suite = trytond.tests.test_tryton.suite()
    test_suite.addTests([
        unittest.TestLoader().loadTestsFromTestCase(TestParty),
    ])
    return test_suite

if __name__ == '__main__':
    unittest.TextTestRunner(verbosity=2).run(suite())
