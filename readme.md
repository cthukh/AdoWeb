# HoloWeb

HoloWeb es una aplicación web para consultar y administrar un directorio de talentos de Hololive. Cada perfil reúne información básica del miembro para que la comunidad pueda explorar sus generaciones, estado y trayectoria.

## Funcionalidades

- Listado de Holomiembros con filtros por generación y estadísticas de activos e inactivos.
- Vista de detalle con nombre, generación, estado, cantidad de seguidores en YouTube, fecha de debut y descripción.
- Inicio de sesión para acceder a las acciones de administración.
- Creación, edición y eliminación de perfiles para usuarios autenticados.
- Formularios con validación y confirmación antes de eliminar un perfil.

## Información gestionada

Cada miembro tiene nombre, descripción opcional, cantidad de seguidores en YouTube, fecha de debut y estado activo/inactivo. También puede asociarse a una generación. Las generaciones se mantienen como registros independientes para agrupar los perfiles.

## Tecnologías

- Python y Django.
- Django Templates y Bootstrap 5.3 para la interfaz.
- CSS propio para la identidad visual de HoloWeb.

## Puesta en marcha

Con Python y `pip` disponibles, instala las dependencias y prepara la base de datos:

```bash
pip install -r requirements.txt
python manage.py migrate
```

Para acceder a las acciones protegidas, crea un usuario administrador:

```bash
python manage.py createsuperuser
```

Inicia el servidor de desarrollo:

```bash
python manage.py runserver
```

Abre `http://127.0.0.1:8000/` en el navegador.
