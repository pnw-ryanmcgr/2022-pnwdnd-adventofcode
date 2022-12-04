#!/usr/bin/perl

use strict;
use warnings;

open(my $fh, "input") or die("couldn't open file");

my $inclusive = 0;
my $overlap = 0;

foreach my $line (<$fh>) {
  $line =~ s/\n//g;
  my @ass = split(',',$line);
  my %elf_ranges;
  my $elf_num = 1;
  foreach my $elf_ass (@ass) {
    my @range = split('-',$elf_ass);
    $elf_ranges{$elf_num}{'lower'} = $range[0];
    $elf_ranges{$elf_num}{'upper'} = $range[1];
    $elf_num++;
  }
  
  if (($elf_ranges{1}{'lower'} <= $elf_ranges{2}{'lower'} && 
       $elf_ranges{1}{'upper'} >= $elf_ranges{2}{'upper'}) ||
      ($elf_ranges{2}{'lower'} <= $elf_ranges{1}{'lower'} &&
       $elf_ranges{2}{'upper'} >= $elf_ranges{1}{'upper'})) {
    $inclusive++;
    $overlap++;
  }
  elsif (($elf_ranges{1}{'lower'} < $elf_ranges{2}{'lower'} &&
          $elf_ranges{1}{'upper'} <= $elf_ranges{2}{'upper'} &&
          $elf_ranges{1}{'upper'} >= $elf_ranges{2}{'lower'}) || #lower overlap

         ($elf_ranges{1}{'lower'} >= $elf_ranges{2}{'lower'} &&
          $elf_ranges{1}{'lower'} <= $elf_ranges{2}{'upper'} &&
          $elf_ranges{1}{'upper'} > $elf_ranges{2}{'upper'})) {
    $overlap++;
  }
}

print "there are $inclusive groups of elves where on range fully contains the other\n";
print "$overlap groups of elves overlap\n";

close($fh)