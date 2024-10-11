==================================
``alexapy.aiohttp.http_websocket``
==================================

.. automodule:: alexapy.aiohttp.http_websocket

   .. contents::
      :local:

.. currentmodule:: alexapy.aiohttp.http_websocket


Classes
=======

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

- :py:exc:`WebSocketError`:
  WebSocket protocol parser error.


.. autoexception:: WebSocketError

   .. rubric:: Inheritance
   .. inheritance-diagram:: WebSocketError
      :parts: 1


Variables
=========

- :py:data:`WS_CLOSED_MESSAGE`
- :py:data:`WS_CLOSING_MESSAGE`
- :py:data:`WS_KEY`

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
