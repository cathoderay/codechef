#
# Problem: Stone Game
# URL: http://www.codechef.com/problems/RESN04
#
# Author: Ronald Kaiser
# Email: raios dot catodicos at gmail dot com


use feature qw(say);

chop(my $t = <>);
for (1..$t) {
    chop(my $n = <>);
    my @piles = split /\s+/, <>;
    my $plays = 0;
    for (1..@piles) { $plays += int($piles[$_-1]/$_) }
    ($plays % 2 == 1) ? say "ALICE" : say "BOB"
}
