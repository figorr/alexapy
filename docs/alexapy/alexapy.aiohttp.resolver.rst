============================
``alexapy.aiohttp.resolver``
============================

.. automodule:: alexapy.aiohttp.resolver

   .. contents::
      :local:

.. currentmodule:: alexapy.aiohttp.resolver


Classes
=======

- :py:class:`ThreadedResolver`:
  Use Executor for synchronous getaddrinfo() calls, which defaults to

- :py:class:`AsyncResolver`:
  Use the `aiodns` package to make asynchronous DNS lookups

- :py:class:`DefaultResolver`:
  Use Executor for synchronous getaddrinfo() calls, which defaults to


.. autoclass:: ThreadedResolver
   :members:

   .. rubric:: Inheritance
   .. inheritance-diagram:: ThreadedResolver
      :parts: 1

.. autoclass:: AsyncResolver
   :members:

   .. rubric:: Inheritance
   .. inheritance-diagram:: AsyncResolver
      :parts: 1

.. autoclass:: DefaultResolver
   :members:

   .. rubric:: Inheritance
   .. inheritance-diagram:: DefaultResolver
      :parts: 1
