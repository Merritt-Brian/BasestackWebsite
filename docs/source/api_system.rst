System
====


.. note::
    To get the status of the server at the specified port,
    you can use the ``curl`` or `Postman <https://www.postman.com/>`_ to test your calls. 


Pinging the Server ``GET``
---------

.. note::
   You can use Postman as your API management toolkit for testing the server

``curl localhost:5003/server/ping``

returns

.. code-block:: console

   {"status":200,"message":"Server is running at port: 5003"}

getServerLogs ``GET``
---------

.. code-block:: javascript

    curl localhost:5003/log/system


-------
Returns
-------

``Array`` - List of all services that belong to a specific version of a module's procedure in the catalog

-------
Example
-------

.. code-block:: javascript

    curl localhost:5003/log/system

    {
    "status": 200,
    "message": "Got system log",
    "data": [
        "2022-02-14T23:17:12.235Z [info]: stdout: Indel at position 29094: [0, 75, 0, 0, 0, 13, 0] 75",
        "Indel at position 29130: [0, 0, 1, 77, 0, 4, 15] 78",
        "",
        "2022-02-14T23:17:12.236Z [info]: stdout: Indel at position 29323: [230, 0, 0, 0, 0, 35, 18] 230",
        "Indel at position 29376: [0, 0, 0, 97, 0, 2, 41] 97",
        "",
        "2022-02-14T23:17:12.237Z [info]: stdout: Indel at position 29385: [0, 125, 0, 0, 0, 21, 41] 125",
        "",
        "2022-02-14T23:17:12.237Z [info]: stdout: Indel at position 29426: [2, 0, 73, 0, 0, 13, 0] 75",
        "",
        "2022-02-14T23:17:12.237Z [info]: stdout: Indel at position 29753: [0, 110, 0, 0, 0, 3, 18] 110",
        "",
        "2022-02-14T23:17:12.238Z [info]: stdout: Indel at position 29775: [92, 0, 0, 0, 0, 7, 16] 92",
        "",
        "2022-02-14T23:17:12.239Z [info]: stdout: Indel at position 29799: [1, 0, 119, 0, 0, 3, 35] 120",
        "",
        "2022-02-14T23:17:12.277Z [info]: stdout: -[2022-02-14 23:17:12] Starting Module 4 Merging and Allele Frequencies on     /opt/data/artic-pipeline/4-draft-consensus/Sample3_NB03.nanopolish.merged.vcf, /opt/data/artic-pipeline/4-draft-consensus/Sample3_NB03.medaka.merged.vcf, /opt/data/artic-pipeline/4-draft-consensus/Sample3_NB03.samtools.vcf",
        "",
        "2022-02-14T23:17:13.124Z [info]: stdout: ^[2022-02-14 23:17:13] SAMPLE Sample3_NB03: Module 4 Samtools and Merging: processing complete",
        "",


.. note:: 
    Above logs were delivered during a run of a :doc:`Consensus pipeline <basestack_consensus>` procedure 