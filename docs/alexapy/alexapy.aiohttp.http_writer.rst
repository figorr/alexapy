===============================
``alexapy.aiohttp.http_writer``
===============================

.. automodule:: alexapy.aiohttp.http_writer

   .. contents::
      :local:

.. currentmodule:: alexapy.aiohttp.http_writer


Classes
=======

- :py:class:`StreamWriter`:
  Abstract stream writer.

- :py:class:`HttpVersion`:
  HttpVersion(major, minor)


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


Variables
=========

- :py:data:`HttpVersion10`
- :py:data:`HttpVersion11`

.. autodata:: HttpVersion10
   :annotation:

   .. code-block:: text

      HttpVersion(major=1, minor=0)

.. autodata:: HttpVersion11
   :annotation:

   .. code-block:: text

      HttpVersion(major=1, minor=1)
