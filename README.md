# Programs
## SILVA_domain.py
This program helps you arrange taxanomy file downloaded from SILVA.

Input file should be in one file consisting of two sheets.
### Input
first filedialog

1. hierarchical data from SILVA (taxanomy server) in txt file (~_tax_assignments.txt)

second filedialog

2. read abundance result from taxonomy server in txt file

Those two files are the raw files from the server.

third filedialog

3. namemap in txt

This helps you replace the name code with name found from Namemap.txt

### Return 
1. xlsx file merging hierarchy and read abundance with the name from Namemap

This will be the input file to SILVA_conversion.py

## SILVA_conversion.py
This program helps you organize the NGS result.

### Input 
the result file from 'SILVA_domain.py'. 

The result of this program would be the excel files with total 19sheets.
### results
1. OTUs : the whole hierarchy from domain to species with each read abundance
2. #_read : the absolute number of read abundance for each samples when grouped by # hierarchy
3. #(%) : the percentage of read abundance for each samples when grouped by # hierarchy
4. #_rank(%) : the major OTU shown by # hierarchy which was selected by maximum percentage of read abundance for each OTU showing more than 1%
