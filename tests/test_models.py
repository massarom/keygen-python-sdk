# SPDX-FileCopyrightText: 2024, Marcello Massaro
#
# SPDX-License-Identified: Apache-2.0
import pytest

from keygen_python_sdk import models, exceptions as exc


@pytest.mark.parametrize("cls", (models.License, models.User, models.Token))
def test_models_response_parsing_failure(
    cls: type[models.License] | type[models.User] | type[models.Token],
):
    with pytest.raises(exc.KeygenError, match="no 'type' field in 'data' object"):
        cls.from_response({"data": {"id": "test"}})
    with pytest.raises(
        exc.KeygenError, match=f"'some' type cannot be parsed as {cls.__name__}"
    ):
        cls.from_response({"data": {"type": "some"}})
    with pytest.raises(exc.KeygenError, match="'data'.+not a mapping:"):
        cls.from_response({"data": "wow"})
