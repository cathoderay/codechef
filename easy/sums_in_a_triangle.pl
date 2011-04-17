#
# Problem: Sums in a triangle
# URL: http://www.codechef.com/problems/SUMTRIAN
#
# Author: Ronald Kaiser
# Email: raios dot catodicos at gmail dot com
#
# Observation: This unfortunately doesn't solve the problem 
# in the time limit imposed by codechef.
# As it's based on recursion and generates a binary tree, 
# this solution for n > 20 becomes slow (in an ordinary machine).
# 
# Better trying another approach.
# 

use List::Util qw[max];

my @triangle = ();

sub solve {
    (my $sum, my $l, my $c) = @_;

    $sum += $triangle[$l]->[$c];
    my $path1, my $path2 = 0, 0;

    if (undef != $triangle[$l + 1]) {
        $path1 = solve($sum, $l + 1, $c);
        if(undef != $triangle[$l + 1]->[$c + 1]) { 
            $path2 = solve($sum, $l + 1, $c + 1)
        }
        return max($path1, $path2); 
   } else {
       return $sum;
   };
};

chop(my $n = <>);

while(<>) {
    chop; 
    @triangle = ();
    for(1 .. $_) {
        my $line = <>;
        my @line = split(/\s+/, $line);
        push(@triangle, \@line);
    }   

    print solve(0, 0, 0);
    print "\n";
    $n--;
    last if $n == 0;
};
