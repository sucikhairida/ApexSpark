# test_apexspark.py
"""
Tests for ApexSpark module.
"""

import unittest
from apexspark import ApexSpark

class TestApexSpark(unittest.TestCase):
    """Test cases for ApexSpark class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = ApexSpark()
        self.assertIsInstance(instance, ApexSpark)
        
    def test_run_method(self):
        """Test the run method."""
        instance = ApexSpark()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
