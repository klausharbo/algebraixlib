"""Testing the mathobjects.couplet module."""

# $Id: test_mathobjects_couplet.py 22674 2015-07-24 20:45:24Z gfiedler $
# Copyright Algebraix Data Corporation 2015 - $Date: 2015-07-24 15:45:24 -0500 (Fri, 24 Jul 2015) $
#
# This file is part of algebraixlib <http://github.com/AlgebraixData/algebraixlib>.
#
# algebraixlib is free software: you can redistribute it and/or modify it under the terms of version
# 3 of the GNU Lesser General Public License as published by the Free Software Foundation.
#
# algebraixlib is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without
# even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License along with algebraixlib.
# If not, see <http://www.gnu.org/licenses/>.
# --------------------------------------------------------------------------------------------------
import inspect
import os
import unittest

from algebraixlib.mathobjects import Atom, Couplet, MathObject, Set
from algebraixlib.structure import CartesianProduct, GenesisSetA, PowerSet
from algebraixlib.undef import Undef

# noinspection PyUnresolvedReferences
from data_mathobjects import basic_couplets


# Ground set structures for the basic_couplets.
_basic_couplet_struct = CartesianProduct(GenesisSetA(), GenesisSetA())
_complex_couplet_struct = CartesianProduct(_basic_couplet_struct, PowerSet(GenesisSetA()))
_basic_couplets_structs = {
    '3x2': _basic_couplet_struct,
    "'5'x'4'": _basic_couplet_struct,
    "'7'x6": _basic_couplet_struct,
    'Coupl x Set': _complex_couplet_struct
}


class CoupletTest(unittest.TestCase):
    """Test the Couplet class."""

    print_examples = False

    def test_Couplet(self):
        """Create various forms of Couplets."""
        if self.print_examples:
            print('(printing examples)')  # Make 'nosetests -s' more readable.
        for test_couplet_name in basic_couplets.keys():
            self._couplet_assert(test_couplet_name)

    def _couplet_assert(self, test_couplet_name):
        """Assert that 'couplet' is a proper Couplet with left 'left' and right 'right'."""
        test_couplet = basic_couplets[test_couplet_name]
        left = test_couplet._test_val['left']
        right = test_couplet._test_val['right']
        couplet = Couplet(left=left, right=right)
        # Convert the arguments into Atoms if they are values.
        if not isinstance(left, MathObject):
            left = Atom(left)
        if not isinstance(right, MathObject):
            right = Atom(right)
        # Test the type structure.
        self.assertTrue(isinstance(couplet, MathObject))
        self.assertFalse(isinstance(couplet, Atom))
        self.assertTrue(isinstance(couplet, Couplet))
        self.assertFalse(isinstance(couplet, Set))
        # Compare the values of right and left.
        left_val = couplet.left
        right_val = couplet.right
        self.assertEqual(left_val, left)
        self.assertEqual(right_val, right)
        # Test that the representation caching doesn't change the value.
        couplet_repr = repr(couplet)
        self.assertEqual(couplet_repr, repr(couplet))
        # Check structure.
        self.assertEqual(test_couplet.get_ground_set(), _basic_couplets_structs[test_couplet_name])
        # Test left set and functionality.
        self.assertIs(couplet.get_left_set(), Undef())
        self.assertIs(couplet.is_functional(), Undef())
        self.assertIs(couplet('callable'), Undef())
        # Make sure that the representation evaluates to a couplet that compares equal.
        repr_exec = 'self.assertEqual(couplet, {0})'.format(repr(couplet))
        exec(repr_exec)
        # Print the representation and the string conversion.
        if self.print_examples:
            print('repr(Couplet(left={left}, right={right})) = {repr}'.format(
                left=repr(left_val), right=repr(right_val), repr=couplet_repr))
            print('str(Couplet(left={left}, right={right})) = {str}'.format(
                left=str(left_val), right=str(right_val), str=str(couplet)))

    def test_operators(self):
        """Test operators"""
        a = Atom(1)
        c = Couplet(1, 2)
        self.assertTrue(a != c)
        self.assertTrue(c != a)

    def test_invalid_constructs(self):
        """Test invalid Couplets."""
        self.assertRaises(TypeError, lambda: Couplet(Undef(), 2))
        self.assertRaises(TypeError, lambda: Couplet(1, right=Undef()))

    def test_properties(self):
        def _test_undef(cc):
            self.assertIs(cc.get_left_set(), Undef())
            self.assertIs(cc.is_functional(), Undef())
            self.assertIs(cc.get_right_set(), Undef())
            self.assertIs(cc.is_right_functional(), Undef())
            self.assertIs(cc.is_bijective(), Undef())
            self.assertIs(cc.is_transitive(), Undef())
            self.assertIs(cc.is_equivalence_relation(), Undef())
        c = Couplet(1, 2)
        _test_undef(c)
        self.assertFalse(c.is_reflexive())
        c = Couplet(1)
        _test_undef(c)
        self.assertTrue(c.is_reflexive())

    def test_flags_cache(self):
        c = Couplet(1, 2)
        self.assertFalse(c.cached_is_relation)
        self.assertTrue(c.cached_is_not_relation)
        self.assertFalse(c.cached_is_clan)
        self.assertTrue(c.cached_is_not_clan)
        self.assertFalse(c.cached_is_multiclan)
        self.assertTrue(c.cached_is_not_multiclan)
        self.assertFalse(c.cached_is_functional)
        self.assertFalse(c.cached_is_not_functional)
        self.assertFalse(c.cached_is_right_functional)
        self.assertFalse(c.cached_is_not_right_functional)
        self.assertFalse(c.cached_is_regular)
        self.assertFalse(c.cached_is_not_regular)
        self.assertFalse(c.cached_is_reflexive)
        self.assertFalse(c.cached_is_not_reflexive)
        self.assertFalse(c.cached_is_symmetric)
        self.assertFalse(c.cached_is_not_symmetric)
        self.assertFalse(c.cached_is_transitive)
        self.assertFalse(c.cached_is_not_transitive)

        self.assertRaises(AssertionError, lambda: c.cache_is_relation(True))
        self.assertRaises(AssertionError, lambda: c.cache_is_clan(True))
        self.assertRaises(AssertionError, lambda: c.cache_is_multiclan(True))

        self.assertRaises(Exception, lambda: c.cache_is_transitive(False))
        self.assertRaises(Exception, lambda: c.cache_is_functional(False))
        self.assertRaises(Exception, lambda: c.cache_is_right_functional(False))
        self.assertRaises(Exception, lambda: c.cache_is_regular(False))
        self.assertRaises(Exception, lambda: c.cache_is_reflexive(False))
        self.assertRaises(Exception, lambda: c.cache_is_symmetric(False))
        self.assertRaises(Exception, lambda: c.cache_is_transitive(False))

    def test__str__(self):
        """Verify __str__() returns the representation of a Couplet object."""
        s = str(Couplet(1, 2))
        self.assertEqual(s, '(1->2)')

    def test_optional_right(self):
        """Test optional right"""
        c1 = Couplet(1, 1)
        c2 = Couplet(1)
        self.assertEqual(c1, c2)

# --------------------------------------------------------------------------------------------------
if __name__ == '__main__':
    # The print is not really necessary. It helps making sure we always know what we ran in the IDE.
    print('main: {file}'.format(file=os.path.basename(inspect.getfile(inspect.currentframe()))))
    unittest.main()
