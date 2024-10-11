===========================
``alexapy.aiohttp.streams``
===========================

.. automodule:: alexapy.aiohttp.streams

   .. contents::
      :local:

.. currentmodule:: alexapy.aiohttp.streams


Classes
=======

- :py:class:`StreamReader`:
  An enhancement of asyncio.StreamReader.

- :py:class:`DataQueue`:
  DataQueue is a general-purpose blocking queue with one reader.

- :py:class:`FlowControlDataQueue`:
  FlowControlDataQueue resumes and pauses an underlying stream.


.. autoclass:: StreamReader
   :members:

   .. rubric:: Inheritance
   .. inheritance-diagram:: StreamReader
      :parts: 1

.. autoclass:: DataQueue
   :members:

   .. rubric:: Inheritance
   .. inheritance-diagram:: DataQueue
      :parts: 1

.. autoclass:: FlowControlDataQueue
   :members:

   .. rubric:: Inheritance
   .. inheritance-diagram:: FlowControlDataQueue
      :parts: 1


Exceptions
==========

- :py:exc:`EofStream`:
  eof stream indication.


.. autoexception:: EofStream

   .. rubric:: Inheritance
   .. inheritance-diagram:: EofStream
      :parts: 1


Variables
=========

- :py:data:`EMPTY_PAYLOAD`

.. autodata:: EMPTY_PAYLOAD
   :annotation:

   .. code-block:: text

      <alexapy.aiohttp.streams.EmptyStreamReader object at 0x10e2626d0>
