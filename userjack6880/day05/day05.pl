#!/usr/bin/perl

use strict;
use warnings;

open(my $fh, "input") or die("couldn't open file");

my $phase = 0;
# phase 0 is getting the stacks
# phase 1 is making moves
my %stacks;

for (my $i = 1; $i < 10; $i++) {
  $stacks{$i}{'top'} = 0;
}

foreach my $line (<$fh>) {
  if ($line =~ m/^\s\d/) {
    next;
  }
  if ($line =~ m/^\n/) {
    $phase = 1;
    next;
  }
  if ($phase == 0) {
    $line =~ s/\n//g;
    my @crates = split('',$line);
    my $column = 0;
    my $stack = 1;
    foreach my $value (@crates) {
      if ($column == 3) {
        $column = 0;
        $stack++;
        next;
      }
      if ($value eq "[" || $value eq "]" || $value eq " ") {
        $column++;
        next;
      }
      else {
        $column++;
        if ($stacks{$stack}{'top'} == 0) {         # if top index is 0, then put value there
          $stacks{$stack}{1} = $value;
          $stacks{$stack}{'top'} = 1;
        }
        else {
          my $top = $stacks{$stack}{'top'}+1;      # indicate new top index
          $stacks{$stack}{'top'} = $top;
          for (my $i = $top; $i > 1; $i--) {        # shift values up 1
            $stacks{$stack}{$i} = $stacks{$stack}{$i-1};
          }
          $stacks{$stack}{1} = $value;             # put new item in index 0
        }
      }
    }
  }
  else {
    my @move = split(' ',$line);
    for (my $i = 0; $i < $move[1]; $i++) {
      my $top_from = $stacks{$move[3]}{'top'};     # top of from stack
      my $top_to = $stacks{$move[5]}{'top'};       # top of to stack
      my $top_item = $stacks{$move[3]}{$top_from}; # top item of from stack
      $top_to++;                                   # move index of to stack up
      $stacks{$move[5]}{'top'} = $top_to;          # change the stored top index
      $stacks{$move[5]}{$top_to} = $top_item;      # save value of top item in to stack
      $top_from--;                                 # move index of from stack down
      $stacks{$move[3]}{'top'} = $top_from;        # change the stored top index
    }
  }
}

print "top items: ";
for (my $stack = 1; $stack < 10; $stack++) {
  my $top = $stacks{$stack}{'top'};
  print $stacks{$stack}{$top};
}
print "\n";

close($fh)