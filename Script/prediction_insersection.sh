#!Rscript
# Usage: Rscript myscript.R
##################################################################################################################
#Taking the intersection of lncRNA identification results, to obtain high confidence lncRNAs.
##################################################################################################################
	
args<-commandArgs(TRUE)

#################################################
## R package
myPaths <- .libPaths()
library(tidyverse)


#################################################
##### 
candidate_lncRNA <- read.table(args[1], header = FALSE, col.names = "genes") %>% pull(genes)


##### PlantLncBoost
PlantLncBoost <- read_delim(args[2], delim = "\t", col_names = TRUE) %>% filter(Predicted_label == 1) %>% pull(id)

##### CPAT-plant
CPAT_plant <- read_delim(args[3], delim = "\t") %>% filter(coding_prob < 0.46) %>% pull(mRNA_size)


##### LncFinder-plant
LncFinder_plant <- read_delim(args[4], delim = "\t") %>% filter(Coding.Potential == "NonCoding") %>% pull(Pred)


##### Swissprot
uniprot <- read_delim(args[5], delim = "\t", col_names = FALSE) %>% filter(X3>60, X11<1e-5) %>% pull(X1) %>% unique()
uniprot <- dplyr::setdiff(candidate_lncRNA, uniprot)


##### Take intersection
lncRNA = Reduce(intersect, list(PlantLncBoost, CPAT_plant, LncFinder_plant, uniprot))
write.table(lncRNA, file = "Final_lncRNA_results.txt",
            row.names = F,
            col.names = F,
            quote = F)
				
##### Venn
#install.packages("VennDiagram") 
library(VennDiagram)
library(RColorBrewer)
library(scales)
color <- c("#9B9DCD", "#ECACA8", "#E96E6A", "#6976B7")
pdf(file = "Venn_pred_lncRNA.pdf", onefile = TRUE, width = 8, height = 8)
venn.plot <- venn.diagram(list(PlantLncBoost=PlantLncBoost, CPAT_plant=CPAT_plant, LncFinder_plant=LncFinder_plant, uniprot=uniprot),
  col = 'grey',
  alpha = 1,
  fill = color)
dev.off()  
  
  
  
  
  
  
  
  
  
  
  
  
  

  