"""Tests for hardstyle.settings module."""

import pytest

from hardstyle.settings import LoggerSettings, Settings


class TestLoggerSettings:
    """Test cases for LoggerSettings class."""

    def test_default_values(self):
        """Test that LoggerSettings has correct default values."""
        settings = LoggerSettings()
        
        assert settings.console is True
        assert settings.file is True
        assert settings.structured_file is True
        assert settings.save_path == "logs/hardstyle"
        assert settings.level == "INFO"
        assert settings.rotation == "100 MB"
        assert settings.compression == "gz"
        assert settings.retention == "1 week"
        assert settings.rich_tracebacks is True
        assert settings.diagnose is True

    def test_custom_values(self):
        """Test LoggerSettings with custom values."""
        settings = LoggerSettings(
            console=False,
            file=True,
            structured_file=False,
            save_path="/custom/path",
            level="DEBUG",
            rotation="50 MB",
            compression="bz2",
            retention="2 weeks",
            rich_tracebacks=False,
            diagnose=False,
        )
        
        assert settings.console is False
        assert settings.file is True
        assert settings.structured_file is False
        assert settings.save_path == "/custom/path"
        assert settings.level == "DEBUG"
        assert settings.rotation == "50 MB"
        assert settings.compression == "bz2"
        assert settings.retention == "2 weeks"
        assert settings.rich_tracebacks is False
        assert settings.diagnose is False

    def test_format_string_multiline(self):
        """Test that the format string is properly constructed."""
        settings = LoggerSettings()
        
        # The format should be a single string despite multiline definition
        assert isinstance(settings.format, str)
        assert "time:YYYY-MM-DD HH:mm:ss" in settings.format
        assert "level" in settings.format
        assert "name" in settings.format
        assert "function" in settings.format
        assert "line" in settings.format
        assert "message" in settings.format


class TestSettings:
    """Test cases for main Settings class."""

    def test_default_settings(self):
        """Test that Settings creates proper default configuration."""
        settings = Settings()
        
        assert isinstance(settings.logger, LoggerSettings)
        assert settings.logger.console is True
        assert settings.logger.file is True
        assert settings.logger.structured_file is True

    def test_custom_logger_settings(self):
        """Test Settings with custom LoggerSettings."""
        custom_logger = LoggerSettings(
            console=False,
            level="ERROR",
            save_path="/tmp/custom"
        )
        settings = Settings(logger=custom_logger)
        
        assert settings.logger.console is False
        assert settings.logger.level == "ERROR"
        assert settings.logger.save_path == "/tmp/custom"

    def test_config_class(self):
        """Test that Config class is properly set up."""
        settings = Settings()
        
        assert hasattr(settings.Config, 'env_file')
        assert settings.Config.env_file == ".env"
        assert settings.Config.env_file_encoding == "utf-8"

    def test_settings_singleton_behavior(self):
        """Test that settings can be imported and used consistently."""
        from hardstyle.settings import settings

        # Should be a Settings instance
        assert isinstance(settings, Settings)
        assert isinstance(settings.logger, LoggerSettings)

    @pytest.mark.parametrize("level", [
        "TRACE", "DEBUG", "INFO", "SUCCESS", 
        "WARNING", "ERROR", "CRITICAL"
    ])
    def test_valid_log_levels(self, level):
        """Test that all valid log levels work."""
        logger_settings = LoggerSettings(level=level)
        assert logger_settings.level == level

    @pytest.mark.parametrize("rotation", [
        "1 MB", "10 MB", "100 MB", "1 GB",
        "1 hour", "1 day", "1 week", "1 month"
    ])
    def test_valid_rotation_values(self, rotation):
        """Test that various rotation values are accepted."""
        logger_settings = LoggerSettings(rotation=rotation)
        assert logger_settings.rotation == rotation

    @pytest.mark.parametrize("compression", [
        "gz", "bz2", "xz", "lzma", "tar.gz", "tar.bz2"
    ])
    def test_valid_compression_values(self, compression):
        """Test that various compression formats are accepted."""
        logger_settings = LoggerSettings(compression=compression)
        assert logger_settings.compression == compression 