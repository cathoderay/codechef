#
# Problem: Birthday Candles
# URL: http://www.codechef.com/problems/CANDLE
#
# Author: Ronald Kaiser
# Email: raios dot catodicos at gmail dot com
#


use strict;
use feature qw(say);
use List::Util qw(min max);

chop(my $t = <>);

for (1..$t) {
   my @freq = split /\s+/, <>; 
   my %hash_ref = {};
   for (0..9) {%hash_ref->{$_} = $freq[$_]};
   my $min_freq = min @freq;
   my $max_freq = max @freq;

   my $min_candle = -1;
   for (0..9) {
       if (%hash_ref->{$_} == $min_freq) {
           $min_candle = $_;
           ($_ == 0) ? next : last;
       }
   }
   if (($max_freq == 0 and $min_freq == 0)) {
       say 1;
       next;
   }
   $min_candle == 0 ? say 10**(%hash_ref->{0}+1) : say "$min_candle"x($min_freq+1);
}
