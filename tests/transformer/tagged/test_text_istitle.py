# -*- coding: utf-8 -*-
from unittest import TestCase

from underthesea_flow.transformer.tagged_feature import text_istitle

sentence_1 = [(u"Chào", "V"), (u"em", "N"), (u"cô gái", "N"), (u"Lam Hồng", "N")]


class TestTextIsTitle(TestCase):
    def test_true(self):
        words = [
            "Hải",
            "Đặng",
            "Hải Dương",
            "This Is String Example"
        ]
        for word in words:
            self.assertTrue(text_istitle(word))

    def test_false(self):
        words = [
            "",
            "hải",
            u"hải",
            "%",
            "Hải dương",
            "This is string example..."
        ]
        for word in words:
            self.assertFalse(text_istitle(word))
