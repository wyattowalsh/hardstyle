"""hardstyle/logger.py -- Enhanced logger for the hardstyle project.

Features:
- Rich console integration with beautiful formatting
- File logging with rotation and compression
- Structured JSON logging
- Configurable via settings
- Proper error handling and validation
"""

import sys
from pathlib import Path
from typing import Optional

from loguru import logger
from rich.console import Console
from rich.logging import RichHandler

from hardstyle.settings import settings


def _create_rich_handler() -> RichHandler:
    """Create a Rich handler for beautiful console logging."""
    rich_console = Console(
        stderr=True,
        force_terminal=True,
        width=120,
    )
    
    return RichHandler(
        console=rich_console,
        show_time=False,  # We handle time in our format
        show_level=False,  # We handle level in our format
        show_path=False,  # We handle path in our format
        rich_tracebacks=settings.logger.rich_tracebacks,
        tracebacks_show_locals=settings.logger.diagnose,
        markup=True,
    )


def setup_logger(
    force_setup: bool = False,
    console_override: Optional[bool] = None,
    file_override: Optional[bool] = None,
    structured_file_override: Optional[bool] = None,
) -> None:
    """Setup the enhanced logger for the hardstyle project.
    
    Args:
        force_setup: Force re-setup even if already configured
        console_override: Override console logging setting
        file_override: Override file logging setting  
        structured_file_override: Override structured file logging setting
        
    Raises:
        ValueError: If invalid configuration provided
        OSError: If unable to create log directory
    """
    # Remove any existing handlers (safe to call even if none exist)
    logger.remove()
    
    # Get settings with overrides
    enable_console = (
        console_override 
        if console_override is not None 
        else settings.logger.console
    )
    enable_file = (
        file_override 
        if file_override is not None 
        else settings.logger.file
    )
    enable_structured = (
        structured_file_override 
        if structured_file_override is not None 
        else settings.logger.structured_file
    )
    
    # Validate log level
    valid_levels = {
        "TRACE", "DEBUG", "INFO", "SUCCESS", 
        "WARNING", "ERROR", "CRITICAL"
    }
    if settings.logger.level.upper() not in valid_levels:
        raise ValueError(
            f"Invalid log level: {settings.logger.level}. "
            f"Must be one of: {', '.join(valid_levels)}"
        )
    
    # Setup console logging with Rich
    if enable_console:
        try:
            rich_handler = _create_rich_handler()
            logger.add(
                rich_handler,
                level=settings.logger.level,
                format=settings.logger.format,
                diagnose=settings.logger.diagnose,
            )
        except Exception as e:
            # Fallback to stderr if Rich fails
            logger.add(
                sys.stderr,
                level=settings.logger.level,
                format=settings.logger.format,
                diagnose=settings.logger.diagnose,
            )
            logger.warning(
                f"Failed to setup Rich console handler, using stderr: {e}"
            )
    
    # Setup file logging
    if enable_file:
        try:
            # Ensure log directory exists
            log_path = Path(settings.logger.save_path)
            if log_path.suffix:
                # save_path includes filename
                log_dir = log_path.parent
                file_path = log_path
            else:
                # save_path is directory only
                log_dir = log_path
                file_path = log_path / "hardstyle.log"
            
            log_dir.mkdir(parents=True, exist_ok=True)
            
            logger.add(
                str(file_path),
                level=settings.logger.level,
                format=settings.logger.format,
                rotation=settings.logger.rotation,
                retention=settings.logger.retention,
                compression=settings.logger.compression,
                diagnose=settings.logger.diagnose,
                enqueue=True,  # Thread-safe logging
            )
        except Exception as e:
            logger.error(f"Failed to setup file logging: {e}")
            raise OSError(f"Unable to setup file logging: {e}") from e
    
    # Setup structured JSON logging
    if enable_structured:
        try:
            # Ensure log directory exists
            log_path = Path(settings.logger.save_path)
            if log_path.suffix:
                # save_path includes filename, modify for structured
                log_dir = log_path.parent
                stem = log_path.stem
                structured_path = log_dir / f"{stem}_structured.jsonl"
            else:
                # save_path is directory only
                log_dir = log_path
                structured_path = log_path / "hardstyle_structured.jsonl"
            
            log_dir.mkdir(parents=True, exist_ok=True)
            
            logger.add(
                str(structured_path),
                level=settings.logger.level,
                rotation=settings.logger.rotation,
                retention=settings.logger.retention,
                compression=settings.logger.compression,
                diagnose=settings.logger.diagnose,
                enqueue=True,  # Thread-safe logging
                serialize=True,  # Automatic JSON serialization
            )
        except Exception as e:
            logger.error(f"Failed to setup structured logging: {e}")
            # Don't raise here as structured logging is optional
    
    # Log successful setup
    logger.info(
        "Logger setup complete - "
        f"Console: {enable_console}, "
        f"File: {enable_file}, "
        f"Structured: {enable_structured}"
    )


def get_logger(name: str = "hardstyle"):
    """Get a logger instance with the specified name.
    
    Args:
        name: Logger name (defaults to 'hardstyle')
        
    Returns:
        Configured logger instance
    """
    # Ensure logger is setup
    setup_logger()
    
    # Return logger with context
    return logger.bind(name=name)


# Initialize logger on import
setup_logger()


# Re-export logger for convenience
__all__ = ["logger", "setup_logger", "get_logger"]