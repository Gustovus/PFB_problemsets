#!/usr/bin/env python3

#Highest Score of PAM matrices 30, 70, & 250?
#PAM30 = 13	PAM70 = 13 	PAM250 = 17

#Highest Score for a W-W match?
#PAM30 = 13	PAM70 = 13	PAM250 = 17

#Scores for W-G mismatch?
#PAM30 = -15	PAM70 = -10	PAM250 = -7

#How long is the query sequence?
# 209 aa

#How many sequences are in the PIR1 database?
#13144

#What scoring matrix was used?
#BL50 matrix(15:5)xS

#What were the gap penalties?
#-10/-2 (open/ext)

#What are each of the numbers after the description of the library sequence? Which one is best for inferring homology?
#The search scores and the best is e-value

#Looking at an alignment, where are the boundaries of the alignment (the best local region)?
#

#What is the highest scoring non-homolog? (The non-homolog with the highest alignment score, or the lowest E()-value.) How would you confirm that your candidate non-homolog was truly unrelated?


#Note that this drosophila glutathione transferase shares significant similarity with both sequences from bacteria (SSPA_EOC57) and mammals. How might you test whether the stringent starvation protein is homologous to glutathione transferases? (Hint - compare your candidate non-homolog with SwissProt for a more reliable test.)


#Compare the expectation (E()) value for the distant relationship between GSTT1_DROME and GSTM2_RAT (class-mu). How would you demonstrate that GSTT1_DROME is homologous to GSTM2_RAT?
#GSTT1_Drome e-value is 6.4e-104 and for GSTM2_Rat(mu) is .2. You would demonstrate homology by a reciprocal blast

#Examine how the expectation value changes with different scoring matrices (BLOSUM62, BlastP62, PAM250) and different gap penalties. (The default scoring matrix for the FASTA programs is BLOSUM50, with gap penalties of -10 to open a gap and -2 for each residue in the gap - e.g. -12 for a one residue gap).
#BlastP62(Drome: 2.3e-117 Rat: .83) PAM250(Drome: 3.2e-75 Rat: MUCH HIGHER)

#What happens to the E()-value for the 100% identical sequence with the different matrices and different gap penalties?
#Changes (?)

#What happens to the E()-value for distant homologs, like GSTA1_RAT with the different matrices and different gap penalties?
#E-value decreases as the gap penalties increase

#What happens to the E()-value for the highest scoring unrelated sequence with the different matrices?
#E-value increases as the gap penalties increase and 

#Try the search ssearch (Smith-Waterman). Again, look at the E()-values for distant homologs and the highest scoring unrelated sequence.
#Most e-values decreased but the order of the scoring did not change much

#How long is the query sequence?
#209

#How many sequences are in the Swissprot database?
#470,882

#What scoring matrix was used?
#

#What were the gap penalties?


#Looking at an alignment, where are the boundaries of the alignment (the best local region)?


#What is the highest scoring non-homolog?


#How do the blastp E(), alignment length and score compare with the FASTA SSPA_ECO57?


