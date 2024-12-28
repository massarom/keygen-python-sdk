Models
******

.. currentmodule:: keygen_python_sdk.models

.. toctree::
   :hidden:
   :maxdepth: 1

   Licenses <licenses>
   Tokens <tokens>
   Users <users>

All models inherit from :class:`CamelCasedModel`, which is a Pydantic model whose
initialisation can be done using ``camelCased`` arguments instead of ``snake_cased``.
This is to facilitate direct conversion of the Keygen's API JSON objects.

.. autoclass:: CamelCasedModel

.. autoclass:: JSONAPIRelationshipObject
