"""Pytest configuration and fixtures for hardstyle tests."""

import tempfile
from pathlib import Path
from typing import Generator
from unittest.mock import Mock

import pytest
from loguru import logger

from hardstyle.settings import LoggerSettings, Settings


@pytest.fixture
def temp_log_dir() -> Generator[Path, None, None]:
    """Create a temporary directory for log files during testing."""
    with tempfile.TemporaryDirectory() as temp_dir:
        yield Path(temp_dir)


@pytest.fixture
def mock_settings(temp_log_dir: Path) -> Settings:
    """Create mock settings for testing with temporary log directory."""
    logger_settings = LoggerSettings(
        console=True,
        file=True,
        structured_file=True,
        save_path=str(temp_log_dir / "test_logs"),
        level="DEBUG",
        rotation="10 MB",
        compression="gz",
        retention="1 day",
        rich_tracebacks=True,
        diagnose=True,
    )
    
    return Settings(logger=logger_settings)


@pytest.fixture
def clean_logger():
    """Clean logger state before and after each test."""
    # Remove all handlers before test
    logger.remove()
    yield
    # Clean up after test
    logger.remove()


@pytest.fixture
def mock_rich_handler():
    """Create a mock Rich handler for testing."""
    mock_handler = Mock()
    mock_handler.emit = Mock()
    return mock_handler


@pytest.fixture
def sample_log_messages():
    """Sample log messages for testing."""
    return {
        "info": "This is an info message",
        "debug": "This is a debug message",
        "warning": "This is a warning message",
        "error": "This is an error message",
        "success": "This is a success message",
        "critical": "This is a critical message",
    }


@pytest.fixture
def sample_exception():
    """Create a sample exception for testing exception logging."""
    try:
        raise ValueError("Test exception for logging")
    except ValueError as e:
        return e 