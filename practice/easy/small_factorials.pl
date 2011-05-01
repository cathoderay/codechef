#
# Problem: Small factorials
# URL: http://www.codechef.com/problems/FCTRL2
#
# Author: Ronald Kaiser
# Email: raios dot catodicos at gmail dot com
#


use bignum;

my $n = <STDIN>;
chomp($n);

my @precalculated = (1,);
for (1 .. 100) {
    @precalculated[$_] = @precalculated[$_ - 1]*$_;
};

while(<STDIN>) {
    chomp($_);
    print @precalculated[$_] . "\n";
    $n--;
    last if $n == 0;
};
