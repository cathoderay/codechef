#
# Problem: Transform the expression
# URL: http://www.codechef.com/problems/ONP
#
# Author: Ronald Kaiser
# Email: raios dot catodicos at gmail dot com
#


chop(my $n = <>);

while(<STDIN>) {
    chop;

    my @in = split(//, $_);
    my (@operators, @solution) = (), ();
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
