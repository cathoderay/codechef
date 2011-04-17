#
# Problem: Odd
# URL: http://www.codechef.com/problems/DCE05
#
# Author: Ronald Kaiser
# Email: raios dot catodicos at gmail dot com
#


my $n = <STDIN>;
chomp($n);

while(<STDIN>) {
    chomp($_);
    print 1 << int(log($_)/log(2));

    print "\n";
    $n--;
    last if $n == 0;
};
