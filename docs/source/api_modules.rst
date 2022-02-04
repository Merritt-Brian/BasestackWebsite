Modules
=====================

Basestack uses these calls for anything involving modules specifically in the app  ecosystem:

------------------------------------------------------------------------------

ping ``POST``
---------

.. note::
    To get the status of the server at the specified port,
    you can use the ``curl`` or `Postman <https://www.postman.com/>`_ to test your calls. 

.. code-block:: javascript

    curl localhost:5003/server/ping

------------------------------------------------------------------------------

getAllCatalog ``GET``
---------

.. code-block:: javascript

    curl localhost:5003/catalog/all/get


Gets all available catalogs, both remote and/or installed 

----------
Parameters
----------

-------
Returns
-------

``Array`` - List of all catalog entries available either remotely situated or locally available

-------
Example
-------

.. code-block:: javascript

    {
      "icon": "dna",
      "title": "Minimap2",
      "tags": [
        "minimap2",
        "alignment",
        "genomics"
      ],
      "status": {
        "installed": true,
        "latest": null,
        "building": true,
        "version": null,
        "running": false,
        "error": null
      },
      "name": "minimap2",
      "remotes": [],
      "modules": [
        {
          "status": {
            "fully_installed": true,
            "latest": null,
            "building": true,
            "version": null,
            "partial_install": true,
            "running": false,
            "error": null
          },
          "name": "minimap2",


------------------------------------------------------------------------------

getInstalledCatalog ``GET``
---------

.. code-block:: javascript

    curl localhost:5003/catalog/installed/get


Gets all installed catalogs, both remote and/or locally found in the app 

----------
Parameters
----------

-------
Returns
-------

``Array`` - List of installed catalog entries available either remotely situated or locally available

-------
Example
-------

.. code-block:: javascript

    {
      "icon": "dna",
      "title": "Minimap2",
      "tags": [
        "minimap2",
        "alignment",
        "genomics"
      ],
      "status": {
        "installed": true,
        "latest": null,
        "building": true,
        "version": null,
        "running": false,
        "error": null
      },
      "name": "minimap2",
      "remotes": [],
      "modules": [
        {
          "status": {
            "fully_installed": true,
            "latest": null,
            "building": true,
            "version": null,
            "partial_install": true,
            "running": false,
            "error": null
          },
          "name": "minimap2",


------------------------------------------------------------------------------



moduleBuildDependency ``POST``
---------

.. code-block:: javascript

    localhost:5003/module/build/dependency


Installs a single dependency belonging to a module's procedure (version)

----------
Parameters
----------

1. - ``dependency`` ``Int`` - Dependency index written for a procedure in the configuration of it
2. - ``catalog`` ``String`` - Catalog name
3. - ``module`` ``Int``  - Index of the module version for a catalog entry
4. - ``procedure`` ``Int`` - Index of the procedure in the module

-------
Returns
-------

``Status`` - Returns successful kickoff of installation or Error

-------
Example Body
-------

.. code-block:: javascript

    {
        "procedure": 1, 
        "catalog": "mytax",
        "module": 0,
        "dependency": 0
    }


------------------------------------------------------------------------------


procedureBuild ``POST``

.. code-block:: javascript

    localhost:5003/procedure/build


Installs all dependencies belonging to a procedure 

----------
Parameters
----------

1. - ``catalog`` ``String`` - Catalog name
2. - ``module`` ``Int``  - Index of the module version for a catalog entry
3. - ``procedure`` ``Int`` - Index of the procedure to completely install

-------
Returns
-------

``Status`` - Returns successful kickoff of installation or Error

-------
Example Body
-------

.. code-block:: javascript

    {
        "procedure": 0, 
        "catalog": "mytax",
        "module": 0
    }


------------------------------------------------------------------------------


moduleBuild ``POST``
---------

.. code-block:: javascript

    localhost:5003/module/build


Installs all procedures and their corresponding dependencies for a given catalog's module

----------
Parameters
----------

1. - ``catalog`` ``String`` - Catalog name
2. - ``module`` ``Int``  - Index of the module version for a catalog entry

-------
Returns
-------

``Status`` - Returns successful kickoff of installation or Error

-------
Example Body
-------

.. code-block:: javascript

    {
        "catalog": "mytax",
        "module": 0
    }


------------------------------------------------------------------------------