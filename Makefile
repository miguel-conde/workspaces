# =============================================================================
# 🛠️ Makefile PRO para microservices-example
# =============================================================================

# Variables generales
PROJECT_NAME := microservices-example
COMPOSE := docker compose

# Colores
GREEN := \033[0;32m
RED := \033[0;31m
YELLOW := \033[1;33m
NC := \033[0m  # No Color

# =============================================================================
# Comandos
# =============================================================================

.PHONY: help up down restart logs ps build test test-watch lint format

help:
	@echo ""
	@echo "  $(GREEN)Comandos disponibles:$(NC)"
	@echo ""
	@echo "  $(YELLOW)make up$(NC)         → Levanta docker-compose con build"
	@echo "  $(YELLOW)make down$(NC)       → Baja docker-compose"
	@echo "  $(YELLOW)make restart$(NC)    → Reinicia docker-compose"
	@echo "  $(YELLOW)make logs$(NC)       → Logs en tiempo real"
	@echo "  $(YELLOW)make ps$(NC)         → Estado de contenedores"
	@echo "  $(YELLOW)make build$(NC)      → Construye imágenes"
	@echo "  $(YELLOW)make test$(NC)       → Ejecuta todos los tests"
	@echo "  $(YELLOW)make test-watch$(NC) → Ejecuta tests parando en el primer error"
	@echo "  $(YELLOW)make lint$(NC)       → Formatea el código (black + isort)"
	@echo "  $(YELLOW)make format$(NC)     → Igual que lint"
	@echo ""

# Docker
up:
	@echo "$(GREEN)→ Levantando servicios...$(NC)"
	@$(COMPOSE) up --build

down:
	@echo "$(RED)→ Parando servicios...$(NC)"
	@$(COMPOSE) down

restart:
	@make down
	@make up

logs:
	@echo "$(GREEN)→ Mostrando logs...$(NC)"
	@$(COMPOSE) logs -f

ps:
	@$(COMPOSE) ps

build:
	@echo "$(GREEN)→ Build de imágenes...$(NC)"
	@$(COMPOSE) build

# Testing
test:
	@echo "$(GREEN)→ Lanzando tests...$(NC)"
	@pytest -q tests/

test-watch:
	@echo "$(GREEN)→ Lanzando tests (modo rápido)...$(NC)"
	@pytest --maxfail=1 --disable-warnings -q tests/

# Formateo
lint:
	@echo "$(GREEN)→ Formateando código...$(NC)"
	@black .
	@isort .

format: lint
