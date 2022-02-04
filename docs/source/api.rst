API
===

.. note::
   Undergoing Maintenance pending release v2.0.0 of Basestack

Development Setup of Server and App
-----

.. code-block:: console

   conda activate basestack
   npm run dev:server
   npm run dev:app (if running the app in parallel)


Pinging the Server
----

.. note::
   You can use Postman as your API management toolkit for testing the server

``curl localhost:5003/server/ping``

returns

.. code-block:: console

   {"status":200,"message":"Server is running at port: 5003"}

.. toctree::
    :maxdepth: 2
    :caption: API Reference

    api_modules
    api_procedures
    api_service
    api_cache
    api_stats