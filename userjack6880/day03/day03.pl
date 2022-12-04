#!/usr/bin/perl

use strict;
use warnings;

open(my $fh, "input") or die("couldn't open file");

my @matched;

foreach my $line (<$fh>) {
  $line =~ s/\n//g;
  my $pocket_1 = substr($line,0,(length($line)/2));
  my $pocket_2 = substr($line,((length($line)/2)));

  foreach my $item (split //, $pocket_1) {
    if ($pocket_2 =~ m/($item)/) {
      push(@matched, $item);
      last;
    }
  }

}

my $sum = 0;
foreach my $item (@matched) {
  my $value;
  if ($item eq lc($item)) {
    $value = ord($item) - 96;
  }
  else {
    $value = ord($item) - 38;
  }
  $sum += $value;
}

print "total is $sum\n";

close($fh)