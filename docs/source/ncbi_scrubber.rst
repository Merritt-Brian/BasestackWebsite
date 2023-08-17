
NCBI Scrubber
------

.. note:: 
   Only works on interleaved R1/R2 fastq file OR NanoPore reads. 

NCBI scubber removes human reads from sequencing data

-------
Parameters
-------
input  : `File` 
   Your input fastq file. Can be compressed but you must check "decompressed" if so
interleaved : `Boolean` 
   Is the file interleaved? (TRUE/FALSE, Illumina)
decompressed: `Boolean`
   Check if your file is compressed. You can decompress it directly in the UI here to the name: decompressed.fastq in the same path as the input file
   
-------
Returns
-------


Filtered File : `.filtered.fastq`
   removed of human reads

