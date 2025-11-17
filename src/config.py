from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class ProjectPaths:
    """Centralise the main paths used in the project."""
    project_root: Path
    data_dir: Path
    data_raw: Path
    data_processed: Path
    results_dir: Path
    figures_dir: Path
    metrics_dir: Path


def get_paths() -> ProjectPaths:
    """
    Compute canonical project paths based on the location of this file.
    """
    project_root = Path(__file__).resolve().parents[1]

    data_dir = project_root / "data"
    results_dir = project_root / "results"

    return ProjectPaths(
        project_root=project_root,
        data_dir=data_dir,
        data_raw=data_dir / "raw",
        data_processed=data_dir / "processed",
        results_dir=results_dir,
        figures_dir=results_dir / "figures",
        metrics_dir=results_dir / "metrics",
    )


def ensure_directories(paths: ProjectPaths | None = None) -> None:
    """
    Create all needed directories (data, results, etc.) if they do not exist.
    """
    if paths is None:
        paths = get_paths()

    for path in [
        paths.data_dir,
        paths.data_raw,
        paths.data_processed,
        paths.results_dir,
        paths.figures_dir,
        paths.metrics_dir,
    ]:
        path.mkdir(parents=True, exist_ok=True)
