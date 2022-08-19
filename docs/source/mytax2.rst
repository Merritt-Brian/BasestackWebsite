Mytax version 2 (Metagenomics)
-----

.. warning:: 
   This module is under construction and is in alpha-release. Scheduled full release of v1.0 in Oct. 2022




**Please see relevant links in the listed modules for more information on the underlying mechanisms and corresponding papers (if existent)**



-------
Parameters
-------

- Samplesheet (.csv): `file` 

   Contains a mapping of metadata and a single sample per row. Explanations of the possible columns for Basestack are seen below:

.. list-table:: Samplesheet Description
   :header-rows: 1
   :stub-columns: 1
   :class: my-class
   :name: my-name

   * - Column Name
     - Description

   * - sample
     - Custom sample name. This entry will be identical for multiple sequencing libraries/runs from the same sample. Spaces in sample names are automatically converted to underscores (`_`).
   * - format
     - [directory, run, file] Is it a run directory of files that need to be demux'd, an already full directory of files for Oxford, or a single file (or paired files)
   * - path_1
     - Full path to FastQ file for Illumina short reads 1 OR OXFORD reads. File has to be gzipped and have the extension ".fastq.gz" or ".fq.
   * - path_2
     - Full path to FastQ file for Illumina short reads 2. File has to be gzipped and have the extension ".fastq.gz" or ".fq.
   * - kits
     - What default barcode kit to use for demux. Only applies to those with the "run" format
   * - pattern
     - Regex matching for the names of the folders that are made on demux. Default is barcode[0-9]+
   * - platform
     - Platform used, [illumina, oxford]
   * - database
     - Kraken2 database path (root level folder)
   * - compressed
     - TRUE/FALSE for gunzipped files
     


.. list-table:: Example Samplesheet
   :header-rows: 1
   :stub-columns: 1
   :class: my-class
   :name: my-nametwo

   * - sample
     - path_1
     - path_2
     - format 
     - platform 
     - database
     - compressed
     - pattern
     - kits
     
   * - covid_run
     - fastq_pass
     - NULL
     - run
     - oxford
     - NULL
     - NULL
     - barcode[0-9]+
     - EXP-NBD103
   * - NB03
     - ./NB11
     - NULL
     - directory
     - oxford
     - minikraken2
     - FALSE
     - NULL
     - NULL
   * - ERR123
     - ERR123_R1.fastq.gz
     - ERR123_R2.fastq.gz
     - file
     - illumina
     - flukraken2
     - TRUE
     - NULL
     - NULL

-------
Returns
-------
