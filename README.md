# Programs
## SILVA_domain.py
This program helps you arrange taxanomy file downloaded from SILVA. 
Input file should be in one file consisting of two sheets.
1st sheet should be the hierarchical data from SILVA (taxanomy server) and
2nd sheet should be the read abundance result from NGS analysis.
Those two sheets are the raw data from each server.

## SILVA_conversion.py
This program helps you organize the NGS result.
Input file is the result file from 'SILVA_domain.py'. 
The result of this program would be the excel files with total 19sheets.
### results
1. OTUs : the whole hierarchy from domain to species with each read abundance
2. #_read : the absolute number of read abundance for each samples when grouped by # hierarchy
3. #(%) : the percentage of read abundance for each samples when grouped by # hierarchy
4. #_rank(%) : the major OTU shown by # hierarchy which was selected by maximum percentage of read abundance for each OTU showing more than 1%
