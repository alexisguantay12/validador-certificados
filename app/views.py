from django.shortcuts import render

CERTIFICADOS = [
    {
        "documento": "40899934",
        "codigo": "25122321551882",
        "nombre": "Alexis Ramon Guantay",
        "materia": "Desarrollo de Software",
        "fecha": "17/12/2025",
        "pdf": 'pdf/certificado_desarrollosoftware.pdf'
    },
    {
        "documento": "40899934",
        "codigo": "122521551993",
        "nombre": "Alexis Ramon Guantay",
        "materia": "Analisis y Diseño de Sistemas de Informacion 2",
        "fecha": "03/03/2026",
        "pdf": "pdf/certificado_adsi2.pdf"
    }
]


def validador(request):

    # datos para autocompletar desde QR
    dni = request.GET.get("dni", "")
    solicitud = request.GET.get("solicitud", "")

    if request.method == "POST":

        documento = request.POST.get("documento")
        codigo = request.POST.get("codigo")

        for cert in CERTIFICADOS:

            if cert["documento"] == documento and cert["codigo"] == codigo:

                return render(request, "valido.html", {
                    "cert": cert,
                    "pdf": cert["pdf"]
                })

        return render(request, "home.html", {
            "error": "No se encontró ningún certificado con esos datos.",
            "dni": documento,
            "solicitud": codigo
        })

    return render(request, "home.html", {
        "dni": dni,
        "solicitud": solicitud
    })