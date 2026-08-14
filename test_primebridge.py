# test_primebridge.py
"""
Tests for PrimeBridge module.
"""

import unittest
from primebridge import PrimeBridge

class TestPrimeBridge(unittest.TestCase):
    """Test cases for PrimeBridge class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = PrimeBridge()
        self.assertIsInstance(instance, PrimeBridge)
        
    def test_run_method(self):
        """Test the run method."""
        instance = PrimeBridge()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
