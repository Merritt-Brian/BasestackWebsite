TaxTriage (Metagenomics) (Under Construction)
-----

.. warning:: 
   This module is under construction and is in alpha-release. Scheduled full release of v1.0 in Oct. 2022


Standard diagram for deployment and pipeline development

.. image:: ../assets/img/APHLPipeline.png
   :width: 100%

The pipeline consists of a variety of alignment/classification steps as well as QC and pre-filtering processes. 
It is designed to be serve as the initial triage step for identifying unknown organisms present in one or more
sample types and supports both Illumina or Oxford Nanopore-generated NGS data. 


The pipeline is packaged to include basic quality control to making a (potential) de-novo assembly for each organism
that is detected in the sample from a filtering a hierarchical perspective. That is, the most prevalent taxonomic IDs
at various ranks in the hierarchical chain are reported, binned, and run through a variety of alignment and assembly 
steps (for lower levels like species). Finally, a set of flags are generated for each taxonomic map that is the most prevalent per sample. 

A list of tools used are listed below for each step


1. Demultiplex and Gather **OPTIONAL, Oxford Nanopore Only** 
  - `Artic Guppyplex <https://nf-co.re/modules/artic_guppyplex>`_ - Aggregate Nanopore reads for downstream analysis 
2. Quality Control **OPTIONAL**
  - `PycoQC <https://nf-co.re/modules/pycoqc>`_ - Computes metrics and generates interactive QC plots for Oxford Nanopore technologies sequencing data
3. Trimming 
  - Illumina: `Trimgalore <https://nf-co.re/modules/trimgalore>`_
  - Oxford: `Porechop <https://nf-co.re/modules/porechop>`_
4. Filtering
  - `Kraken2 <https://nf-co.re/modules/kraken2_kraken2>`_
5. QC Plotting 
  - Illumina: `FastQC <https://nf-co.re/modules/fastqc>`_
  - Oxford: `Nanoplot <https://nf-co.re/modules/nanoplot>`_
6. Classification (K-mer approach)
  - `Kraken2 <https://nf-co.re/modules/kraken2_kraken2>`_
7. Alignent Stats
  - Illumina: `BWAMEM2 <https://nf-co.re/modules/bwamem2_mem>`_
  - Oxford: `Minimap2 <https://nf-co.re/modules/minimap2_align>`_
8. Report Generation 
  - `MultiQC <https://nf-co.re/modules/multiqc>`_




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
   * - single_end
     - Is the data single or paired end
   * - fastq_1
     - Full path to FastQ file for Illumina short reads 1 OR OXFORD reads. File has to be gzipped and have the extension ".fastq.gz" or ".fq.
   * - fastq_2
     - Full path to FastQ file for Illumina short reads 2. File has to be gzipped and have the extension ".fastq.gz" or ".fq.
   * - barcode
     - TRUE/FALSE, is the row attributed to a demultiplexed barcode folder of 1 or more fastq files or is it a single file that is .
   * - from
     - Directory path of the barcode, only used with the column being set as TRUE in the barcode column
   * - trim
     - TRUE/FALSE, do you want to run trimming on the sample? 
   * - platform
     - Platform used, [ILLUMINA, OXFORD]
   * - sequencing_summary
     - If detected, output plots based on the the sequencing summary file for that sample
     


.. list-table:: Example Samplesheet
   :header-rows: 1
   :stub-columns: 1
   :class: my-class
   :name: my-nametwo

   * - sample
     - fastq_1
     - fastq_2
     - platform 
     - from 
     - trim
     - sequencing_summary
     - single_end
     - barcode
     
   * - Sample_1
     - AEG588A1_S1_L001_R1_001.fastq.gz
     - AEG588A1_S1_L001_R2_001.fastq.gz
     - ILLUMINA
     - NULL (or leave blank)
     - FALSE
     - NULL (or leave blank)
     - FALSE
     - FALSE
   * - Sample_2
     - ecoli_reads.fastq
     - NULL
     - OXFORD
     - NULL
     - FALSE
     - sequencing_summary.txt
     - TRUE
     - FALSE
   * - Sample_3
     - NULL
     - NULL
     - OXFORD
     - barcode01
     - TRUE
     - FALSE
     - TRUE
     - TRUE


For the samples shown above: 

1. A paired-end run of Illumina data where we DON'T trim anything (no Trimgalore)
2. A single-end Oxford Nanopore run where all reads are concatenated to a single fastq file. No barcode. There is a sequencing summary file we want to plot for run statistics/plots
3. A single-end Oxford Nanopore run where reads have NOT been demultiplexed and/or aggregated to a single fastq file (like row 2). This will run `artic guppyplex` as well to concatenate all to one fastq file





-------
Returns
-------

1. MultiQC report HTML file 
2. Variety of intermediate and output results files for the MultiQC report
  - Examples: 
    - SAM/BAM alignment 
    - Filtered FASTQ Files (for downstream use)
    - Assembly (de novo) - WIP and is not ready just yet 
    - Kraken2 Report(s)
