# test_graystone.py
"""
Tests for GrayStone module.
"""

import unittest
from graystone import GrayStone

class TestGrayStone(unittest.TestCase):
    """Test cases for GrayStone class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = GrayStone()
        self.assertIsInstance(instance, GrayStone)
        
    def test_run_method(self):
        """Test the run method."""
        instance = GrayStone()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
