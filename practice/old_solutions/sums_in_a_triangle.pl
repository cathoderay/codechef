#
# Problem: Sums in a triangle
# URL: http://www.codechef.com/problems/SUMTRIAN
#
# Author: Ronald Kaiser
# Email: raios dot catodicos at gmail dot com
#
# Observation: This is a so much better version than the
# previous one, but it can be better.
# This code didn't pass in the Time limit of codechef, although
# the same algorithm in C code, runs pretty well. 
# Investigate a better approach in Perl.
#


chomp(my $n = <>);

my @triangle = [];
while(<>) {
    chomp($_);
    for(1 .. $_) {
        my @line = split(/\s+/, <>);
        @triangle[$_ - 1] = \@line;
    }  
    for (my $i = $_-2; $i >= 0; $i--) { 
        for (my $j = 0; $j <= $i; $j++) {
            $triangle[$i][$j] += ($triangle[$i+1][$j] > $triangle[$i+1][$j+1]) ? 
                                    $triangle[$i+1][$j] : $triangle[$i+1][$j+1];
        }
    };
    print "$triangle[0]->[0]" . "\n";

    $n--;
    last if $n == 0;
};
