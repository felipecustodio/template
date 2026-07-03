from pydantic import ValidationError

from app.main import health
from app.models import HealthResponse


def test_health_response_serializes() -> None:
    response = HealthResponse(status="ok")

    assert response.model_dump() == {"status": "ok"}


def test_health_response_rejects_unknown_status() -> None:
    try:
        HealthResponse.model_validate({"status": "down"})
    except ValidationError:
        return

    raise AssertionError("invalid status accepted")


def test_health_returns_validated_payload() -> None:
    assert health() == {"status": "ok"}
