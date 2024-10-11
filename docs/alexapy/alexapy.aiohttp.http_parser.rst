===============================
``alexapy.aiohttp.http_parser``
===============================

.. automodule:: alexapy.aiohttp.http_parser

   .. contents::
      :local:

.. currentmodule:: alexapy.aiohttp.http_parser


Classes
=======

- :py:class:`HeadersParser`:
  Undocumented.

- :py:class:`HttpParser`:
  Helper class that provides a standard way to create an ABC using

- :py:class:`HttpRequestParser`:
  Read request status line. Exception .http_exceptions.BadStatusLine

- :py:class:`HttpResponseParser`:
  Read response status line and headers.

- :py:class:`RawRequestMessage`:
  RawRequestMessage(method, path, version, headers, raw_headers, should_close, compression, upgrade, chunked, url)

- :py:class:`RawResponseMessage`:
  RawResponseMessage(version, code, reason, headers, raw_headers, should_close, compression, upgrade, chunked)


.. autoclass:: HeadersParser
   :members:

   .. rubric:: Inheritance
   .. inheritance-diagram:: HeadersParser
      :parts: 1

.. autoclass:: HttpParser
   :members:

   .. rubric:: Inheritance
   .. inheritance-diagram:: HttpParser
      :parts: 1

.. autoclass:: HttpRequestParser
   :members:

   .. rubric:: Inheritance
   .. inheritance-diagram:: HttpRequestParser
      :parts: 1

.. autoclass:: HttpResponseParser
   :members:

   .. rubric:: Inheritance
   .. inheritance-diagram:: HttpResponseParser
      :parts: 1

.. autoclass:: RawRequestMessage
   :members:

   .. rubric:: Inheritance
   .. inheritance-diagram:: RawRequestMessage
      :parts: 1

.. autoclass:: RawResponseMessage
   :members:

   .. rubric:: Inheritance
   .. inheritance-diagram:: RawResponseMessage
      :parts: 1
