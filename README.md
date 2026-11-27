# Sistema de gestión académica

Aplicación de consola en Python para registrar profesores, aprendices, cursos, inscripciones y calificaciones. El taller se desarrolla sin framework y usa almacenamiento temporal en memoria. Al cerrar la aplicación se pierden los registros de la sesión.

| Integrante | GitHub |
|---|---|
| Camilo Andrés Tamayo Durán | `copito111` |
| Santiago Ortiz Claros | `Ortiz-png` |

## Cómo usarlo

Abre una terminal en la carpeta del proyecto y ejecuta:

```powershell
py main.py
```

Si tu equipo usa el comando `python`, ejecuta `python main.py`.

Desde el menú puedes registrar profesores y aprendices, crear cursos y hacer inscripciones. En el panel del profesor puedes ver sus cursos, registrar notas y consultar promedios e informes.

## Ejemplo rápido

Registra a un profesor y a un aprendiz. Crea un curso, asígnalo al profesor e inscribe al aprendiz. Luego entra al panel con el documento del profesor y registra las notas `2`, `3` y `4`. El informe debe mostrar `3.00` y el resultado **Aprobado**.

## Pruebas

En [Pruebas.md](Pruebas.md) dejamos los pasos para repetir las pruebas, los resultados que obtuvimos y los errores que resolvimos durante el taller.
