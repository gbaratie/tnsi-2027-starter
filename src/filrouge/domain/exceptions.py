"""Exceptions métier et applicatives du domaine."""


class DomainError(Exception):
    """Erreur de base pour toutes les exceptions du domaine."""



class ValidationError(DomainError):
    """Erreur levée lors de la validation des données du domaine."""

    def __init__(self, message: str, fields: dict[str, str] | None = None) -> None:
        super().__init__(message)
        self.message = message
        self.fields = fields or {}


class ConfigurationError(DomainError):
    """Erreur levée lorsqu'une configuration obligatoire est absente ou invalide."""

    def __init__(self, message: str) -> None:
        super().__init__(message)
        self.message = message


class StorageError(DomainError):
    """Erreur levée lors de l'accès ou la persistance des données."""

    def __init__(self, message: str, details: str | None = None) -> None:
        super().__init__(message)
        self.message = message
        self.details = details
