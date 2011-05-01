#
# Problem: Ambiguous
# URL: http://www.codechef.com/problems/PERMUT2
#
# Author: Ronald Kaiser
# Email: raios dot catodicos at gmail dot com
#

while (<>) {
    last if $_ == 0;
    
    my @in = split /\s+/, <>;
    my $flag = 0;
    for my $i (0 .. @in - 1) {
        if ($in[$in[$i] - 1] != $i + 1) {
            print "not ambiguous\n";
            $flag = 1;
            last;
        }
    }
    print "ambiguous\n" if ($flag == 0);
}
