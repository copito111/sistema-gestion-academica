# Sistema de gestión académica

Aplicación de consola en Python para registrar profesores, aprendices, cursos, inscripciones y calificaciones. El taller se desarrolla sin framework y usa almacenamiento temporal en memoria. Al cerrar la aplicación se pierden los registros de la sesión.

| Integrante | GitHub |
|---|---|
| Camilo Andrés Tamayo Durán | `copito111` |
| Santiago Ortiz Claros | `Ortiz-png` |

## 1. Abrir y probar la plantilla

En PowerShell, entren a la carpeta que contiene este README y ejecuten:

```powershell
py --version
git --version
py main.py
```

Si el comando de su equipo es `python`, usen `python main.py`. El menú inicial muestra cinco secciones. Las opciones `1` a `5` indican qué falta programar, y `0` cierra el programa. `modelos/persona.py` contiene el contrato abstracto inicial. Los demás módulos incluyen una indicación de lo que deben implementar.

## 2. Poner la plantilla en GitHub

1. **Camilo** crea `sistema-gestion-academica` desde `copito111`, con `Add README` activado y `main` como rama inicial. Invita a `Ortiz-png` en **Settings → Collaborators → Add people**. Si ya existe el repositorio, úselo. [Crear un repositorio](https://docs.github.com/en/repositories/creating-and-managing-repositories/creating-a-new-repository) · [Invitar colaboradores](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/repository-access-and-collaboration/inviting-collaborators-to-a-personal-repository)
2. **Santiago** acepta la invitación. Ambos clonan el repositorio en su computador. Ejecuten `git clone` desde la carpeta donde guardarán su copia de trabajo. Si la plantilla está descomprimida allí con el mismo nombre, usen otra carpeta para clonar.

   ```powershell
   git clone https://github.com/copito111/sistema-gestion-academica.git
   cd sistema-gestion-academica
   git config user.name "Tu nombre completo"
   git config user.email "Tu correo asociado a GitHub o tu correo noreply"
   ```

3. **Camilo** prepara `develop`. Si todavía no existe, ejecute `git switch main` y `git switch -c develop`. Si ya existe en GitHub, ejecute `git switch develop` y `git pull --ff-only origin develop`. Desde el explorador, copie `main.py`, `README.md`, `modelos/`, `servicios/` y `almacenamiento/` de la plantilla a la raíz del clon. Puede incluir `.gitignore` si el clon aún no lo tiene. Si el README existente contiene instrucciones del curso, incorpórelas antes de reemplazarlo. Luego ejecute:

   ```powershell
   py main.py
   git status
   git add main.py README.md modelos servicios almacenamiento
   git add .gitignore
   git commit -m "Agregar estructura inicial del sistema académico"
   git push -u origin develop
   ```

4. **Santiago** ejecuta `git fetch origin` y `git switch develop`. Si ya tenía `develop` en su computador, ejecuta también `git pull --ff-only origin develop`. Los dos prueban `py main.py` desde sus respectivos clones. Desde aquí, editan sus clones.

## 3. Programar por etapas

| Orden | Responsable | Rama | Tarea y prueba antes del PR |
|---|---|---|---|
| 0 | Ambos. Camilo sube el cambio | `develop` | Completar `Persona` con nombre, documento y edad privados, propiedades y validaciones. Acordar los contratos mínimos de almacenamiento y su implementación con diccionarios. |
| 1a | Camilo | `feature/gestion-profesores` | Completar `Profesor` con profesión, código y especialidad. Implementar registro, listado y búsqueda por documento. Probar documento o código repetido. |
| 1b | Santiago | `feature/gestion-aprendices` | Completar `Aprendiz` con datos de contacto. Implementar registro, listado y búsqueda por documento. Probar documento repetido y búsqueda de un documento inexistente. |
| 2 | Camilo | `feature/gestion-cursos` | Implementar `Curso` con código, nombre, descripción, duración en horas y modalidad. Registrar ambas modalidades, asignar un profesor existente y consultar cursos por código y por profesor. |
| 3 | Santiago | `feature/inscripciones` | Vincular aprendiz y curso, guardar fecha y estado y evitar duplicados por la pareja documento–código. Consultar los cursos de un aprendiz y los inscritos de un curso. Probar ambos sentidos de la relación. |
| 4 | Santiago, luego Camilo | `feature/calificaciones` | Santiago implementa `Calificacion` y el registro, modificación y consulta de notas por inscripción. Luego Camilo implementa promedios, informes por curso y por aprendiz y las opciones del profesor. Ambos hacen sus propios commits. |

### Primer día de programación

1. **Juntos**, abran `modelos/persona.py`. Diseñen el constructor con `nombre`, `documento` y `edad`. Traten el documento como texto para conservar ceros iniciales. Definan cómo validarán datos vacíos y una edad inválida. Mantengan `mostrar_informacion()` y `obtener_rol()` como métodos abstractos que las subclases deben implementar con retorno de texto.
2. **Juntos**, abran `almacenamiento/contratos.py` y `memoria.py`. Definan un contrato de lectura con `buscar(clave)` y `listar()`, y uno de escritura con `guardar(clave, entidad)`. Escriban una implementación con un diccionario por repositorio. Usen instancias independientes para profesores, aprendices, cursos e inscripciones. Acuerden que `buscar` devuelve `None` cuando la clave falta. Camilo sube esta base a `develop` y Santiago la descarga.
3. **Camilo** crea `feature/gestion-profesores`, abre `modelos/profesor.py`, hereda de `Persona` y llama a `super().__init__` para los campos comunes. Escribe primero una prueba manual que construya un profesor y llame `obtener_rol()`. Después incorpora `registrar_profesor`, `buscar_profesor` y `listar_profesores` en `GestionAcademica`. Conecta esas operaciones con la opción `1` del menú.
4. **Santiago** crea `feature/gestion-aprendices`, abre `modelos/aprendiz.py` y sigue el mismo orden con su entidad. Implementa `registrar_aprendiz`, `buscar_aprendiz` y `listar_aprendices`. Puede avanzar en su modelo mientras Camilo integra profesores. Antes de tocar los archivos compartidos, incorpora `develop` y conecta la opción `2` del menú.
5. Para las siguientes funcionalidades, repitan el orden **modelo → reglas en el servicio → menú → prueba manual → PR**. Integren profesores y aprendices antes de abrir cursos. Luego integren cursos antes de inscripciones e inscripciones antes de calificaciones.

### Reglas para implementar y explicar en la entrega

- **Cursos.** Mantengan un catálogo con las modalidades de formación titulada y complementaria. El menú debe listar las opciones desde ese catálogo. Validen código único, duración positiva y profesor existente.
- **Inscripciones.** Usen `(documento_aprendiz, codigo_curso)` como clave. Consulten esa colección por cualquiera de las dos partes. Empiecen con estado `activa` y acuerden cómo cambiar a `cancelada`.
- **Calificaciones.** Cada inscripción tiene su colección de notas. Acepten números finitos de `0.0` a `5.0`. Con menos de tres notas, muestren `Pendiente`. Con tres o más, calculen el promedio, aprueben desde `3.0` y muestren dos decimales. Permitan modificar una nota existente y revisen que el profesor tenga asignado el curso antes de registrar o modificar sus notas.
- **POO.** Usen atributos privados y propiedades. Mantengan `Persona` abstracta. Demuestren herencia y polimorfismo llamando los mismos métodos con objetos `Profesor` y `Aprendiz`.
- **SOLID.** Separen entidades, consola y almacenamiento. Extiendan modalidades desde el catálogo. Permitan usar ambas subclases como `Persona` respetando su contrato. Separen los contratos por operación. Inyecten los repositorios en `GestionAcademica` desde `main.py` mediante esos contratos.

## 4. Crear una rama y subir un PR

Ejemplo de Camilo para profesores. Cambien el nombre de la rama según la tabla.

```powershell
git switch develop
git pull --ff-only origin develop
git switch -c feature/gestion-profesores
```

Cuando la funcionalidad esté probada:

```powershell
git status
git add modelos/profesor.py servicios/gestion_academica.py main.py
git diff --cached
git commit -m "Implementar registro y consulta de profesores"
git push -u origin feature/gestion-profesores
```

Ajusten `git add` a los archivos que realmente modificaron. En GitHub, abran un PR con **base `develop`** y **compare su rama `feature/...`**. El compañero revisa los cambios y prueba la funcionalidad antes de integrarla. Si `develop` avanzó, ejecuten `git fetch origin` y `git merge origin/develop` desde su rama, resuelvan los conflictos que aparezcan y repitan la prueba. [Crear un pull request](https://docs.github.com/en/pull-requests/how-tos/create-pull-requests/creating-a-pull-request)

Para la rama compartida `feature/calificaciones`, Santiago crea y publica la rama primero. Camilo espera a que Santiago suba sus cambios, ejecuta `git fetch origin` y `git switch --track origin/feature/calificaciones`, agrega su trabajo y hace su propio commit y `git push`. Revisan juntos los cambios y abren un solo PR para esa rama.

## 5. Verificar y entregar

- [ ] Registrar y buscar dos profesores, dos aprendices y dos cursos de modalidades distintas.
- [ ] Inscribir un aprendiz en ambos cursos y otro en uno. Consultar las relaciones en ambos sentidos y rechazar una repetición.
- [ ] Probar notas `0.0`, `5.0`, `-0.1` y `5.1`. Registrar `2.0`, `3.0` y `4.0`. Ver `3.00` y `Aprobado`. Cambiar `4.0` por `1.0` y ver `2.00` y `Reprobado`.
- [ ] Consultar los cursos e inscritos del profesor. Comprobar que pueda operar únicamente sobre sus cursos y generar los informes por curso y por aprendiz.
- [ ] Salir y volver a iniciar. Comprobar que los datos de la sesión anterior se hayan perdido.
- [ ] Actualizar este README con un ejemplo real de uso y apuntar a las clases o métodos donde aplicaron POO y SOLID.
- [ ] Abrir el PR final con **base `main`** y **compare `develop`**. Conservar las cinco ramas de funcionalidad hasta la revisión. Confirmar que el docente pueda abrir el repositorio y entregar el enlace.
