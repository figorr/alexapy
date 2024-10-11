================================
``alexapy.aiohttp.web_protocol``
================================

.. automodule:: alexapy.aiohttp.web_protocol

   .. contents::
      :local:

.. currentmodule:: alexapy.aiohttp.web_protocol


Classes
=======

- :py:class:`RequestHandler`:
  HTTP protocol implementation.


.. autoclass:: RequestHandler
   :members:

   .. rubric:: Inheritance
   .. inheritance-diagram:: RequestHandler
      :parts: 1


Exceptions
==========

- :py:exc:`RequestPayloadError`:
  Payload parsing error.

- :py:exc:`PayloadAccessError`:
  Payload was accessed after response was sent.


.. autoexception:: RequestPayloadError

   .. rubric:: Inheritance
   .. inheritance-diagram:: RequestPayloadError
      :parts: 1

.. autoexception:: PayloadAccessError

   .. rubric:: Inheritance
   .. inheritance-diagram:: PayloadAccessError
      :parts: 1
