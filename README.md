# Keygen Python Software Development Kit

A Python library to interact with the [Kyegen](https://keygen.sh) API and handle
licensing, user authentication, and machine activation.

This library is a work-in-progress and does not aim to cover the entirety of
Keygen’s API, especially the Enterprise features.

This library plays well with projects already relying on Pydantic, as all objects
are Pydantic models, but it uses _synchronous_ API calls. For an async-capable
Keygen client, see [keygen-py](https://pypi.org/project/keygen-py/), which is a
wrapper around [keygen-rs](https://github.com/ahonn/keygen-rs).

**Disclaimer**: this library is not officially endorsed nor supported by
[Keygen LLC](https://keygen.sh).

## Installation

You can install the package as any Python distribution via

```shell
pip install keygen-python-sdk
```

Alternatively, use your project management tool’s command, e.g. with `uv`:

```shell
uv add keygen-python-sdk
```

## Configuration

Configuration is entirely done via environment variables. Any attribute
from the `keygen_python_sdk.config.Config` class can be set in this way. You
will need to set an environment variable starting with `KEYGEN_` and
then append the all-caps version of the attribute you want to set. For
example, to set the `Config.auth_token` attribute:

```dotenv
KEYGEN_ATUH_TOKEN="prod-asdnfKSDAABSDh2q9Dsv3
```

See the [docs](https://keygen-python-sdk.readthedocs.io/en/latest/index.html)
for more details.

## Quickstart

Given a license key `SOME-LICENSE-V3`, you can obtain a license object
with:

```python
import keygen_python_sdk as kg

lic = kg.validate_key("SOME-LICENSE-V3")
```

## Development

To work on `keygen-python-sdk` you need

- Python >= 3.10;
- [uv](https://docs.astral.sh/uv/) for project management;
- [just](https://github.com/casey/just) for running common commands.

```shell
uv sync
just docs test package
```
