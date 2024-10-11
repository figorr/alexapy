========================
``alexapy.aiohttp.http``
========================

.. automodule:: alexapy.aiohttp.http

   .. contents::
      :local:

.. currentmodule:: alexapy.aiohttp.http


Functions
=========

- :py:func:`ws_ext_gen`:
  Undocumented.

- :py:func:`ws_ext_parse`:
  Undocumented.


.. autofunction:: ws_ext_gen

.. autofunction:: ws_ext_parse


Classes
=======

- :py:class:`StreamWriter`:
  Abstract stream writer.

- :py:class:`HttpVersion`:
  HttpVersion(major, minor)

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

- :py:class:`WebSocketReader`:
  Undocumented.

- :py:class:`WebSocketWriter`:
  Undocumented.

- :py:class:`WSMessage`:
  _WSMessageBase(type, data, extra)

- :py:class:`WSMsgType`:
  An enumeration.

- :py:class:`WSCloseCode`:
  An enumeration.


.. autoclass:: StreamWriter
   :members:

   .. rubric:: Inheritance
   .. inheritance-diagram:: StreamWriter
      :parts: 1

.. autoclass:: HttpVersion
   :members:

   .. rubric:: Inheritance
   .. inheritance-diagram:: HttpVersion
      :parts: 1

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

.. autoclass:: WebSocketReader
   :members:

   .. rubric:: Inheritance
   .. inheritance-diagram:: WebSocketReader
      :parts: 1

.. autoclass:: WebSocketWriter
   :members:

   .. rubric:: Inheritance
   .. inheritance-diagram:: WebSocketWriter
      :parts: 1

.. autoclass:: WSMessage
   :members:

   .. rubric:: Inheritance
   .. inheritance-diagram:: WSMessage
      :parts: 1

.. autoclass:: WSMsgType
   :members:

   .. rubric:: Inheritance
   .. inheritance-diagram:: WSMsgType
      :parts: 1

.. autoclass:: WSCloseCode
   :members:

   .. rubric:: Inheritance
   .. inheritance-diagram:: WSCloseCode
      :parts: 1


Exceptions
==========

- :py:exc:`HttpProcessingError`:
  HTTP error.

- :py:exc:`WebSocketError`:
  WebSocket protocol parser error.


.. autoexception:: HttpProcessingError

   .. rubric:: Inheritance
   .. inheritance-diagram:: HttpProcessingError
      :parts: 1

.. autoexception:: WebSocketError

   .. rubric:: Inheritance
   .. inheritance-diagram:: WebSocketError
      :parts: 1


Variables
=========

- :py:data:`RESPONSES`
- :py:data:`SERVER_SOFTWARE`
- :py:data:`HttpVersion10`
- :py:data:`HttpVersion11`
- :py:data:`WS_CLOSED_MESSAGE`
- :py:data:`WS_CLOSING_MESSAGE`
- :py:data:`WS_KEY`

