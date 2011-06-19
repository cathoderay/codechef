#
# Problem: Holes in the text
# URL: http://www.codechef.com/problems/HOLES
# 
# Author: Ronald Kaiser
# Email: raios dot catodicos at gmail dot com
#


use feature qw(say);

my $h_ref = {'A' => 1, 'B' => 2, 'C' => 0, 'D' => 1, 'E' => 0, 'F' => 0, 'G' => 0, 'H' => 0,
             'I' => 0, 'J' => 0, 'K' => 0, 'L' => 0, 'M' => 0, 'N' => 0, 'O' => 1, 'P' => 1,
             'Q' => 1, 'R' => 1, 'S' => 0, 'T' => 0, 'U' => 0, 'V' => 0, 'X' => 0, 'W' => 0,
             'Y' => 0, 'Z' => 0};

chop(my $n = <>);
for (1..$n) {
    my @word = split //, <>;
    my $sum = 0;
    foreach (@word) { $sum += $h_ref->{$_};}
    say $sum;
}
