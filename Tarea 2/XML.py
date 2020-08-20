from xml.dom import minidom
def valiokk():

    Doc = minidom.parse('XMLTXT.xml')
    reg = Doc.getElementsByTagName("Persona")

    for F in reg:
        nombre = F.getElementsByTagName("name")[0]
        edad = F.getElementsByTagName("age")[0]
        activo = F.getElementsByTagName("active")[0]
        years = F.getElementsByTagName("year")[0]

        print(f"    Nombre:", nombre.firstChild.data, f"    Edad:", edad.firstChild.data,f"    Activo:", activo.firstChild.data ,f"    Año:", years.firstChild.data)
valiokk()