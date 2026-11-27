# Sistema de gestión académica

Aplicación de consola en Python para gestionar profesores, aprendices, cursos, inscripciones y calificaciones. Usa la biblioteca estándar y almacena los datos en memoria durante la ejecución. Cada reinicio comienza con los registros vacíos.

| Integrante | GitHub | Aportes |
|---|---|---|
| Camilo Andrés Tamayo Durán | `copito111` | Profesores, cursos, promedios e informes y consultas del panel del profesor. |
| Santiago Ortiz Claros | `Ortiz-png` | Aprendices, inscripciones y registro, modificación y consulta de notas. |

## Ejecutar

Se requiere Python 3.10 o posterior. Desde la carpeta que contiene `main.py`, ejecuten:

```powershell
py main.py
```

Si en su equipo el comando es `python`, ejecuten `python main.py`. En el menú principal las opciones `1` a `5` abren Profesores, Aprendices, Cursos, Inscripciones y Panel del profesor. En los submenús, `0` vuelve al menú principal. En el menú principal, `0` cierra la aplicación.

## Resultado de la verificación

El recorrido se ejecutó en una copia temporal de los archivos de la rama local `feature/calificaciones`. Se enviaron entradas al programa de consola y se comprobaron los mensajes y resultados. Se usaron datos ficticios. Los números de la tabla cuentan comprobaciones sobre la salida, que incluyen resultados esperados y mensajes de rechazo.

| Etapa | Comprobaciones de salida | Resultado |
|---|---:|---|
| Menú inicial | 2 | Pasó |
| Profesores | 7 | Pasó |
| Aprendices | 7 | Pasó |
| Cursos | 8 | Pasó |
| Inscripciones | 10 | Pasó |
| Calificaciones, panel e informes | 21 | Pasó |
| Reinicio y almacenamiento temporal | 3 | Pasó |
| **Total** | **58** | **Pasó** |

También se comprobó directamente que `Persona` es abstracta, que `Profesor` y `Aprendiz` respetan su contrato y que dos repositorios en memoria mantienen sus datos separados.

## Datos para repetir las pruebas

Registren los datos siguientes en **una sola sesión**. Los documentos son texto y conservan los ceros iniciales.

### Profesores · `1 → 1`

| Nombre | Documento | Edad | Profesión | Código | Especialidad |
|---|---|---:|---|---|---|
| Lina | `001` | `32` | Ingeniera | `P01` | Python |
| Ana | `003` | `35` | Ingeniera | `P02` | Redes |

### Aprendices · `2 → 1`

| Nombre | Documento | Edad | Contacto |
|---|---|---:|---|
| Mateo | `002` | `20` | `mateo@example.com` |
| Sara | `004` | `22` | `sara@example.com` |

### Cursos · `3 → 1`

| Código | Nombre | Descripción | Horas | Modalidad | Documento del profesor |
|---|---|---|---:|---|---|
| `C01` | Python básico | Curso Python | `40` | `1` · Formación titulada | `001` |
| `C02` | Redes básicas | Curso Redes | `20` | `2` · Formación complementaria | `003` |

En el campo de modalidad se ingresa `1` o `2`. En el campo del profesor se escribe su documento, como `001`.

### Inscripciones · `4 → 1`

| Documento del aprendiz | Código del curso |
|---|---|
| `002` | `C01` |
| `002` | `C02` |
| `004` | `C01` |

Para reproducir el error **`Inscripción no encontrada.`**, intenten registrar una nota después de crear el aprendiz y el curso, antes de registrar esa pareja. Después registren la inscripción y repitan la operación sin cerrar el programa.

## Pruebas por funcionalidad

Para repetir las etapas por separado, vuelvan a cargar los datos de ejemplo al iniciar cada sesión. Si continúan desde la prueba de cambio de estado, reactiven la inscripción `002`–`C01` antes de registrar las notas.

### Menú inicial y personas

| Caso | Cómo se probó | Resultado observado |
|---|---|---|
| Menú inicial | Ingresar `9` y luego `0`. | Aparece `Opción inválida.` y luego `Hasta luego.` |
| Registro, listado y búsqueda de profesores | Registrar a Lina y Ana. En Profesores, elegir `2` para listar y `3` para buscar `001`. | Aparecen ambos en el listado y Lina al buscar `001`. |
| Validaciones de profesores | Repetir el documento `001` con otro código. Repetir `P01` con otro documento. Intentar registrar edad `0`. | Se rechazan el documento repetido, el código repetido y la edad inválida. |
| Profesor inexistente | Buscar `999` en Profesores. | `Profesor no encontrado.` |
| Registro, listado y búsqueda de aprendices | Registrar a Mateo y Sara. En Aprendices, elegir `2` para listar y `3` para buscar `002`. | Aparecen ambos en el listado y se muestra el contacto de Mateo al buscarlo. |
| Validaciones de aprendices | Repetir el documento `002`, buscar `999` e intentar registrar un contacto vacío. | Se rechaza el duplicado, se informa que el aprendiz no existe y se pide un contacto obligatorio. |

