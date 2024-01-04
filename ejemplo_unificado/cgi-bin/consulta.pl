#!"C:\xampp\perl\bin\perl.exe" -w
use strict;
use warnings;
use CGI;

print "Content-type: text/html\n\n";
print <<HTML;
<!DOCTYPE html>
<html>
  <head> 
    <meta charset="utf-8"> 
    <link rel="stylesheet" type="text/css" href="style.css">
    <title>Búsquedas en archivo CSV</title>
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
	<h1>RESULTADOS:</h1>
HTML

my $q = CGI->new;
my $keyword = $q->param("keyword");
my $flag;

if (!($keyword eq "")) {
  open(my $IN, '<', "Programas_de_Universidades.csv") or die "<h1>ERROR: open file</h1>\n";
  while (my $line = <$IN>) {
    my %dict = matchLine($line);
    if (matchFields(\%dict, $keyword)) {
      print "<p>Encontrado: $line</p>\n";
      $flag = 1;
      next; # continue the loop
    }
  }
  close($IN);
}

if (!defined($flag)) {
  print "<h1>No encontrado</h1>\n";
}

print <<HTML;
    Ingrese <a href="/../../consulta.html">aquí</a> para regresar al formulario de búsqueda
  </body>
</html>

HTML

# Subrutina para procesar la línea y devolver un hash.
sub matchLine {
  my %dict = ();
  my $line = $_[0];
  if ($line =~ /(.+?)\|(.+?)\|(?:.+?\|){2}(.+?)\|(?:.+?\|){5}(.+?)\|(?:.+?\|){5}(.+?)\|/) {
    $dict{"nombre_universidad"} = $1;
    $dict{"periodo_licenciamiento"} = $2;
    $dict{"departamento_local"} = $3;
    $dict{"denominacion_programa"} = $4;
  } else {
    print "<h1></h1>\n";
  }
  return %dict;
}

# Subrutina para verificar si hay coincidencias en los campos.
sub matchFields {
  my ($dict, $keyword) = @_;
  foreach my $field (keys %$dict) {
    if ($dict->{$field} =~ /.*$keyword.*/) {
      return 1; # Coincidencia encontrada
    }
  }
  return 0; # No se encontraron coincidencias
}
