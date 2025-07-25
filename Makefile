.PHONY: help install sync lock format lint test clean docs build all check

# Default target
.DEFAULT_GOAL := help

# Variables
PYTHON_FILES := hardstyle tests notebooks
PACKAGE_NAME := hardstyle

# Help target - shows available commands
help: ## Show this help message
	@echo "Available targets:"
	@awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z_-]+:.*?## / {printf "\033[36m%-15s\033[0m %s\n", $$1, $$2}' $(MAKEFILE_LIST)

# Installation and dependency management
install: ## Install the project and all dependencies
	uv sync --all-groups

sync: ## Sync the environment with the lockfile
	uv sync

lock: ## Update the lockfile
	uv lock

# Code formatting
format: ## Format code using black, isort, autoflake, and autopep8
	@echo "🎨 Running code formatters..."
	uv run --group format autoflake --in-place --remove-all-unused-imports --remove-unused-variables --recursive $(PYTHON_FILES)
	uv run --group format isort $(PYTHON_FILES)
	uv run --group format black $(PYTHON_FILES)
	uv run --group format autopep8 --in-place --recursive --aggressive --aggressive $(PYTHON_FILES)
	@echo "✅ Code formatting completed!"

format-check: ## Check code formatting without making changes
	@echo "🔍 Checking code formatting..."
	uv run --group format black --check $(PYTHON_FILES)
	uv run --group format isort --check-only $(PYTHON_FILES)
	@echo "✅ Format check completed!"

# Linting and static analysis
lint: ## Run all linters (ruff, mypy, pylint)
	@echo "🔍 Running linters..."
	uv run --group lint ruff check $(PYTHON_FILES)
	uv run --group lint mypy $(PYTHON_FILES)
	uv run --group lint pylint $(PACKAGE_NAME)
	@echo "✅ Linting completed!"

lint-fix: ## Run linters with auto-fix where possible
	@echo "🔧 Running linters with auto-fix..."
	uv run --group lint ruff check --fix $(PYTHON_FILES)
	@echo "✅ Lint fixes applied!"

# Testing
test: ## Run all tests
	@echo "🧪 Running tests..."
	uv run --group test pytest tests/ -v --emoji --instafail --cov=$(PACKAGE_NAME) --cov-report=html --cov-report=term
	@echo "✅ Tests completed!"

test-fast: ## Run tests without coverage
	@echo "🏃 Running fast tests..."
	uv run --group test pytest tests/ -v --emoji --instafail
	@echo "✅ Fast tests completed!"

# Documentation
docs: ## Serve documentation locally
	@echo "📖 Serving documentation..."
	cd docs && pnpm run dev

# Jupyter notebooks
notebook: ## Start Jupyter notebook server
	@echo "📓 Starting Jupyter notebook..."
	uv run jupyter notebook notebooks/

# Development utilities
clean: ## Clean up cache files and build artifacts
	@echo "🧹 Cleaning up..."
	find . -type d -name "__pycache__" -delete
	find . -type f -name "*.pyc" -delete
	find . -type f -name "*.pyo" -delete
	find . -type d -name "*.egg-info" -exec rm -rf {} +
	find . -type d -name ".pytest_cache" -delete
	find . -type d -name ".mypy_cache" -delete
	find . -type d -name ".ruff_cache" -delete
	find . -type f -name ".coverage" -delete
	find . -type d -name "htmlcov" -delete
	find . -type d -name "dist" -delete
	find . -type d -name "build" -delete
	@echo "✅ Cleanup completed!"

# Build
build: ## Build the package
	@echo "📦 Building package..."
	uv build
	@echo "✅ Build completed!"

# Environment info
info: ## Show project and environment information
	@echo "📋 Project Information:"
	@echo "Package: $(PACKAGE_NAME)"
	@echo "Python version:"
	@uv run python --version
	@echo "uv version:"
	@uv --version
	@echo "Dependencies:"
	@uv tree

# Quality checks
check: format-check lint test ## Run all quality checks (format, lint, test)

# Comprehensive workflows
all: clean install format lint test ## Run the complete development workflow
	@echo "🎉 All tasks completed successfully!"

ci: install format-check lint test ## CI workflow (install, check format, lint, test)
	@echo "🤖 CI workflow completed!"

# Development setup
dev-setup: install ## Set up development environment
	@echo "🛠️  Setting up development environment..."
	@echo "✅ Development environment ready!"
	@echo "💡 Run 'make help' to see available commands"
