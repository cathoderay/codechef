#
# Problem: Sums in a triangle
# URL: http://www.codechef.com/problems/SUMTRIAN
#
# Author: Ronald Kaiser
# Email: raios dot catodicos at gmail dot com
#
# Observation: This is a so much better version than the
# previous one, but it can be better.
#

use List::Util qw[max];

my @triangle = ();
my @memoized = ();

sub solve {
    my ($sum, $l, $c) = @_;
    if (undef != $memoized[$l]->[$c]) {
        return $memoized[$l]->[$c];
    };

    $sum += $triangle[$l]->[$c];
    my $path1, my $path2 = 0, 0;

    if (undef != $triangle[$l + 1]) {
        $path1 = solve($sum, $l + 1, $c);
        if(undef != $triangle[$l + 1]->[$c + 1]) { 
            $path2 = solve($sum, $l + 1, $c + 1)
        }
        $memoized[$l]->[$c] = $sum;
        return max($path1, $path2); 
   } else {
       $memoized[$l]->[$c] = $sum;
       return $sum;
   };
};

chop(my $n = <>);

while(<>) {
    chop; 
    @triangle = ();
    @memoized = ();
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
