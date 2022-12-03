#!/usr/bin/perl

use strict;
use warnings;

open(my $fh, "input") or die("couldn't open file");

my @matched;
my %elf;
my $enumber = 1;

foreach my $line (<$fh>) {
  $elf{$enumber} = $line;

  if ($enumber == 3) {
    foreach my $item (split //, $elf{1}) {
      if ($elf{2} =~ m/($item)/ && $elf{3} =~ m/($item)/) {
        push(@matched, $item);
        last;
      }
    }
    $enumber = 1;
  }
  else {
    $enumber++;
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