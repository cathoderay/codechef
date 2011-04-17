#
# Problem: Enourmous Input Test
# URL: http://www.codechef.com/problems/INTEST
#
# Author: Ronald Kaiser
# Email: raios dot catodicos at gmail dot com
#


my $in = <STDIN>;
(my $n, my $k) = split(/\s+/, $in);

if ($k == 1) {
    print $n . "\n";
    exit;
};

my $counter = 0;
while(<STDIN>) {
    chomp($_);
    if ($_ % $k == 0) {
        $counter++;
    };
};

print $counter . "\n";
