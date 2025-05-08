# common/exceptions.py
class AppError(Exception):
    """Base para marcar errores controlados."""


class InputError(AppError):
    """Datos de entrada no válidos (400)."""


class BusinessError(AppError):
    """Regla de negocio incumplida (422)."""


class UpstreamError(AppError):
    """Fallo al llamar a otro servicio (502)."""
