# 📦 Proyecto: Microservicios de Calculadora Mock

Este proyecto es una prueba de concepto (POC) que implementa una arquitectura de microservicios usando Python, FastAPI y Docker.
Cada servicio realiza una operación sencilla de cálculo, y un Caso de Uso (CDU) orquesta las llamadas entre servicios.

---

## 📋 Estructura del proyecto

```
/addition_ms/        → Microservicio de suma
/multiply_ms/        → Microservicio de duplicado
/calc_cdu/           → Caso de Uso: suma + duplicado
/common/             → Código compartido (excepciones, middleware, logging)
/tests/              → Tests unitarios e integración
/docker-compose.yml  → Orquestación de contenedores
/.devcontainer/      → Configuración DevContainer para VSCode
/.vscode/            → Configuración de tareas y launch para debug
/Makefile            → Comandos rápidos de desarrollo
```

---

## 🚀 Primeros pasos

### 1. Requisitos

* Docker + Docker Compose (v2+)
* Make
* Python 3.12+ (para desarrollo local si no usas Docker)
* VSCode + extensiones de DevContainer recomendadas

### 2. Levantar servicios

Desde terminal en la raíz del proyecto:

```bash
make up
```

Esto:

* Construirá las imágenes Docker.
* Levantará los microservicios `addition_ms`, `multiply_ms` y el CDU `calc_cdu`.
* Cada servicio corre en un contenedor distinto.

### 3. Parar servicios

```bash
make down
```

---

## 🐳 Desarrollo local en VSCode

Este proyecto está preparado para trabajar directamente en un **DevContainer** de VSCode.

Pasos:

1. Abre el proyecto en VSCode.
2. Si tienes la extensión **Remote - Containers**, haz:
   `Ctrl+Shift+P → Reopen in Container`.
3. Usa las tareas predefinidas para lanzar cada microservicio en modo debug:

   * `run‑addition`
   * `run‑multiply`
   * `run‑cdu`

**Depuración**: Puedes poner breakpoints y usar F5 gracias a `debugpy`.

---

## 💪 Testing

Lanzar todos los tests:

```bash
make test
```

Modo rápido (parando en el primer fallo):

```bash
make test-watch
```

Incluye:

* Tests unitarios de lógica interna (`execute()`).
* Tests de integración de los endpoints usando `httpx` + `respx`.

---

## 🛠️ Formateo de código

Este proyecto usa `black` e `isort` para formateo automático.

Para formatear todo el código:

```bash
make lint
```

o

```bash
make format
```

---

## 📈 Logging estructurado

* Todos los servicios generan logs en formato JSON.
* Cada request genera un `trace_id` que es propagado entre servicios.
* Nivel de logging configurable por entorno (`ENVIRONMENT=development` o `production`).

---

## 📜 Comandos útiles (`Makefile`)

| Comando           | Acción                                   |
| :---------------- | :--------------------------------------- |
| `make up`         | Levanta docker-compose con build         |
| `make down`       | Para docker-compose                      |
| `make restart`    | Baja y vuelve a subir                    |
| `make logs`       | Muestra logs de todos los servicios      |
| `make ps`         | Muestra los contenedores activos         |
| `make test`       | Ejecuta los tests                        |
| `make test-watch` | Tests rápidos parando en el primer fallo |
| `make lint`       | Formatea el código                       |
| `make format`     | Igual que lint                           |

---

## 📈 Extensiones recomendadas para VSCode

* Docker
* Remote - Containers
* Python
* REST Client
* GitLens
* Test Explorer UI

---

## ✨ Pendiente para evolución futura

* Añadir métricas Prometheus (via `prometheus-fastapi-instrumentator`)
* Healthchecks mejorados en `docker-compose.yml`
* Pipeline CI/CD (tests + lint + docker build/push automático)

---

# 📣 Contacto

Este proyecto está desarrollado como parte de un ejercicio de arquitectura de microservicios para proyectos de IA Generativa.

---

# 🔖 Badges (opcional)

```markdown
![Microservices Example](https://img.shields.io/badge/Microservices-Python-FastAPI-blue)
![Docker Compose](https://img.shields.io/badge/Docker-Compose-blue)
![Status](https://img.shields.io/badge/Status-In%20Development-yellow)
```
