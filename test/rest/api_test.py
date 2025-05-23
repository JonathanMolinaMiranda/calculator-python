import http.client
import os
import unittest
from urllib.request import urlopen

import pytest

BASE_URL = os.environ.get("BASE_URL")
DEFAULT_TIMEOUT = 2  # in secs


@pytest.mark.api
class TestApi(unittest.TestCase):
    def setUp(self):
        self.assertIsNotNone(BASE_URL, "URL no configurada")
        self.assertTrue(len(BASE_URL) > 8, "URL no configurada")

    def test_api_add(self):
        url = f"{BASE_URL}/calc/add/2/2"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(
            response.status, http.client.OK, f"Error en la petición API a {url}"
        )

# nuevo

    def test_api_substract(self):
        url = f"{BASE_URL}/calc/substract/5/3"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(response.status, http.client.OK)

    def test_api_multiply(self):
        url = f"{BASE_URL}/calc/multiply/3/4"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(response.status, http.client.OK)

    def test_api_divide_success(self):
        url = f"{BASE_URL}/calc/divide/10/2"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(response.status, http.client.OK)

    def test_api_divide_by_zero(self):
        with self.assertRaises(Exception):
            urlopen(f"{BASE_URL}/calc/divide/10/0", timeout=DEFAULT_TIMEOUT)

    def test_api_power(self):
        url = f"{BASE_URL}/calc/power/2/3"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(response.status, http.client.OK)

    def test_api_sqrt_success(self):
        url = f"{BASE_URL}/calc/sqrt/16"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(response.status, http.client.OK)

    def test_api_sqrt_negative(self):
        with self.assertRaises(Exception):
            urlopen(f"{BASE_URL}/calc/sqrt/-1", timeout=DEFAULT_TIMEOUT)

    def test_api_log10_success(self):
        url = f"{BASE_URL}/calc/log10/1000"
        response = urlopen(url, timeout=DEFAULT_TIMEOUT)
        self.assertEqual(response.status, http.client.OK)

    def test_api_log10_invalid(self):
        for val in [0, -10]:
            with self.assertRaises(Exception):
                urlopen(f"{BASE_URL}/calc/log10/{val}", timeout=DEFAULT_TIMEOUT)

    def test_api_invalid_type(self):
        with self.assertRaises(Exception):
            urlopen(f"{BASE_URL}/calc/add/abc/3", timeout=DEFAULT_TIMEOUT)
