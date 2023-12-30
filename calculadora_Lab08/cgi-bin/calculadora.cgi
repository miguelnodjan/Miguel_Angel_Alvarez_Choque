#!"C:\xampp\perl\bin\perl.exe" -w

use strict;
use warnings;

use CGI;

# Create a new CGI object
my $cgi = CGI->new;

# Get the expression from the form
my $expresion = $cgi->param('expresion');

# Pattern to match a simple mathematical expression
if ($expresion =~ /^\s*(\.\d+)?)\s*([\+\-\*\/])\s*$/) {
    my $num1 = $1;
    my $operador = $3;
    my $num2 = $4;

    my $resultado;

    # Perform the calculation based on the operator
    if ($operador eq '+') {
        $resultado = $num1 + $num2;
    } elsif ($operador eq '-') {
        $resultado = $num1 - $num2;
    } elsif ($operador eq '*') {
        $resultado = $num1 * $num2;
    } elsif ($operador eq '/') {
        if ($num2 != 0) {
            $resultado = $num1 / $num2;
        } else {
            die "Error: División por cero.\n";
        }
    }
}