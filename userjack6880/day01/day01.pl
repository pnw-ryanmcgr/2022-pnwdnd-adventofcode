#!/usr/bin/perl

use strict;
use warnings;

open(my $fh, "input") or die("couldn't open file");

my %elves;
my $current = 0;
my @most;

$elves{$current} = 0;

foreach my $line (<$fh>) {
  if ($line =~ m/(\d+)\n/) {
    $elves{$current} += $1;
  }
  else {
    my $pushed = 0;
    for (my $i = 0; $i < $#most; $i++) {
      if ($elves{$current} > $elves{$most[$i]}) {
        splice(@most,$i,0,$current);
        $pushed = 1;
        last;
      }
    }

    push(@most, $current) if !$pushed;

    $current++;
  }
}

my $total = $elves{$most[0]} + $elves{$most[1]} + $elves{$most[2]};

print "the elves with the most are ".$most[0].", ".$most[1].", and ".$most[2]." having a total Calorie count of: $total\n";

close($fh)