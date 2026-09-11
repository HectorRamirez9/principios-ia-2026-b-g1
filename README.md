# Principios de Inteligencia Artificial - 2026-B

Repositorio de clase - Corporacion Universitaria del Huila (CORHUILA).

| | |
| --- | --- |
| **Programa** | Ingenieria en Inteligencia Artificial |
| **Creditos** | 3 |
| **Grupo** | V (IPT) |
| **Horario** | Miercoles y Viernes 8:20 p. m. - 10:00 p. m. |
| **Modalidad** | Virtual (semanas 1-13) · Presencial (semanas 14-16) |
| **Aula** | Sesion virtual: enlace publicado en Moodle |
| **Semestre** | 2026-B |
| **Frecuencia** | 2 sesiones por semana |

## Estructura

El repositorio esta organizado en 16 semanas (`01-week` .. `16-week`).
Cada semana tiene la siguiente forma:

```
NN-week/
|-- 01-session/            # Primera sesion de la semana (miercoles)
|-- 02-session/            # Segunda sesion de la semana (viernes)
\-- 03-optional-activity/  # Actividad opcional de refuerzo
```

- Las carpetas `NN-session` contienen el material trabajado en clase.
- `03-optional-activity` guarda ejercicios opcionales de refuerzo, no calificables.

## Temario (16 semanas)

| Corte | Semanas | Unidad | Contenido |
| --- | --- | --- | --- |
| 1 | 1-5 | Introduccion a la IA y Busqueda | Que es la IA e historia · areas y aplicaciones · agentes y PEAS · busqueda no informada (BFS, DFS, UCS) · A\* y heuristicas · busqueda local, metaheuristicas y minimax |
| 2 | 6-10 | Aprendizaje Automatico | Fundamentos de ML y overfitting · regresion lineal y logistica · arboles, kNN y Naive Bayes · validacion cruzada, matriz de confusion y ROC · sesgo-varianza, regularizacion, k-means y PCA |
| 3 | 11-16 | Etica, Logica Difusa y Proyecto | Redes neuronales y deep learning · logica difusa e inferencia Mamdani · impactos sociales e IA responsable · herramientas practicas · integracion end-to-end · proyecto final |

## Como trabajar

```bash
# 1. Haz un fork de este repositorio (boton Fork arriba a la derecha).
# 2. Clona TU fork:
git clone https://github.com/TU-USUARIO/principios-ia-2026-b-g1.git
cd principios-ia-2026-b-g1

# 3. Coloca tu entrega en la carpeta de la semana correspondiente, por ejemplo 03-week/.
# 4. Sube los cambios:
git add .
git commit -m "Entrega semana 03"
git push
```

Antes de cada clase, actualiza tu copia local:

```bash
git pull origin main
```

Consulta el **Manual de Entrega por GitHub** disponible en el aula Moodle (Informacion importante).
Recuerda tener tu **repositorio de perfil** (usuario/usuario) con el bloque **CONFIG** (`FULL_NAME` + `GITHUB_USER`).

## Material interactivo (OVAs)

Las 32 sesiones interactivas del curso estan publicadas en:
**https://code-corhuila.github.io/ova-web/2026-B/principios-ia/**
