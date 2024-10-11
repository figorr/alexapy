=============================
``alexapy.aiohttp.multipart``
=============================

.. automodule:: alexapy.aiohttp.multipart

   .. contents::
      :local:

.. currentmodule:: alexapy.aiohttp.multipart


Functions
=========

- :py:func:`parse_content_disposition`:
  Undocumented.

- :py:func:`content_disposition_filename`:
  Undocumented.


.. autofunction:: parse_content_disposition

.. autofunction:: content_disposition_filename


Classes
=======

- :py:class:`MultipartReader`:
  Multipart body reader.

- :py:class:`MultipartWriter`:
  Multipart body writer.

- :py:class:`BodyPartReader`:
  Multipart reader for single body part.


.. autoclass:: MultipartReader
   :members:

   .. rubric:: Inheritance
   .. inheritance-diagram:: MultipartReader
      :parts: 1

.. autoclass:: MultipartWriter
   :members:

   .. rubric:: Inheritance
   .. inheritance-diagram:: MultipartWriter
      :parts: 1

.. autoclass:: BodyPartReader
   :members:

   .. rubric:: Inheritance
   .. inheritance-diagram:: BodyPartReader
      :parts: 1


Exceptions
==========

- :py:exc:`BadContentDispositionHeader`:
  Base class for warnings about dubious runtime behavior.

- :py:exc:`BadContentDispositionParam`:
  Base class for warnings about dubious runtime behavior.


.. autoexception:: BadContentDispositionHeader

   .. rubric:: Inheritance
   .. inheritance-diagram:: BadContentDispositionHeader
      :parts: 1

.. autoexception:: BadContentDispositionParam

   .. rubric:: Inheritance
   .. inheritance-diagram:: BadContentDispositionParam
      :parts: 1
