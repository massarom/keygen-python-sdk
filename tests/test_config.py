# SPDX-FileCopyrightText: 2024, Marcello Massaro
#
# SPDX-License-Identified: Apache-2.0
from keygen_python_sdk.config import config


class TestConfig:
    def test_headers_conversion(self):
        """Test that keyword arguments are correctly translated into headers."""
        hdr = config.request_headers(some_header="asd")
        assert "Some-Header" in hdr
        assert config.request_headers(some_header="asd")["Some-Header"] == "asd"
