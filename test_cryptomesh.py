# test_cryptomesh.py
"""
Tests for CryptoMesh module.
"""

import unittest
from cryptomesh import CryptoMesh

class TestCryptoMesh(unittest.TestCase):
    """Test cases for CryptoMesh class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = CryptoMesh()
        self.assertIsInstance(instance, CryptoMesh)
        
    def test_run_method(self):
        """Test the run method."""
        instance = CryptoMesh()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
