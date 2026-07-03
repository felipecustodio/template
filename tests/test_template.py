from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]


class TemplateContractTests(unittest.TestCase):
    def test_required_files_exist(self) -> None:
        required = (
            ".github/workflows/ci.yml",
            "backend/pyproject.toml",
            "backend/src/app/main.py",
            "backend/src/app/models.py",
            "backend/tests/test_health.py",
            "backend/uv.lock",
            "frontend/aube-lock.yaml",
            "frontend/package.json",
            "frontend/src/health.ts",
            "frontend/src/main.ts",
            "frontend/tsconfig.json",
            "frontend/vite.config.ts",
            "hk.pkl",
            "mise.lock",
            "mise.toml",
        )

        missing = [path for path in required if not (ROOT / path).is_file()]
        self.assertEqual([], missing)

    def test_named_tools_are_configured(self) -> None:
        files = {
            "frontend/package.json": ("vite", "typescript", "zod", "@biomejs/biome"),
            "backend/pyproject.toml": ("robyn", "pydantic", "karva"),
            "mise.toml": ("aube", "uv", "hk", "[tasks.ci]"),
            "hk.pkl": ("pre-commit", "pre-push", "mise"),
            ".github/workflows/ci.yml": ("jdx/mise-action", "mise run ci"),
        }

        for relative_path, terms in files.items():
            with self.subTest(path=relative_path):
                content = (ROOT / relative_path).read_text()
                for term in terms:
                    self.assertIn(term, content)

    def test_mise_exposes_complete_task_surface(self) -> None:
        content = (ROOT / "mise.toml").read_text()

        for task in ("install", "dev", "format", "lint", "typecheck", "test", "build", "ci"):
            self.assertIn(f"[tasks.{task}]", content)

    def test_ci_uses_locked_mise_toolchain(self) -> None:
        content = (ROOT / ".github/workflows/ci.yml").read_text()

        for term in (
            "push:",
            "pull_request:",
            "permissions:",
            "concurrency:",
            "cancel-in-progress: true",
            "actions/checkout@v6",
            "jdx/mise-action@v4",
            "version: 2026.6.10",
            "mise run ci",
        ):
            self.assertIn(term, content)


if __name__ == "__main__":
    unittest.main()
