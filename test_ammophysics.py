# test_ammophysics.py
"""
Tests for AmmoPhysics module.
"""

import unittest
from ammophysics import AmmoPhysics

class TestAmmoPhysics(unittest.TestCase):
    """Test cases for AmmoPhysics class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = AmmoPhysics()
        self.assertIsInstance(instance, AmmoPhysics)
        
    def test_run_method(self):
        """Test the run method."""
        instance = AmmoPhysics()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
