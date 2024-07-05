x1 <- c("AGAG","GACA", "CTAG")
y1 <- c("ATGA","TATT", "ACAG")
z1 <- c("ATAC","CTGG", "AATA")

# Creando una lista
mi_lista <- list(x1, y1, z1)
mi_lista


la <- c("mRNA1","mRNA2","mRNA3","Canti")
p1 <- c("AGAG","GACA", "CTAG",1)
p2 <- c("ATGA","TATT", "ACAG",4)
p3 <- c("ATAC","CTGG", "AATA",7)

# Creando una lista
gen <- list(la, p1, p2, p3)
gen

#Creando dataframe 

df_gen <- data.frame(mRNA = gen[[1]], 
                     p1 = gen[[2]], 
                     p2 = gen[[3]], 
                     p3 = gen[[4]])

#ordenar datos 
df_gen_organized <- df_gen[order(-df_gen_$la3)]

gen_organized


Revisar el video 
# https://www.youtube.com/watch?v=tlf6wYJrwKY

