#!/usr/bin/perl
use strict;
use warnings;
use CGI::Carp qw (warningsToBrowser fatalsToBrowser);

use CGI;

my $cgi = CGI->new();
print $cgi->header();

print("Wallpaper OS");

exit();
