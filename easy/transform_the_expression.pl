#
# Problem: Transform the expression
# URL: http://www.codechef.com/problems/ONP
#
# Author: Ronald Kaiser
# Email: raios dot catodicos at gmail dot com
#


my $n = <STDIN>;
chop($n);

while(<STDIN>) {
    chop($_);

    my @in = split(//, $_);
    my @operators = ();
    my @solution = ();
    my $i = 0;
    for (@in) {
        if ($_ =~ m/[a-z]/) {
            @solution[$i] = $_;
        } elsif ($_ eq ")") {
            push(@solution, pop(@operators));
        } elsif ($_ =~ m/[-+*\/^]/) {
            push(@operators, $_);
        }
        $i++;
    };
    print @solution; 
    print "\n";
    
    $n--;
    last if $n == 0;
};
