#!/usr/bin/perl -w

############################################################
# Program: water_2_jugs.pl
# Comment: Euclidean Algorithm for The Water 2-Jug Problem
# Perl Version: v5.10.0
# Run It 1: ./water_2_jugs.pl
# Run It 2: perl water_2_jugs.pl
# Runtime Environment: Snow Leopard 10.6.4
# Date: Oct 22nd, 2010
# Author: Fei Zhao
# Warnning: All Rights Reserved
############################################################

# About This Program:
# We are given two jugs named L and S, a 7-gallon (L jug) one and 5-gallon (S jug) one. Neither has any measuring marks on it. There is a pump that can be used to fill the jugs with  water. How can you get exactly 4 gallons of water into the 7-gallon jug?

use strict;
use warnings;

sub gcd{
    $_[0] == 0 ? $_[1] : &gcd($_[1] % $_[0], $_[0]);
}

my $l = $ARGV[0];
my $s = $ARGV[1];
my $n = $ARGV[2];

#my $l = 7;
#my $s = 5;
#my $n = 4;

my $x = 0;
my $y = 0;


if( ($n > $l) && ($n > $s) || ($n % &gcd($l, $s) != 0) ){
    print "Impossible\n";
    exit -1;
}

do{
    if($x == 0){
	print "fill red\n";
	$x = $l;
    }
    elsif($y == $s){
	print "empty blue\n";
	$y = 0;
    }
    elsif($x < $s - $y){
	print "pour red into blue\n";
	$y += $x;
	$x = 0;
    }
    else{
	print "red to blue until max blue\n";
	$x -= $s - $y;
	$y = $s;
    }
}while( ($x != $n) && ($y != $n));

if($x == $n){
    print "red success\n";
}

if($y == $n){
    print "blue success\n";
}
