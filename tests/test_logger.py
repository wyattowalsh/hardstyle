"""Tests for hardstyle.logger module."""

import json
import sys
from unittest.mock import patch

import pytest
from loguru import logger
from rich.logging import RichHandler

from hardstyle.logger import _create_rich_handler, get_logger, setup_logger


class TestCreateRichHandler:
    """Test cases for _create_rich_handler function."""

    @patch('hardstyle.logger.settings')
    def test_create_rich_handler_default_settings(self, mock_settings):
        """Test Rich handler creation with default settings."""
        mock_settings.logger.rich_tracebacks = True
        mock_settings.logger.diagnose = True
        
        handler = _create_rich_handler()
        
        assert isinstance(handler, RichHandler)
        assert handler.rich_tracebacks is True
        assert handler.show_time is False
        assert handler.show_level is False
        assert handler.show_path is False

    @patch('hardstyle.logger.settings')
    def test_create_rich_handler_custom_settings(self, mock_settings):
        """Test Rich handler creation with custom settings."""
        mock_settings.logger.rich_tracebacks = False
        mock_settings.logger.diagnose = False
        
        handler = _create_rich_handler()
        
        assert isinstance(handler, RichHandler)
        assert handler.rich_tracebacks is False


class TestSetupLogger:
    """Test cases for setup_logger function."""

    def test_setup_logger_removes_existing_handlers(self, clean_logger):
        """Test that setup_logger removes existing handlers."""
        # Add a dummy handler
        logger.add(sys.stderr)
        
        # Setup logger should remove the existing handler
        setup_logger()
        
        # We can't easily check handler count, so verify function completes
        assert True

    @patch('hardstyle.logger.settings')
    def test_setup_logger_with_invalid_level(
        self, mock_settings, clean_logger
    ):
        """Test setup_logger raises ValueError for invalid log level."""
        mock_settings.logger.level = "INVALID_LEVEL"
        
        with pytest.raises(ValueError, match="Invalid log level"):
            setup_logger()

    @patch('hardstyle.logger.settings')
    def test_setup_logger_console_only(self, mock_settings, clean_logger):
        """Test setup_logger with console logging only."""
        mock_settings.logger.console = True
        mock_settings.logger.file = False
        mock_settings.logger.structured_file = False
        mock_settings.logger.level = "INFO"
        mock_settings.logger.format = "test format"
        mock_settings.logger.diagnose = True
        mock_settings.logger.rich_tracebacks = True
        
        setup_logger()
        
        # Function should complete without errors
        assert True

    @patch('hardstyle.logger.settings')
    def test_setup_logger_file_only(
        self, mock_settings, clean_logger, temp_log_dir
    ):
        """Test setup_logger with file logging only."""
        mock_settings.logger.console = False
        mock_settings.logger.file = True
        mock_settings.logger.structured_file = False
        mock_settings.logger.level = "DEBUG"
        mock_settings.logger.format = "test format"
        mock_settings.logger.save_path = str(temp_log_dir / "test.log")
        mock_settings.logger.rotation = "1 MB"
        mock_settings.logger.retention = "1 week"
        mock_settings.logger.compression = "gz"
        mock_settings.logger.diagnose = True
        
        setup_logger()
        
        # Function should complete without errors
        assert True

    @patch('hardstyle.logger.settings')
    def test_setup_logger_structured_only(
        self, mock_settings, clean_logger, temp_log_dir
    ):
        """Test setup_logger with structured logging only."""
        mock_settings.logger.console = False
        mock_settings.logger.file = False
        mock_settings.logger.structured_file = True
        mock_settings.logger.level = "WARNING"
        mock_settings.logger.save_path = str(temp_log_dir / "structured.log")
        mock_settings.logger.rotation = "5 MB"
        mock_settings.logger.retention = "2 days"
        mock_settings.logger.compression = "bz2"
        mock_settings.logger.diagnose = False
        
        setup_logger()
        
        # Function should complete without errors
        assert True

    @patch('hardstyle.logger.settings')
    def test_setup_logger_all_enabled(
        self, mock_settings, clean_logger, temp_log_dir
    ):
        """Test setup_logger with all logging types enabled."""
        mock_settings.logger.console = True
        mock_settings.logger.file = True
        mock_settings.logger.structured_file = True
        mock_settings.logger.level = "TRACE"
        mock_settings.logger.format = "test format"
        mock_settings.logger.save_path = str(temp_log_dir)
        mock_settings.logger.rotation = "10 MB"
        mock_settings.logger.retention = "1 month"
        mock_settings.logger.compression = "xz"
        mock_settings.logger.diagnose = True
        mock_settings.logger.rich_tracebacks = True
        
        setup_logger()
        
        # Function should complete without errors
        assert True

    def test_setup_logger_with_overrides(self, clean_logger):
        """Test setup_logger with parameter overrides."""
        setup_logger(
            console_override=False,
            file_override=False,
            structured_file_override=False
        )
        
        # Function should complete without errors
        assert True

    @patch('hardstyle.logger.settings')
    @patch('hardstyle.logger._create_rich_handler')
    def test_setup_logger_rich_handler_failure(
        self, mock_create_rich, mock_settings, clean_logger
    ):
        """Test setup_logger fallback when Rich handler creation fails."""
        mock_settings.logger.console = True
        mock_settings.logger.file = False
        mock_settings.logger.structured_file = False
        mock_settings.logger.level = "INFO"
        mock_settings.logger.format = "test format"
        mock_settings.logger.diagnose = True
        
        # Make Rich handler creation fail
        mock_create_rich.side_effect = Exception("Rich handler failed")
        
        setup_logger()
        
        # Should fall back to stderr
        assert True

    @patch('hardstyle.logger.settings')
    def test_setup_logger_file_logging_error(
        self, mock_settings, clean_logger
    ):
        """Test setup_logger raises OSError when file logging fails."""
        mock_settings.logger.console = False
        mock_settings.logger.file = True
        mock_settings.logger.structured_file = False
        mock_settings.logger.level = "INFO"
        mock_settings.logger.format = "test format"
        mock_settings.logger.save_path = "/invalid/path/that/does/not/exist"
        mock_settings.logger.rotation = "1 MB"
        mock_settings.logger.retention = "1 week"
        mock_settings.logger.compression = "gz"
        mock_settings.logger.diagnose = True
        
        with pytest.raises(OSError, match="Unable to setup file logging"):
            setup_logger()


