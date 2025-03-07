import os

import pytest
from helpers import TemporaryShowyourworkRepository


@pytest.mark.xfail(
    os.getenv("WORKFLOW_VERSION") == "0.3.1",
    reason="letter class not supported for showyourwork <= 0.3.1",
)
class TestLetter(TemporaryShowyourworkRepository):
    """Test setting up and building an article that uses the basic `letter` documentclass."""

    # No need to test this on CI
    local_build_only = True

    ms = r"""
\documentclass{letter}
\usepackage{showyourwork}
\begin{document}
This is a test of the standard letter class.
\end{document}
    """

    def customize(self):
        with open(self.cwd / "src" / "tex" / "ms.tex", "w") as f:
            f.write(self.ms)