.. autodata:: RESPONSES
   :annotation:

   .. code-block:: text

      {<HTTPStatus.CONTINUE: 100>: ('Continue', 'Request received, please continue'),
       <HTTPStatus.SWITCHING_PROTOCOLS: 101>: ('Switching Protocols',
                                               'Switching to new protocol; obey '
                                               'Upgrade header'),
       <HTTPStatus.PROCESSING: 102>: ('Processing', ''),
       <HTTPStatus.OK: 200>: ('OK', 'Request fulfilled, document follows'),
       <HTTPStatus.CREATED: 201>: ('Created', 'Document created, URL follows'),
       <HTTPStatus.ACCEPTED: 202>: ('Accepted',
                                    'Request accepted, processing continues '
                                    'off-line'),
       <HTTPStatus.NON_AUTHORITATIVE_INFORMATION: 203>: ('Non-Authoritative '
                                                         'Information',
                                                         'Request fulfilled from '
                                                         'cache'),
       <HTTPStatus.NO_CONTENT: 204>: ('No Content',
                                      'Request fulfilled, nothing follows'),
       <HTTPStatus.RESET_CONTENT: 205>: ('Reset Content',
                                         'Clear input form for further input'),
       <HTTPStatus.PARTIAL_CONTENT: 206>: ('Partial Content',
                                           'Partial content follows'),
       <HTTPStatus.MULTI_STATUS: 207>: ('Multi-Status', ''),
       <HTTPStatus.ALREADY_REPORTED: 208>: ('Already Reported', ''),
       <HTTPStatus.IM_USED: 226>: ('IM Used', ''),
       <HTTPStatus.MULTIPLE_CHOICES: 300>: ('Multiple Choices',
                                            'Object has several resources -- see URI '
                                            'list'),
       <HTTPStatus.MOVED_PERMANENTLY: 301>: ('Moved Permanently',
                                             'Object moved permanently -- see URI '
                                             'list'),
       <HTTPStatus.FOUND: 302>: ('Found', 'Object moved temporarily -- see URI list'),
       <HTTPStatus.SEE_OTHER: 303>: ('See Other',
                                     'Object moved -- see Method and URL list'),
       <HTTPStatus.NOT_MODIFIED: 304>: ('Not Modified',
                                        'Document has not changed since given time'),
       <HTTPStatus.USE_PROXY: 305>: ('Use Proxy',
                                     'You must use proxy specified in Location to '
                                     'access this resource'),
       <HTTPStatus.TEMPORARY_REDIRECT: 307>: ('Temporary Redirect',
                                              'Object moved temporarily -- see URI '
                                              'list'),
       <HTTPStatus.PERMANENT_REDIRECT: 308>: ('Permanent Redirect',
                                              'Object moved permanently -- see URI '
                                              'list'),
       <HTTPStatus.BAD_REQUEST: 400>: ('Bad Request',
                                       'Bad request syntax or unsupported method'),
       <HTTPStatus.UNAUTHORIZED: 401>: ('Unauthorized',
                                        'No permission -- see authorization schemes'),
       <HTTPStatus.PAYMENT_REQUIRED: 402>: ('Payment Required',
                                            'No payment -- see charging schemes'),
       <HTTPStatus.FORBIDDEN: 403>: ('Forbidden',
                                     'Request forbidden -- authorization will not '
                                     'help'),
       <HTTPStatus.NOT_FOUND: 404>: ('Not Found', 'Nothing matches the given URI'),
       <HTTPStatus.METHOD_NOT_ALLOWED: 405>: ('Method Not Allowed',
                                              'Specified method is invalid for this '
                                              'resource'),
       <HTTPStatus.NOT_ACCEPTABLE: 406>: ('Not Acceptable',
                                          'URI not available in preferred format'),
       <HTTPStatus.PROXY_AUTHENTICATION_REQUIRED: 407>: ('Proxy Authentication '
                                                         'Required',
                                                         'You must authenticate with '
                                                         'this proxy before '
                                                         'proceeding'),
       <HTTPStatus.REQUEST_TIMEOUT: 408>: ('Request Timeout',
                                           'Request timed out; try again later'),
       <HTTPStatus.CONFLICT: 409>: ('Conflict', 'Request conflict'),
       <HTTPStatus.GONE: 410>: ('Gone',
                                'URI no longer exists and has been permanently '
                                'removed'),
       <HTTPStatus.LENGTH_REQUIRED: 411>: ('Length Required',
                                           'Client must specify Content-Length'),
       <HTTPStatus.PRECONDITION_FAILED: 412>: ('Precondition Failed',
                                               'Precondition in headers is false'),
       <HTTPStatus.REQUEST_ENTITY_TOO_LARGE: 413>: ('Request Entity Too Large',
                                                    'Entity is too large'),
       <HTTPStatus.REQUEST_URI_TOO_LONG: 414>: ('Request-URI Too Long',
                                                'URI is too long'),
       <HTTPStatus.UNSUPPORTED_MEDIA_TYPE: 415>: ('Unsupported Media Type',
                                                  'Entity body in unsupported '
                                                  'format'),
       <HTTPStatus.REQUESTED_RANGE_NOT_SATISFIABLE: 416>: ('Requested Range Not '
                                                           'Satisfiable',
                                                           'Cannot satisfy request '
                                                           'range'),
       <HTTPStatus.EXPECTATION_FAILED: 417>: ('Expectation Failed',
                                              'Expect condition could not be '
                                              'satisfied'),
       <HTTPStatus.MISDIRECTED_REQUEST: 421>: ('Misdirected Request',
                                               'Server is not able to produce a '
                                               'response'),
       <HTTPStatus.UNPROCESSABLE_ENTITY: 422>: ('Unprocessable Entity', ''),
       <HTTPStatus.LOCKED: 423>: ('Locked', ''),
       <HTTPStatus.FAILED_DEPENDENCY: 424>: ('Failed Dependency', ''),
       <HTTPStatus.UPGRADE_REQUIRED: 426>: ('Upgrade Required', ''),
       <HTTPStatus.PRECONDITION_REQUIRED: 428>: ('Precondition Required',
                                                 'The origin server requires the '
                                                 'request to be conditional'),
       <HTTPStatus.TOO_MANY_REQUESTS: 429>: ('Too Many Requests',
                                             'The user has sent too many requests in '
                                             'a given amount of time ("rate '
                                             'limiting")'),
       <HTTPStatus.REQUEST_HEADER_FIELDS_TOO_LARGE: 431>: ('Request Header Fields '
                                                           'Too Large',
                                                           'The server is unwilling '
                                                           'to process the request '
                                                           'because its header '
                                                           'fields are too large'),
       <HTTPStatus.UNAVAILABLE_FOR_LEGAL_REASONS: 451>: ('Unavailable For Legal '
                                                         'Reasons',
                                                         'The server is denying '
                                                         'access to the resource as '
                                                         'a consequence of a legal '
                                                         'demand'),
       <HTTPStatus.INTERNAL_SERVER_ERROR: 500>: ('Internal Server Error',
                                                 'Server got itself in trouble'),
       <HTTPStatus.NOT_IMPLEMENTED: 501>: ('Not Implemented',
                                           'Server does not support this operation'),
       <HTTPStatus.BAD_GATEWAY: 502>: ('Bad Gateway',
                                       'Invalid responses from another server/proxy'),
       <HTTPStatus.SERVICE_UNAVAILABLE: 503>: ('Service Unavailable',
                                               'The server cannot process the '
                                               'request due to a high load'),
       <HTTPStatus.GATEWAY_TIMEOUT: 504>: ('Gateway Timeout',
                                           'The gateway server did not receive a '
                                           'timely response'),
       <HTTPStatus.HTTP_VERSION_NOT_SUPPORTED: 505>: ('HTTP Version Not Supported',
                                                      'Cannot fulfill request'),
       <HTTPStatus.VARIANT_ALSO_NEGOTIATES: 506>: ('Variant Also Negotiates', ''),
       <HTTPStatus.INSUFFICIENT_STORAGE: 507>: ('Insufficient Storage', ''),
       <HTTPStatus.LOOP_DETECTED: 508>: ('Loop Detected', ''),
       <HTTPStatus.NOT_EXTENDED: 510>: ('Not Extended', ''),
       <HTTPStatus.NETWORK_AUTHENTICATION_REQUIRED: 511>: ('Network Authentication '
                                                           'Required',
                                                           'The client needs to '
                                                           'authenticate to gain '
                                                           'network access')}

.. autodata:: SERVER_SOFTWARE
   :annotation:

   .. code-block:: text

      'Python/3.8 aiohttp/3.6.2'

.. autodata:: HttpVersion10
   :annotation:

   .. code-block:: text

      HttpVersion(major=1, minor=0)

.. autodata:: HttpVersion11
   :annotation:

   .. code-block:: text

      HttpVersion(major=1, minor=1)

.. autodata:: WS_CLOSED_MESSAGE
   :annotation:

   .. code-block:: text

      WSMessage(type=<WSMsgType.CLOSED: 257>, data=None, extra=None)

.. autodata:: WS_CLOSING_MESSAGE
   :annotation:

   .. code-block:: text

      WSMessage(type=<WSMsgType.CLOSING: 256>, data=None, extra=None)

.. autodata:: WS_KEY
   :annotation:

   .. code-block:: text

      b'258EAFA5-E914-47DA-95CA-C5AB0DC85B11'