### Cursos

| Caso | Cómo se probó | Resultado observado |
|---|---|---|
| Modalidades y asignación | Crear `C01` con modalidad `1` y profesor `001`, y `C02` con modalidad `2` y profesor `003`. Listar con la opción `2`. | Aparecen Formación titulada y Formación complementaria, con sus profesores responsables. |
| Consultar por código | En Cursos, elegir `3` y buscar `C01`. Repetir con `C99`. | Se muestra `C01` y se informa que `C99` no existe. |
| Consultar por profesor | En Cursos, elegir `4` e ingresar `001`. | Aparece `C01`, el curso asignado a Lina. |
| Reglas de registro | Intentar repetir `C01`, asignar al profesor `999`, ingresar el texto `Formacion titulada` como modalidad y probar duraciones `0` y `3.5`. | Cada intento se rechaza por su regla correspondiente. |

### Inscripciones

| Caso | Cómo se probó | Resultado observado |
|---|---|---|
| Cursos por aprendiz | En Inscripciones, elegir `3` e ingresar `002`. | Mateo aparece en `C01` y `C02`. |
| Aprendices por curso | En Inscripciones, elegir `4` e ingresar `C01`. | Aparecen Mateo (`002`) y Sara (`004`). |
| Duplicados | Volver a registrar `002` en `C01`, primero activa y luego cancelada. | Se conserva una sola inscripción por pareja documento–código. |
| Registros inexistentes | Intentar inscribir a `999` en `C01` y a `002` en `C99`. | Se informa que falta el aprendiz o el curso, respectivamente. |
| Fecha y estado | Consultar `002`–`C01`, cambiarla con la opción `2` a `cancelada` y volver a consultar. Probar luego un estado inválido. | La fecha queda igual, el estado cambia a `cancelada` y el valor inválido se rechaza. |

### Calificaciones e informes

En el menú principal, abran **`5` Panel del profesor** con el documento `001`. Las operaciones de notas piden primero el código del curso y luego el documento del aprendiz.

| Paso | Opción del panel | Entrada en orden | Resultado observado |
|---|---|---|---|
| 1 | `1` Registrar nota, dos veces | `C01`, `002`, `2`. Después `C01`, `002`, `3`. | Se guardan ambas notas. |
| 2 | `6` Informe por curso | `C01` | Mateo aparece con dos notas y estado `Pendiente`. |
| 3 | `1` Registrar nota | `C01`, `002`, `4` | Se guarda la tercera nota. |
| 4 | `3` Consultar notas y `6` Informe por curso | Para `3`, `C01`, `002`. Para `6`, `C01`. | Aparecen `2`, `3` y `4`. El promedio es `3.00` y el resultado es `Aprobado`. |
| 5 | `2` Modificar nota | `C01`, `002`, `3`, `1` | Se reemplaza la nota de la posición `3` por `1`. |
| 6 | `3` Consultar notas y `7` Informe por aprendiz | Para `3`, `C01`, `002`. Para `7`, `002`. | Aparecen `2`, `3` y `1`. El promedio es `2.00` y el resultado es `Reprobado`. El informe de Lina muestra `C01`. |

Fragmentos de salida comprobados durante el recorrido:

```text
Notas 1) 2, 2) 3 | Pendiente
Promedio 3.00 | Aprobado
Nota actualizada.
Nota 1: 2
Nota 2: 3
Nota 3: 1
Promedio 2.00 | Reprobado
```

Para repetir las validaciones adicionales, utilicen las inscripciones existentes:

