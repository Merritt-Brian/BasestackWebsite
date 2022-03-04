GAMMA
-----


`GAMMA <https://github.com/rastanton/GAMMA>`_ is a tool designed to analyze gene allele mutations for microbes, primarily bacterial genomes. 

.. note::
   This module outputs only a text file for analysis

-------
Parameters
-------

FASTA file : `File` 
   FASTA or genome file to check for AMR alleles

output : `String` 
   Text string to have as a prefix for the output file(s)

Gene Database file : `File` 
   ``.fsa`` file that contains the mapping of genes linked to AMR

-------
Returns
-------

GAMMA file : `Tab-separated file`
   
.. note::

   Below output gathered from `here <https://github.com/rastanton/GAMMA>`_

   The default output of GAMMA is a tab-delimited file with a “.gamma” extension with 15 columns:

   1. Gene – The name of the closest matching gene (target) from the database. If there are ambiguous gene matches (i.e., multiple target matches with the same number of non-degenerate codon changes, basepair changes, and transversions), the gene match will be appended with a "‡".
   2. Contig – The name of the contig on which the match was found.
   3. Start – The start position of the sequence matching the gene on the contig.
   4. Stop – The end position of the sequence matching the gene on the contig.
   5. Match_Type – The type of the gene match based on the translation of the sequence (i.e., the protein sequence). Can be native (for identical amino acid sequences to the target), mutant (for nonsynonymous mutations), truncation (for nonsense mutations), indels (for insertions/deletions), nonstop (for a missing stop codon), contig edge (for matches that are truncated at the start or stop of a contig), or a combination of multiple types (i.e., indel truncation).
   6. Description – A short description of the match type.
   7. Codon_Changes – The count of the non-degenerate codon changes in the sequence versus the closest match from the datbase.
   8. BP_Changes - The count of the basepair changes in the sequence versus the closest match from the datbase.
   9. Transversions - The count of basepair changes that are transversions (i.e., purine to pyrimidine or vice versa, such as an A -> C or a T -> G)
   10. Codon_Percent – The percent (expressed as a decimal value) of the degenerate codon similarity between the query and match sequence. Gene matches with large insertions may show a negative value.
   11. BP_Percent - The percent (expressed as a decimal value) of the basepair similarity between the query and match sequence. Gene matches with large insertions may show a negative value.
   12. Percent_Length - The percent (expressed as a decimal value) of the length of the target covered by the matching sequence, maximum of 1.
   13. Match_Length – The length (in basepairs) of the matching sequence.
   14. Target_Length - The length (in basepairs) of the target sequence.
   15. Strand – The sense of the strand (+ or -) on which the match is found.

