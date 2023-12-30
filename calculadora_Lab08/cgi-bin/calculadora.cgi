#!"C:\xampp\perl\bin\perl.exe" -w

use strict;
use warnings;

use CGI;

# Create a new CGI object
my $cgi = CGI->new;

# Get the expression from the form
my $expresion = $cgi->param('expresion');

# Pattern to match a simple mathematical expression
if ($expresion =~ /^\s*(-?\d+(\.\d+)?)\s*([\+\-\*\/])\s*(-?\d+(\.\d+)?)\s*$/) {
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

    # Print the HTML response
    print $cgi->header;
    print<<BLOCK;
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <link rel="stylesheet" type="text/css" href="style.css">
        <title>Calculadora Básica</title>
    </head>
    <body>
        <nav class="BarraNavegacion">
            <div class="logo">
                <picture><img src="LOGO_UNSA.png" width="20%" alt="logo"></picture>
            </div>
            <a href="https://www.unsa.edu.pe/">Más de UNSA </a>
            <a href="https://github.com/miguelnodjan/Miguel_Angel_Alvarez_Choque.git">Repositorio personal</a>    
        </nav>
        <picture><img class="logoCentral" src="LOGO_UNSA.png" width="30%" alt="logo"></picture>
        <div class="contenido">
            <h1>Calculadora Basica</h1>
            <form action="/cgi-bin/calculadora.cgi" method="post">
                <input type="text"  name="ecuacion">
                <p>Respuesta: $resultado </p>
                <input type="submit" value="Calcular">
                <table style="width:100%">
                    <tr>
                        <td>  <input type="button" value="1"></td>
                        <td><input type="button" value="2"></td>
                        <td><input type="button" value="3"></td>
                        <td><input class="operador" type="button" value=" +"></td>
                    </tr>
                    <tr>
                        <td>  <input type="button" value="4"></td>
                        <td><input type="button" value="5"></td>
                        <td><input type="button" value="6"></td>
                        <td><input class="operador" type="button" value=" -"></td>
                    </tr>
                    <tr>
                        <td>  <input type="button" value="7"></td>
                        <td><input type="button" value="8"></td>
                        <td><input type="button" value="9"></td>
                        <td><input class="operador" type="button" value=" x"></td>
                    </tr>
                <tr>
                        <td>  <input type="button" value="("></td>
                        <td><input type="button" value="0"></td>
                        <td><input type="button" value=")"></td>
                        <td><input class="operador" type="button" value=" ÷"></td>
                    </tr>
                    <tr>
                        <td>  <input type="button" value="( - )"></td>
                        <td><input type="button" value=" "></td>
                        <td><input type="button" value=" "></td>
                        <td><input class="operador" class="botonBuscar" type="submit" name="operacion" value="="></td>
                    </tr>
                </table>
            </form>
        </div>
    </body>
    </html>
BLOCK
} else {
    # Print an error message if the expression is not valid
    print $cgi->header;
    print<<BLOCK;
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
		<link rel="stylesheet" type="text/css" href="style.css">
        <title>Calculadora Básica</title>
    </head>
    <body>
        <nav class="BarraNavegacion">
            <div class="logo">
                <picture><img src="LOGO_UNSA.png" width="20%" alt="logo"></picture>
            </div>
            <a href="https://www.unsa.edu.pe/">Más de UNSA </a>
            <a href="https://github.com/miguelnodjan/Miguel_Angel_Alvarez_Choque.git">Repositorio personal</a>    
        </nav>
        <picture><img class="logoCentral" src="LOGO_UNSA.png" width="30%" alt="logo"></picture>
        <div class="contenido">
            <h1>Calculadora Básica</h1>
            <form action="/cgi-bin/calculadora.cgi" method="post">
                <input type="text"  name="ecuacion">
                <p>Respuesta: ERROR al operar </p>
                <input type="submit" value="Calcular">
                <table style="width:100%">
                    <tr>
                        <td>  <input type="button" value="1"></td>
                        <td><input type="button" value="2"></td>
                        <td><input type="button" value="3"></td>
                        <td><input class="operador" type="button" value=" +"></td>
                    </tr>
                    <tr>
                        <td>  <input type="button" value="4"></td>
                        <td><input type="button" value="5"></td>
                        <td><input type="button" value="6"></td>
                        <td><input class="operador" type="button" value=" -"></td>
                    </tr>
                    <tr>
                        <td>  <input type="button" value="7"></td>
                        <td><input type="button" value="8"></td>
                        <td><input type="button" value="9"></td>
                        <td><input class="operador" type="button" value=" x"></td>
                    </tr>
                <tr>
                        <td>  <input type="button" value="("></td>
                        <td><input type="button" value="0"></td>
                        <td><input type="button" value=")"></td>
                        <td><input class="operador" type="button" value=" ÷"></td>
                    </tr>
                    <tr>
                        <td>  <input type="button" value="( - )"></td>
                        <td><input type="button" value=" "></td>
                        <td><input type="button" value=" "></td>
                        <td><input class="operador" class="botonBuscar" type="submit" name="operacion" value="="></td>
                    </tr>
                </table>
            </form>
        </div>
    </body>
    </html>
BLOCK
}
