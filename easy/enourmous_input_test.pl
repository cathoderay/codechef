#
# Problem: Enourmous Input Test
# URL: http://www.codechef.com/problems/INTEST
#
# Author: Ronald Kaiser
# Email: raios dot catodicos at gmail dot com
#


my $in = <>;
my ($n, $k) = split(/\s+/, $in);

if ($k == 1) {
    print $n . "\n";
    exit;
};

my $counter = 0;
while(<>) {
    chop;
    $counter++ if ($_ % $k == 0) 
};

print $counter . "\n";