| Caso | Cómo se probó | Resultado observado |
|---|---|---|
| Límites y formato decimal | Registrar `0.0`, `5.0` y `3,5` para Sara (`004`) en `C01`. | Se aceptan los límites y la consulta muestra `3.5` para la nota ingresada con coma. |
| Valores inválidos | Intentar registrar `-0.1`, `5.1`, `NaN` y `texto`. | Se rechazan los valores fuera del rango, los no finitos y el texto. |
| Posición inválida | Elegir `2` y escribir `C01`, `002`, `9`, `4`. | `Esa posición de nota no existe.` Las notas válidas siguen disponibles para consulta. |
| Inscripción sin crear | Intentar registrar una nota para `002`–`C01` antes de inscribir a Mateo. | `Inscripción no encontrada.` Una vez creada la inscripción, la nota se guarda. |
| Inscripción cancelada | Cambiar `002`–`C01` a `cancelada` y volver al panel de Lina. Intentar agregar una nota y luego consultar. | Se rechaza el registro y se pueden consultar las notas existentes. |
| Cursos e inscritos del profesor | En el panel de Lina, elegir `4` para ver sus cursos y `5` con `C01` para ver inscritos. | Lina ve `C01` y, dentro de ese curso, ve a Mateo y a Sara. |
| Curso de otro profesor | En el panel de Lina, intentar ver inscritos, consultar el informe o cargar una nota en `C02`, que corresponde a Ana. | `El curso no está asignado a ese profesor.` El informe por aprendiz de Lina también omite `C02`. |

### Reinicio y almacenamiento temporal

1. Salir del panel con `0` y cerrar el programa con `0` desde el menú principal.
2. Volver a ejecutar `py main.py`.
3. Listar profesores, aprendices y cursos. Los listados comienzan vacíos.
4. Intentar entrar al panel con `001`. Aparece `Profesor no encontrado.` porque los registros de la ejecución anterior ya se perdieron.

## Incidencias encontradas durante el desarrollo

| Incidencia | Corrección y comprobación |
|---|---|
| `ImportError` al importar `RepositorioEnMemoria`. | Se completaron `almacenamiento/memoria.py`, `almacenamiento/contratos.py` y `modelos/persona.py`. Se volvió a abrir el menú y se registró, listó y buscó un profesor. |
| `La modalidad seleccionada no existe.` al escribir el nombre de la modalidad. | La opción de consola utiliza `1` o `2`. Se comprobó el rechazo del texto y el registro con ambos valores válidos. |
| `GestionAcademica() takes no arguments`. | Se corrigió el nombre del constructor a `__init__` y se usaron los mismos atributos privados que consultan los métodos. Se reprodujo el fallo con el archivo original y se verificó el arranque con el archivo corregido. |
| Error de atributo en `__inscripcion_editable` y error de `NoneType` al guardar una nota. | Se dejó un único método dentro de `GestionAcademica`, con los nombres de las llamadas correctos y `return inscripcion` fuera del `if`. Se comprobó el registro, la edición y la consulta posterior. |
| `Inscripción no encontrada.` durante la prueba de Camilo. | Se verificó que la pareja `002`–`C01` debe existir en la sesión actual. Tras inscribir a Mateo, la misma nota se guardó y se pudo consultar. |
| `git switch develop` bloqueado por cambios locales de cursos. | Se guardaron los archivos de cursos temporalmente antes de cambiar de rama. El trabajo quedó asociado a `feature/gestion-cursos`. |
| `src refspec feature/inscripciones does not match any`. | El commit de inscripciones estaba en `develop` local. Se creó `feature/inscripciones` a partir de ese commit y se comprobó que la rama quedó publicada en GitHub. |

## Organización y criterios de diseño

- [main.py](main.py) contiene los menús y conecta los repositorios en memoria con el servicio. [GestionAcademica](servicios/gestion_academica.py) coordina las reglas del sistema y [los informes](servicios/informes.py) calculan y formatean los resultados académicos.
- [Persona](modelos/persona.py) usa `ABC`, métodos abstractos y atributos privados consultables mediante propiedades. [Profesor](modelos/profesor.py) y [Aprendiz](modelos/aprendiz.py) heredan el contrato. El menú llama `mostrar_informacion()` de la misma forma para cada clase y obtiene el texto correspondiente.
- [Curso](modelos/curso.py) consulta un catálogo de modalidades. Para incorporar otra modalidad, el catálogo es el punto de extensión que comparten el menú y el modelo.
- [Los contratos de almacenamiento](almacenamiento/contratos.py) separan lectura y escritura. `GestionAcademica` recibe los repositorios por constructor. [La implementación en memoria](almacenamiento/memoria.py) utiliza un diccionario por repositorio.
- Las ramas del taller son `main`, `develop`, `feature/gestion-profesores`, `feature/gestion-aprendices`, `feature/gestion-cursos`, `feature/inscripciones` y `feature/calificaciones`. La rama de calificaciones reúne el trabajo de Santiago en notas y el de Camilo en promedios, informes y panel.
