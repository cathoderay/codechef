#
# Problem: The lead game
# URL: http://www.codechef.com/problems/TLG
#
# Author: Ronald Kaiser
# Email: raios dot catodicos at gmail dot com
#


use feature qw(say);

chop(my $rounds = <>);
my $max_diff = 0;
my $p1, $p2, $winner;

for (1..$rounds) {
    my ($cp1, $cp2) = split /\s+/, <>;
    $p1 += $cp1;
    $p2 += $cp2;
    my $cur_diff = $p1 - $p2;
    if (abs($cur_diff) > $max_diff) {
        $max_diff = abs $cur_diff;
        if ($cur_diff >= 0) { 
            $winner = 1;
        } else {
            $winner = 2;
        }
    }
}
print "$winner $max_diff\n"
