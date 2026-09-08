# Taller-mecanico-
Repositorio oficial y bitácora de seguimiento para el módulo *Taller Mecánico 114-2A-F2*.

---

## 📋 Información General

- *Módulo / Asignatura:* Taller Mecánico 114-2A-F2
- *Institución / Sede:* [Completar]
- *Docente / Instructor:* [Completar]
- *Integrantes:*
  - Estudiante 1
  - Estudiante 2
- *Periodo Académico:* 2026

---

## 🎯 Objetivos del Módulo

- Desarrollar habilidades prácticas y teóricas en diagnóstico, mantenimiento y reparación de sistemas mecánicos automotrices.
- Aplicar normas de seguridad, higiene industrial y uso correcto de Elementos de Protección Personal (EPP) en taller.
- Documentar de manera sistemática y continua las actividades, aprendizajes y resoluciones técnicas en esta bitácora.

---

## 📖 Bitácora de Actividades / Registro de Sesiones

| N° Sesión | Fecha | Tema / Actividad Realizada | Responsable(s) | Observaciones / Resultados | Estado |
| :---: | :---: | :--- | :--- | :--- | :---: |
| *01* | 07/09/2026 | Inicialización del repositorio y desarrollo de la clase base `Vehiculo` en `vehiculo.py` (atributos tipados, constructor `__init__`, métodos `ingresar()` y `entregar()`) | Equipo | Código documentado línea por línea, probado y sincronizado en GitHub | ✅ Completado |
| *02* | DD/MM/AAAA | [Descripción de la actividad] | [Nombre] | [Observaciones] | ⏳ Pendiente |
| *03* | DD/MM/AAAA | [Descripción de la actividad] | [Nombre] | [Observaciones] | ⏳ Pendiente |

---

### 🚗 Implementación Técnica (`vehiculo.py`)

Se diseñó la clase orientada a objetos `Vehiculo` para la gestión del taller:
- **Atributos de instancia:**
  - `patente: str` (identificador en texto).
  - `annio: int` (año de fabricación del vehículo).
  - `en_taller / _en_taller: bool` (estado de permanencia en taller).
- **Constructor (`__init__`):** Inicializa los atributos con soporte de tipos y valor por defecto `en_taller = True`.
- **Métodos de estado:**
  - `ingresar()`: Cambia `_en_taller` y `en_taller` a `True`.
  - `entregar()`: Cambia `_en_taller` y `en_taller` a `False`.
- **Documentación:** Comentarios explicativos detallados en cada línea de código.

---

## 🛡️ Normas de Seguridad y EPP Obligatorio

1. *Uso obligatorio de EPP:* Overol/ropa de trabajo, calzado de seguridad, gafas protectoras y guantes adecuados según la labor.
2. *Orden y Limpieza:* Mantener el área de trabajo y las herramientas limpias y ordenadas al finalizar cada jornada (metodología 5S).
3. *Manejo de Residuos:* Disposición correcta de aceites usados, refrigerantes y materiales contaminados en los contenedores designados.
4. *Reporte de Incidentes:* Informar inmediatamente al docente o supervisor de cualquier desperfecto, incidente o situación de riesgo.

---

## 📂 Estructura del Repositorio

```text
Taller-mecanico-/
├── README.md               # Bitácora principal e información del módulo
├── vehiculo.py             # Clase base Vehiculo con constructor y métodos ingresar()/entregar()
├── docs/                   # Guías de taller, manuales técnicos y apuntes
└── informes/               # Reportes y evaluaciones prácticas
```

---

## 📌 Notas y Pendientes

- [ ] Completar la nómina de integrantes del grupo.
- [x] Registrar la primera sesión de taller y creación de la clase `Vehiculo`.
- [ ] Subir pautas o guías entregadas por el docente.
