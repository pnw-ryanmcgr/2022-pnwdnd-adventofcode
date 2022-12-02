#!/usr/bin/perl

#curse VAST paying for dinner and drinks tonight

use strict;
use warnings;

open(my $fh, "input") or die("couldn't open file");

my $score = 0;

foreach my $line (<$fh>) {
  $line =~ m/(\w)\s(\w)\n/;
  $score += 1 if $2 eq "X";
  $score += 2 if $2 eq "Y";
  $score += 3 if $2 eq "Z";

  if (($1 eq "A" && $2 eq "X") || ($1 eq "B" && $2 eq "Y") || ($1 eq "C" && $2 eq "Z")) {
    $score += 3;
  }
  if (($1 eq "A" && $2 eq "Y") || ($1 eq "B" && $2 eq "Z") || ($1 eq "C" && $2 eq "X")) {
    $score += 6;
  }
}

print "score is: $score\n";

close($fh)
