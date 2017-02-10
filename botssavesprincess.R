f <- file('stdin')
open(f)
on.exit(close(f))
inp <- read.table(f, fill = TRUE, sep = '\n')
n <- as.integer(readline(f))
grids <- 
for (i in c(1:n))
{

  str <- as.character(readline())
  str <- as.vector(strsplit(str,''))
  for(j in c(1:n)){
    grids[i,j] <- str[[1]][j]
  }
}
p <- which(grids =='p', arr.ind = TRUE)
m <- which(grids =='m', arr.ind = TRUE)
diff <- p - m
vert <- ifelse(diff[1] < 0, paste(rep('UP\n',abs(diff[1])), collapse = ''), paste(rep('DOWN\n',abs(diff[1])), collapse = ''))
horz <- ifelse(diff[1] > 0, paste(rep('RIGHT\n',diff[2]), collapse = ''), paste(rep('LEFT\n',abs(diff[2])), collapse = ''))
write((paste(vert, horz, sep ='')), stdout())

