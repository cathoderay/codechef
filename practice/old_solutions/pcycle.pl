#
# Problem: Permutation Cycles
# URL: http://www.codechef.com/problems/PCYCLE
#
# Author: Ronald Kaiser
# Email: raios dot catodicos at gmail dot com
#


use feature qw(say);

chop(my $n = <>);
my @list = (-1, split(/\s+/, <>));

my @m = (-1, ((0)x$n));

my @current_cycle = ();
my @all_cycles = ();
my $i = 1;

while (1) {
    push @current_cycle, $i;
    if ($m[$i] == 1) {
        my @copy = @current_cycle;
        @all_cycles = (@all_cycles, \@copy);
        @current_cycle = ();
        my @r = grep $m[$_] == 0, 1..$#m;
        if (@r > 0) {
             $i = shift @r;
        }
        else {
            say scalar(@all_cycles);
            foreach my $cycle (@all_cycles) {
                say "@{$cycle}";
            }
            exit 0;
        };
    }
    else {
        $m[$i] = 1;
        $i = $list[$i];
    }
}
