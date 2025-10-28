# VNTG Infra - Docker Commands
# .env.local 파일을 기본으로 사용하며 다른 파일을 사용할 경우 아래와 같이 사용함
# make ENV_FILE=./.env.dev all-up"

# .PHONY: help all alloy infra-up log-up down restart logs clean ps db-shell redis-cli

# Variables
ENV_FILE := ./.env.local
DOCKER_COMPOSE := docker compose 

# Method 1: Include .env file (recommended)
# This loads all variables from .env file into make
# ifneq (,$(wildcard $(ENV_FILE))) # 파일이 존재하면: 파일명 반환 (../.env.local)
#     include $(ENV_FILE)
#     export
# endif

# Default target
help:
	@echo "VNTG Infra - Docker Commands"
	@echo ""
	@echo "Usage: make [target]"
	@echo ""
	@echo "Targets:"
	@echo "  help       Show this help message"
	@echo "  up    		up -d"
	@echo "  down       Stop all services"
	@echo "  restart    Restart all services"
	@echo "  logs       Show logs for all services"
	@echo "  clean      Stop services and remove volumes"
	@echo "  ps         Show running containers"


up: 
	$(DOCKER_COMPOSE) up -d

# # Start infrastructure only
# alloy:
# 	@echo "Starting infrastructure services..."
# 	$(DOCKER_COMPOSE) --profile=alloy up -d
# 	@echo "Infrastructure services started!"

# Stop all services
down:
	@echo "Stopping all services..."
	#$(DOCKER_COMPOSE) --profile "*" down
	$(DOCKER_COMPOSE) down
	@echo "All services stopped!"

# Restart all services
restart: down all-up

# Show logs for all services
logs:
	$(DOCKER_COMPOSE) logs -f

# Clean up everything including volumes
clean:
	@echo "Stopping services and removing volumes..."
	$(DOCKER_COMPOSE) down -v
	@echo "Cleanup complete!"

# Show running containers
ps:
	$(DOCKER_COMPOSE) ps

