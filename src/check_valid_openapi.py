from __future__ import annotations

import argparse
import ast
import platform
import sys
import traceback
from typing import Sequence
import subprocess


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument('filenames', nargs='*')
    args = parser.parse_args(argv)

    retval = 0
    for filename in args.filenames:

        subprocess.run(['openapi-spec-validator', filename],
                       stderr=sys.stderr, stdout=sys.stdout)

    return 0


if __name__ == '__main__':
    raise SystemExit(main())
