#
# Problem: Internet Media Type
# URL: http://www.codechef.com/problems/MIME2
#
# Author: Ronald Kaiser
# Email: raios dot catodicos at gmail dot com
#
# Observation: this problem was in the 24th Apr Cook-off competition
#


use feature qw(say);

my ($n, $q) = split /\s+/, <>;
my $table = {};
for (1 .. $n ) {
    my ($key, $val) = split /\s+/, <>;
    $table->{$key} = $val;	
}

for (1 .. $q) {
    chomp(my $line = <>);
    if ($line =~ m/.*\.(?<ext>[a-z0-9]+)/ig) {
        my $ext = $+{ext};
        (exists $table->{$ext}) ? say "$table->{$ext}" : say "unknown";
    } else {
        say "unknown";
    }
}
