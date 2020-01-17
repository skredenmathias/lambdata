#!/usr/bin/env python

import unittest
from acme import Product
from acme_report import generate_products, ADJECTIVES, NOUNS


class AcmeProductTests(unittest.TestCase):
    """Making sure Acme products are the tops!"""
    def test_default_product_price(self):
        """Test default product price being 10."""
        prod = Product('Test Product')
        self.assertEqual(prod.price, 10)

    def test_product_weight_over10(self):
        """Test if a product weighs more than 10"""
        prod = Product('Test Product')
        self.assertTrue(prod.weight > 10)

    def test_products_not_equal(self):
        """Tests if two products are equal."""
        prod1 = Product('Test Product')
        prod2 = Product('Test Product')
        self.assertIsNot(prod1, prod2)


class AcmeReportTests(unittest.TestCase):
    """docstring"""
    def test_default_num_products(self):
        """docstring"""
        prod = generate_products('Test Product list??')
        self.assertEqual(len(prod), 30)

    def test_legal_names(self):
        """docstring"""
        prod =  # smh


if __name__ == '__main__':
    unittest.main()
