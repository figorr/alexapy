===========================
``alexapy.aiohttp.tracing``
===========================

.. automodule:: alexapy.aiohttp.tracing

   .. contents::
      :local:

.. currentmodule:: alexapy.aiohttp.tracing


Classes
=======

- :py:class:`TraceConfig`:
  First-class used to trace requests launched via ClientSession

- :py:class:`TraceRequestStartParams`:
  Parameters sent by the `on_request_start` signal

- :py:class:`TraceRequestEndParams`:
  Parameters sent by the `on_request_end` signal

- :py:class:`TraceRequestExceptionParams`:
  Parameters sent by the `on_request_exception` signal

- :py:class:`TraceConnectionQueuedStartParams`:
  Parameters sent by the `on_connection_queued_start` signal

- :py:class:`TraceConnectionQueuedEndParams`:
  Parameters sent by the `on_connection_queued_end` signal

- :py:class:`TraceConnectionCreateStartParams`:
  Parameters sent by the `on_connection_create_start` signal

- :py:class:`TraceConnectionCreateEndParams`:
  Parameters sent by the `on_connection_create_end` signal

- :py:class:`TraceConnectionReuseconnParams`:
  Parameters sent by the `on_connection_reuseconn` signal

- :py:class:`TraceDnsResolveHostStartParams`:
  Parameters sent by the `on_dns_resolvehost_start` signal

- :py:class:`TraceDnsResolveHostEndParams`:
  Parameters sent by the `on_dns_resolvehost_end` signal

- :py:class:`TraceDnsCacheHitParams`:
  Parameters sent by the `on_dns_cache_hit` signal

- :py:class:`TraceDnsCacheMissParams`:
  Parameters sent by the `on_dns_cache_miss` signal

- :py:class:`TraceRequestRedirectParams`:
  Parameters sent by the `on_request_redirect` signal

- :py:class:`TraceRequestChunkSentParams`:
  Parameters sent by the `on_request_chunk_sent` signal

- :py:class:`TraceResponseChunkReceivedParams`:
  Parameters sent by the `on_response_chunk_received` signal


.. autoclass:: TraceConfig
   :members:

   .. rubric:: Inheritance
   .. inheritance-diagram:: TraceConfig
      :parts: 1

.. autoclass:: TraceRequestStartParams
   :members:

   .. rubric:: Inheritance
   .. inheritance-diagram:: TraceRequestStartParams
      :parts: 1

.. autoclass:: TraceRequestEndParams
   :members:

   .. rubric:: Inheritance
   .. inheritance-diagram:: TraceRequestEndParams
      :parts: 1

.. autoclass:: TraceRequestExceptionParams
   :members:

   .. rubric:: Inheritance
   .. inheritance-diagram:: TraceRequestExceptionParams
      :parts: 1

.. autoclass:: TraceConnectionQueuedStartParams
   :members:

   .. rubric:: Inheritance
   .. inheritance-diagram:: TraceConnectionQueuedStartParams
      :parts: 1

.. autoclass:: TraceConnectionQueuedEndParams
   :members:

   .. rubric:: Inheritance
   .. inheritance-diagram:: TraceConnectionQueuedEndParams
      :parts: 1

.. autoclass:: TraceConnectionCreateStartParams
   :members:

   .. rubric:: Inheritance
   .. inheritance-diagram:: TraceConnectionCreateStartParams
      :parts: 1

.. autoclass:: TraceConnectionCreateEndParams
   :members:

   .. rubric:: Inheritance
   .. inheritance-diagram:: TraceConnectionCreateEndParams
      :parts: 1

.. autoclass:: TraceConnectionReuseconnParams
   :members:

   .. rubric:: Inheritance
   .. inheritance-diagram:: TraceConnectionReuseconnParams
      :parts: 1

.. autoclass:: TraceDnsResolveHostStartParams
   :members:

   .. rubric:: Inheritance
   .. inheritance-diagram:: TraceDnsResolveHostStartParams
      :parts: 1

.. autoclass:: TraceDnsResolveHostEndParams
   :members:

   .. rubric:: Inheritance
   .. inheritance-diagram:: TraceDnsResolveHostEndParams
      :parts: 1

.. autoclass:: TraceDnsCacheHitParams
   :members:

   .. rubric:: Inheritance
   .. inheritance-diagram:: TraceDnsCacheHitParams
      :parts: 1

.. autoclass:: TraceDnsCacheMissParams
   :members:

   .. rubric:: Inheritance
   .. inheritance-diagram:: TraceDnsCacheMissParams
      :parts: 1

.. autoclass:: TraceRequestRedirectParams
   :members:

   .. rubric:: Inheritance
   .. inheritance-diagram:: TraceRequestRedirectParams
      :parts: 1

.. autoclass:: TraceRequestChunkSentParams
   :members:

   .. rubric:: Inheritance
   .. inheritance-diagram:: TraceRequestChunkSentParams
      :parts: 1

.. autoclass:: TraceResponseChunkReceivedParams
   :members:

   .. rubric:: Inheritance
   .. inheritance-diagram:: TraceResponseChunkReceivedParams
      :parts: 1
