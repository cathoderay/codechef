#
# Problem: Odd
# URL: http://www.codechef.com/problems/DCE05
#
# Author: Ronald Kaiser
# Email: raios dot catodicos at gmail dot com
#


chop(my $n = <>);

while(<>) {
    chop;
    print 1 << int(log($_)/log(2)) . "\n";

    $n--;
    last if $n == 0;
};
