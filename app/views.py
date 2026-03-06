from django.shortcuts import render

CERTIFICADOS = [
    {
        "documento": "12345678",
        "codigo": "ABC123",
        "nombre": "Juan Perez",
        "curso": "Python",
        "fecha": "2026"
    },
    {
        "documento": "30111222",
        "codigo": "SIU2026",
        "nombre": "Maria Lopez",
        "curso": "Bases de Datos",
        "fecha": "2025"
    }
]

def validador(request):
    if request.method == "POST":
        documento = request.POST.get("documento", "").strip()
        codigo = request.POST.get("codigo", "").strip().upper()

        for cert in CERTIFICADOS:
            if cert["documento"] == documento and cert["codigo"].upper() == codigo:
                return render(request, "valido.html", {
                    "resultado": cert
                })

        return render(request, "home.html", {
            "error": "No se encontró ningún certificado con esos datos."
        })

    return render(request, "home.html")