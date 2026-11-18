# Bitácora RTCF

## 1. Acceso y navegación autenticada

**Rol**  
Actúa como diseñador front-end senior, experto en plantillas Django, autenticación y Bootstrap 5.3, manteniendo la coherencia visual de HoloWeb.

**Tarea**  
Crea `login.html`, agrega controles de iniciar y cerrar sesión en el navbar, y muestra las acciones de agregar y editar solo cuando el usuario tenga sesión iniciada.

**Contexto**  
Usa `LoginView` con el formulario `AuthenticationForm` (`username` y `password`), las URLs `login`, `logout`, `home`, `agregar_miembro` y `editar_miembro`. El cierre de sesión debe ser un formulario POST con CSRF. No se deben modificar archivos Python.

**Formato**  
Extiende `base.html`, conserva navbar y footer globales, renderiza el formulario automáticamente, incluye CSRF y `next`, y agrega los estilos necesarios a `base.css`, sin CSS inline ni JavaScript.

**Resultado**  
Se creó la pantalla de login y se adaptó el navbar para distinguir usuarios autenticados y visitantes, incluyendo logout seguro por POST y estilos responsive.

## 2. Confirmación para eliminar un Holomiembro

**Rol**  
Actúa como diseñador front-end senior, experto en plantillas Django y Bootstrap 5.3, priorizando la coherencia con el sitio y la reutilización de estilos.

**Tarea**  
Crea `eliminar_miembro.html` como pantalla de confirmación y agrega un botón «Eliminar» al detalle del miembro.

**Contexto**  
El objeto se recibe como `holo`; la confirmación envía POST a `{% url 'eliminar_miembro' holo.id %}` con CSRF, y cancelar vuelve a `{% url 'detalle_miembro' holo.id %}`. El botón del detalle solo aparece para usuarios autenticados. No se modifican archivos Python.

**Formato**  
Extiende `base.html`, reutiliza la tarjeta y las clases existentes, presenta una advertencia accesible y botones «Sí, eliminar» y «Cancelar». Los estilos de peligro van en `base.css`; no uses enlaces para ejecutar el borrado ni JavaScript.

**Resultado**  
Se añadió una confirmación accesible que elimina mediante POST, junto con el botón protegido en el detalle y una variante de peligro coherente con la paleta del sitio.