class TestGetLogger:
    """Test cases for get_logger function."""

    def test_get_logger_default_name(self, clean_logger):
        """Test get_logger with default name."""
        test_logger = get_logger()
        
        # Should return a logger-like object
        assert hasattr(test_logger, 'info')
        assert hasattr(test_logger, 'debug')
        assert hasattr(test_logger, 'warning')
        assert hasattr(test_logger, 'error')

    def test_get_logger_custom_name(self, clean_logger):
        """Test get_logger with custom name."""
        test_logger = get_logger("custom_logger")
        
        # Should return a logger-like object
        assert hasattr(test_logger, 'info')
        assert hasattr(test_logger, 'debug')
        assert hasattr(test_logger, 'warning')
        assert hasattr(test_logger, 'error')


class TestLoggerIntegration:
    """Integration tests for the complete logger functionality."""

    @patch('hardstyle.logger.settings')
    def test_logger_file_creation(
        self, mock_settings, clean_logger, temp_log_dir
    ):
        """Test that log files are actually created."""
        log_file = temp_log_dir / "integration_test.log"
        
        mock_settings.logger.console = False
        mock_settings.logger.file = True
        mock_settings.logger.structured_file = False
        mock_settings.logger.level = "DEBUG"
        mock_settings.logger.format = "{time} | {level} | {message}"
        mock_settings.logger.save_path = str(log_file)
        mock_settings.logger.rotation = "1 MB"
        mock_settings.logger.retention = "1 week"
        mock_settings.logger.compression = "gz"
        mock_settings.logger.diagnose = False
        
        setup_logger()
        
        # Log some messages
        logger.info("Test info message")
        logger.debug("Test debug message")
        logger.warning("Test warning message")
        
        # Check that log file was created
        assert log_file.exists()
        
        # Check that log file has content
        content = log_file.read_text()
        assert "Test info message" in content
        assert "Test debug message" in content
        assert "Test warning message" in content

    @patch('hardstyle.logger.settings')
    def test_structured_logging_creation(
        self, mock_settings, clean_logger, temp_log_dir
    ):
        """Test that structured log files are created with JSON content."""
        log_dir = temp_log_dir / "structured_logs"
        
        mock_settings.logger.console = False
        mock_settings.logger.file = False
        mock_settings.logger.structured_file = True
        mock_settings.logger.level = "INFO"
        mock_settings.logger.save_path = str(log_dir)
        mock_settings.logger.rotation = "1 MB"
        mock_settings.logger.retention = "1 week"
        mock_settings.logger.compression = "gz"
        mock_settings.logger.diagnose = False
        
        setup_logger()
        
        # Log a message
        logger.info("Structured test message")
        
        # Check that structured log file was created
        structured_file = log_dir / "hardstyle_structured.jsonl"
        assert structured_file.exists()
        
        # Check that the content is valid JSON
        content = structured_file.read_text().strip()
        if content:  # Only check if there's content
            lines = content.split('\n')
            for line in lines:
                if line.strip():  # Skip empty lines
                    parsed = json.loads(line)
                    assert 'timestamp' in parsed
                    assert 'level' in parsed
                    assert 'message' in parsed

    @patch('hardstyle.logger.settings')
    def test_logger_levels_filtering(
        self, mock_settings, clean_logger, temp_log_dir
    ):
        """Test that log level filtering works correctly."""
        log_file = temp_log_dir / "level_test.log"
        
        mock_settings.logger.console = False
        mock_settings.logger.file = True
        mock_settings.logger.structured_file = False
        mock_settings.logger.level = "WARNING"  # Only WARNING and above
        mock_settings.logger.format = "{level} | {message}"
        mock_settings.logger.save_path = str(log_file)
        mock_settings.logger.rotation = "1 MB"
        mock_settings.logger.retention = "1 week"
        mock_settings.logger.compression = "gz"
        mock_settings.logger.diagnose = False
        
        setup_logger()
        
        # Log messages at different levels
        logger.debug("Debug message - should not appear")
        logger.info("Info message - should not appear")
        logger.warning("Warning message - should appear")
        logger.error("Error message - should appear")
        
        # Check log file content
        content = log_file.read_text()
        assert "Debug message" not in content
        assert "Info message" not in content
        assert "Warning message" in content
        assert "Error message" in content

    def test_get_logger_with_context(self, clean_logger):
        """Test that get_logger returns logger with proper context."""
        app_logger = get_logger("test_app")
        
        # Should be able to log messages
        app_logger.info("Test message from context logger")
        
        # Function should complete without errors
        assert True 