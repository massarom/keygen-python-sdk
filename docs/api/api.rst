*************
SDK reference
*************

.. note::

   We use *SDK* to refer to this package's functions, classes, and data, while we use
   *API* to refer to the Keygen's own REST endpoints, methods, and objects.

.. toctree::
   :maxdepth: 1

   Configuration <configuration>
   Functions <functional>
   Models <models/models>
   Exceptions <exceptions>

The SDK follows in spirit an ORM style like SQLAlchemy. The starting point is always
the :func:`.validate_key` function, since this is the most common
use-case currently supported by the SDK.

The function will return a valid :class:`.License`, from which you can start exploring
the rest of your data through its attributes. For example, looking for a licence's
:attr:`.License.owner` will return a :class:`.User` object with all available data
filled-in as its own attributes.

.. important::

   Remember that all API calls are scoped to the currently used API token. A license
   key for example has less permissions than a user :class:`.Token`.

Of course you will not always start from a simple license key if you're working
server-side. By setting a token with appropriate permissions in the ``KEYGEN_API_TOKEN``
environment variable, you'll be able to use all other functions from the
:mod:`.functional` module. These will allow you to work on most API objects with CRUD
operations.
