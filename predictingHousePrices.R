fil <- file("stdin")
open(fil)
fn <- readline()
fn <- strsplit(fn, split = ' ')
f <- fn[[1]][1]
n <- fn[[1]][2]
write(n, stdout())
close(fil)
