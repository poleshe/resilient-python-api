#!/usr/bin/env python
# -*- coding: utf-8 -*-
# (c) Copyright IBM Corp. 2010, 2020. All Rights Reserved.

import copy
import sys
import pytest
from resilient_circuits.app import AppArgumentParser
from resilient_circuits.validate_configs import MAX_NUM_WORKERS
from tests.shared_mock_data import mock_paths


def test_num_workers(fx_clear_cmd_line_args):

    # Test reading from app.config
    opts = AppArgumentParser(config_file=mock_paths.MOCK_APP_CONFIG).parse_args()
    assert isinstance(opts.get("num_workers"), int)
    assert opts.get("num_workers") == 50

    # Test default value - commented out in app.config
    opts = AppArgumentParser(config_file=mock_paths.MOCK_COMMENTED_APP_CONFIG).parse_args()
    assert isinstance(opts.get("num_workers"), int)
    assert opts.get("num_workers") == 25

    # Test overwriting
    sys.argv.extend(["--num-workers", "30"])
    opts = AppArgumentParser(config_file=mock_paths.MOCK_APP_CONFIG).parse_args()
    assert isinstance(opts.get("num_workers"), int)
    assert opts.get("num_workers") == 30

    # Test if over limit
    sys.argv.extend(["--num-workers", str(MAX_NUM_WORKERS+1)])
    with pytest.raises(ValueError, match=r"num_workers must be in the range .*"):
        AppArgumentParser(config_file=mock_paths.MOCK_APP_CONFIG).parse_args()


def test_global_integrations_options(fx_clear_cmd_line_args):
    opts = AppArgumentParser(config_file=mock_paths.MOCK_APP_CONFIG).parse_args().get("integrations", {})
    assert opts.get("http_proxy") == "http://example.com:3000"
    assert opts.get("https_proxy") == "https://example.com:3000"
    assert opts.get("timeout") == "50"


def test_global_integrations_options_commented_out(fx_clear_cmd_line_args):
    opts = AppArgumentParser(config_file=mock_paths.MOCK_COMMENTED_APP_CONFIG).parse_args().get("integrations", {})
    assert opts.get("http_proxy") is None
    assert opts.get("https_proxy") is None
    assert opts.get("timeout") is None
