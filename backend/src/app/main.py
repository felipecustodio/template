"""Robyn application entry point."""

from robyn import Robyn

from app.models import HealthResponse


app = Robyn(__file__)


def health() -> dict[str, str]:
    """Return validated service health data."""
    return HealthResponse(status="ok").model_dump()


@app.get("/api/health")
def health_route() -> dict[str, str]:
    """Serve service health data."""
    return health()


if __name__ == "__main__":
    app.start(host="0.0.0.0", port=8080)
