# Copyright (c) OpenMMLab. All rights reserved.
import copy
from importlib import import_module
from unittest import TestCase

import addict

from mmcfg import LazyObject


class TestLazyObject(TestCase):

    def test_init(self):
        LazyObject('addict')
        LazyObject('addict.addict')
        LazyObject('Dict', 'addict.addict')

    def test_build(self):
        lazy_addict = LazyObject('addict')
        self.assertIs(lazy_addict.build(), addict)

        lazy_addict_module = LazyObject('addict.addict')
        self.assertIs(lazy_addict_module.build(),
                      import_module('addict.addict'))

        lazy_Dict = LazyObject('Dict', LazyObject('addict.addict'))
        self.assertIs(lazy_Dict.build(), addict.Addict)

        copied = copy.deepcopy(lazy_Dict)
        self.assertDictEqual(copied.__dict__, lazy_Dict.__dict__)

        with self.assertRaises(TypeError):
            lazy_addict()

        with self.assertRaises(ImportError):
            LazyObject('unknown').build()

        lazy_addict = LazyObject('addict')
        local_Dict = lazy_addict.Dict
        self.assertIs(local_Dict.build(), addict.Dict)

        copied = copy.deepcopy(local_Dict)
        self.assertDictEqual(copied.__dict__, local_Dict.__dict__)

        with self.assertRaises(TypeError):
            local_Dict()

        with self.assertRaisesRegex(ImportError, 'Failed to import'):
            local_Dict.unknown.build()
