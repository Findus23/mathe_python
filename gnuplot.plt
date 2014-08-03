set nokey
set format x "%.0l*10^%T"
set output "output.png"
set terminal png size 1200,800
plot "daten.csv" with lines

set format x "10^%T"
set logscale xy
set output "log.png"
plot "daten.csv" with lines
