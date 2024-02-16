import sys
from pathlib import Path


def set_path() -> None:
    main_dir = Path(__file__).parent.parent
    sys.path.append(str(main_dir))
