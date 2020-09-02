import re
import Prueba as pb
import webbrowser
temporal = []
comp = []
EsteEsElFin = []
def Run():
    contador = 0
    temporal = pb.jsonread()
    tamaño = len(temporal)
    for A in range(0, len(temporal)):
        simple = str(temporal[A])
        CorcheteU = re.sub('{', '', simple)
        CorcheteD = re.sub('}', '', CorcheteU)
        SinComillas = re.sub("'", "", CorcheteD)
        comp.append(SinComillas)
    EsteEsElFin = comp
    with open('ArchivoHTML.txt', 'w') as F:
        for T in EsteEsElFin:
            if contador <= 10:
                contador = contador + 1
                F.write('REGISTRO' +  str(contador) + '\n')
                F.write(str(T) + '\n')
                F.write('\n')
        F.close()
        pass

        f = open('Reporte.html', 'wb')
        mensaje = """<!DOCTYPE html>
                        <html lang="es">
                        <head>
                            <meta charset="UTF-8">
                            <meta name="viewport" content="width=device-width, initial-scale=1.0">
                            <title>SIMPLEQL</title>
                            <link rel="icon" href="logoPython.png">
                            <link href="https://fonts.googleapis.com/css2?family=Limelight&display=swap" rel="stylesheet">
                            <link href="https://fonts.googleapis.com/css2?family=IM+Fell+DW+Pica+SC&display=swap" rel="stylesheet">
                            <link href="https://fonts.googleapis.com/css2?family=Alata&display=swap" rel="stylesheet">
                            <link rel="stylesheet" href="estilo.css">
                        </head>
                        <body>
                        <div class="contenedor">
                            <center>
                            <header class="fila">
                                <center><div id="logo" class="col-lg-12 col-md-12 col-sm-13 col-xs-12"><img src="asd-removebg-preview.png" height="60">
                                SIMPLEQL</div></center>
                            </header>
                            </center>
                            <section id="seccion4" class="fila">
                                <aside id="izq" class="col-lg-3 col-md-3 col-sm-3 col-xs-12">
                                </aside>
                                <article class="col-lg-6 col-md-6 col-sm-6 col-xs-12">
                                    <center><h1>Reporte de Registros</h1></center>
                                    <center><iframe src="ArchivoHTML.txt" width="620"  style="border: solid;" title="REPORTE DE REGISTROS"></iframe></center>
                                </article>
                                <aside id="der" class="col-lg-3 col-md-3 col-sm-3 col-xs-12">
                                </aside>
                            </section>
                            <footer class="fila">
                                <div class="col-lg-12 col-md-12 col-sm-12 col-xs-12">&reg;201901907, BYRON ESTUARDO CAAL CATÚN</div>
                            </footer>
                        </div>
                        </body>
                        </html>""".encode()
        f.write(mensaje)
        f.close()
        webbrowser.open_new_tab('Reporte.html')
Run()