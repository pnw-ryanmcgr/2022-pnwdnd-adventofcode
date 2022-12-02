#!/usr/bin/perl

#curse VAST paying for dinner and drinks tonight

use strict;
use warnings;

open(my $fh, "input") or die("couldn't open file");

my $score = 0;

foreach my $line (<$fh>) {
  $line =~ m/(\w)\s(\w)\n/;
  if ($2 eq "X") { # lose
    $score += 1 if $1 eq "B";
    $score += 2 if $1 eq "C";
    $score += 3 if $1 eq "A";
  }
  elsif ($2 eq "Y") { # draw
    $score += 4 if $1 eq "A";
    $score += 5 if $1 eq "B";
    $score += 6 if $1 eq "C";
  }
  else { # win
    $score += 7 if $1 eq "C";
    $score += 8 if $1 eq "A";
    $score += 9 if $1 eq "B";
  }
}

print "score is: $score\n";

close($fh)
