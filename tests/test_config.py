# Copyright (c) OpenMMLab. All rights reserved.
import os
import os.path as osp
from pathlib import Path

from addict import Dict

from mmcfg import Config


class TestConfig:
    data_path = Path(__file__).parent / 'data'

    def test_python(self):
        # Python format
        cfg_file = osp.join(self.data_path, 'py_config/config.py')
        cfg = Config.fromfile(cfg_file)
        assert isinstance(cfg, Config)
        assert cfg.item1 == [1, 2]
        assert cfg.item2 == {'a': 1}
        assert cfg.item3 is True
        assert cfg.item4 == 'test'
        assert cfg.item5 == {1, 2, 3}
        assert cfg.item6 == (dict(a=0), dict(b=1))
        assert cfg.item7['a'] == [0, 1, 2]
        assert cfg.item7['b']['c'] == [3.1, 4.2, 5.3]
        assert cfg.item8 == os.getenv('HOME')
        assert cfg.item9 == list(a + 1 for a in range(5))
        assert cfg.item10 == Dict
        assert cfg.item11 == [1, 2, 3]
