from Test_logins import Login
from Test_search import Search
from Test_follow import Follow
from Test_historia import Historia
from Test_like import Like


prueba1 = Login.PruebaSucces()
prueba2 = Login.PruebaFailure()
prueba3 = Search.Prueba()
prueba4 = Follow.Prueba()
prueba5 =  Like.Prueba()
prueba6 =  Historia.Prueba()


from jinja2 import Template
import io

template = Template("""
<!DOCTYPE html>
<html lang="es">
<link>
    <meta charset="UTF-8">
    <title>Plantilla HTML en Python</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <div>
        <h2 class="success">Prueba numero 1:  Inicio de sesion exitoso</h2>
        <p>Se demoro en esta prueba : {{prueba1}}seg</p>

    </div>

    <div>
        <h2 class="failure">Prueba numero 2: Inicio de sesion fallido</h2>
        <p>Se demoro en esta prueba : {{prueba2}}seg</p>
    </div>

    <div>
        <h2 class="success">Prueba numero 3:  Probar la funcionalidad de "search"</h2>
        <p>Se demoro en esta prueba : {{prueba3}}seg</p>

    </div>

    <div>
        <h2 class="success">Prueba numero 4:  Probar la funcionalidad de "seguir"</h2>
        <p>Se demoro en esta prueba : {{prueba4}}seg</p>

    </div>

    <div>
        <h2 class="success">Prueba numero 5:  Probar funcionalidad de "like"</h2>
        <p>Se demoro en esta prueba : {{prueba5}}seg</p>

    </div>

    <div>
        <h2 class="success">Prueba numero 6: Ver una historia</h2>
        <p>Se demoro en esta prueba : {{prueba6}}seg</p>

    </div>

</body>
</html>
""")


html = template.render(prueba1 = prueba1, prueba2 = prueba2, prueba3 = prueba3, prueba4 = prueba4, prueba5 = prueba5, prueba6 = prueba6)

with io.open("reporte.html", "w") as f:
    f.write(html)