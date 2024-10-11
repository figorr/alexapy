==========================
``alexapy.aiohttp.client``
==========================

.. automodule:: alexapy.aiohttp.client

   .. contents::
      :local:

.. currentmodule:: alexapy.aiohttp.client


Functions
=========

- :py:func:`request`:
  Constructs and sends a request. Returns response object.


.. autofunction:: request


Classes
=======

- :py:class:`ClientRequest`:
  Undocumented.

- :py:class:`ClientResponse`:
  Undocumented.

- :py:class:`Fingerprint`:
  Undocumented.

- :py:class:`RequestInfo`:
  Undocumented.

- :py:class:`BaseConnector`:
  Base connector class.

- :py:class:`TCPConnector`:
  TCP connector.

- :py:class:`UnixConnector`:
  Unix socket connector.

- :py:class:`NamedPipeConnector`:
  Named pipe connector.

- :py:class:`ClientWebSocketResponse`:
  Undocumented.

- :py:class:`ClientSession`:
  First-class interface for making HTTP requests.

- :py:class:`ClientTimeout`:
  Undocumented.


.. autoclass:: ClientRequest
   :members:

   .. rubric:: Inheritance
   .. inheritance-diagram:: ClientRequest
      :parts: 1

.. autoclass:: ClientResponse
   :members:

   .. rubric:: Inheritance
   .. inheritance-diagram:: ClientResponse
      :parts: 1

.. autoclass:: Fingerprint
   :members:

   .. rubric:: Inheritance
   .. inheritance-diagram:: Fingerprint
      :parts: 1

.. autoclass:: RequestInfo
   :members:

   .. rubric:: Inheritance
   .. inheritance-diagram:: RequestInfo
      :parts: 1

.. autoclass:: BaseConnector
   :members:

   .. rubric:: Inheritance
   .. inheritance-diagram:: BaseConnector
      :parts: 1

.. autoclass:: TCPConnector
   :members:

   .. rubric:: Inheritance
   .. inheritance-diagram:: TCPConnector
      :parts: 1

.. autoclass:: UnixConnector
   :members:

   .. rubric:: Inheritance
   .. inheritance-diagram:: UnixConnector
      :parts: 1

.. autoclass:: NamedPipeConnector
   :members:

   .. rubric:: Inheritance
   .. inheritance-diagram:: NamedPipeConnector
      :parts: 1

.. autoclass:: ClientWebSocketResponse
   :members:

   .. rubric:: Inheritance
   .. inheritance-diagram:: ClientWebSocketResponse
      :parts: 1

.. autoclass:: ClientSession
   :members:

   .. rubric:: Inheritance
   .. inheritance-diagram:: ClientSession
      :parts: 1

.. autoclass:: ClientTimeout
   :members:

   .. rubric:: Inheritance
   .. inheritance-diagram:: ClientTimeout
      :parts: 1


Exceptions
==========

- :py:exc:`ClientConnectionError`:
  Base class for client socket errors.

- :py:exc:`ClientConnectorCertificateError`:
  Response certificate error.

- :py:exc:`ClientConnectorError`:
  Client connector error.

- :py:exc:`ClientConnectorSSLError`:
  Response ssl error.

- :py:exc:`ClientError`:
  Base class for client connection errors.

- :py:exc:`ClientHttpProxyError`:
  HTTP proxy error.

- :py:exc:`ClientOSError`:
  OSError error.

- :py:exc:`ClientPayloadError`:
  Response payload error.

- :py:exc:`ClientProxyConnectionError`:
  Proxy connection error.

- :py:exc:`ClientResponseError`:
  Connection error during reading response.

- :py:exc:`ClientSSLError`:
  Base error for ssl.*Errors.

- :py:exc:`ContentTypeError`:
  ContentType found is not valid.

- :py:exc:`InvalidURL`:
  Invalid URL.

- :py:exc:`ServerConnectionError`:
  Server connection errors.

- :py:exc:`ServerDisconnectedError`:
  Server disconnected.

- :py:exc:`ServerFingerprintMismatch`:
  SSL certificate does not match expected fingerprint.

- :py:exc:`ServerTimeoutError`:
  Server timeout error.

- :py:exc:`TooManyRedirects`:
  Client was redirected too many times.

- :py:exc:`WSServerHandshakeError`:
  websocket server handshake error.


.. autoexception:: ClientConnectionError

   .. rubric:: Inheritance
   .. inheritance-diagram:: ClientConnectionError
      :parts: 1

.. autoexception:: ClientConnectorCertificateError

   .. rubric:: Inheritance
   .. inheritance-diagram:: ClientConnectorCertificateError
      :parts: 1

.. autoexception:: ClientConnectorError

   .. rubric:: Inheritance
   .. inheritance-diagram:: ClientConnectorError
      :parts: 1

.. autoexception:: ClientConnectorSSLError

   .. rubric:: Inheritance
   .. inheritance-diagram:: ClientConnectorSSLError
      :parts: 1

.. autoexception:: ClientError

   .. rubric:: Inheritance
   .. inheritance-diagram:: ClientError
      :parts: 1

.. autoexception:: ClientHttpProxyError

   .. rubric:: Inheritance
   .. inheritance-diagram:: ClientHttpProxyError
      :parts: 1

.. autoexception:: ClientOSError

   .. rubric:: Inheritance
   .. inheritance-diagram:: ClientOSError
      :parts: 1

.. autoexception:: ClientPayloadError

   .. rubric:: Inheritance
   .. inheritance-diagram:: ClientPayloadError
      :parts: 1

.. autoexception:: ClientProxyConnectionError

   .. rubric:: Inheritance
   .. inheritance-diagram:: ClientProxyConnectionError
      :parts: 1

.. autoexception:: ClientResponseError

   .. rubric:: Inheritance
   .. inheritance-diagram:: ClientResponseError
      :parts: 1

.. autoexception:: ClientSSLError

   .. rubric:: Inheritance
   .. inheritance-diagram:: ClientSSLError
      :parts: 1

.. autoexception:: ContentTypeError

   .. rubric:: Inheritance
   .. inheritance-diagram:: ContentTypeError
      :parts: 1

.. autoexception:: InvalidURL

   .. rubric:: Inheritance
   .. inheritance-diagram:: InvalidURL
      :parts: 1

.. autoexception:: ServerConnectionError

   .. rubric:: Inheritance
   .. inheritance-diagram:: ServerConnectionError
      :parts: 1

.. autoexception:: ServerDisconnectedError

   .. rubric:: Inheritance
   .. inheritance-diagram:: ServerDisconnectedError
      :parts: 1

.. autoexception:: ServerFingerprintMismatch

   .. rubric:: Inheritance
   .. inheritance-diagram:: ServerFingerprintMismatch
      :parts: 1

.. autoexception:: ServerTimeoutError

   .. rubric:: Inheritance
   .. inheritance-diagram:: ServerTimeoutError
      :parts: 1

.. autoexception:: TooManyRedirects

   .. rubric:: Inheritance
   .. inheritance-diagram:: TooManyRedirects
      :parts: 1

.. autoexception:: WSServerHandshakeError

   .. rubric:: Inheritance
   .. inheritance-diagram:: WSServerHandshakeError
      :parts: 1
