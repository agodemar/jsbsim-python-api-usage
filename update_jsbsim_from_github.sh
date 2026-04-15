#!/usr/bin/env bash
# update_jsbsim_from_github.sh
#
# Build and install the JSBSim Python API directly from the latest GitHub
# source, then report the installed version.
#
# Usage:
#   ./update_jsbsim_from_github.sh              # uses /usr/local/bin/python
#   PYTHON=/path/to/python ./update_jsbsim_from_github.sh

set -euo pipefail

PYTHON="${PYTHON:-/usr/local/bin/python}"
JSBSIM_REPO="https://github.com/JSBSim-Team/jsbsim.git"
BUILD_DIR="${TMPDIR:-/tmp}/jsbsim_build"

echo "=== JSBSim from-source installer ==="
echo "  Python    : $PYTHON"
echo "  Build dir : $BUILD_DIR"
echo ""

# ---------------------------------------------------------------------------
# 1. Clone or fast-forward update
# ---------------------------------------------------------------------------
if [ -d "$BUILD_DIR/.git" ]; then
    echo "[1/4] Updating existing clone..."
    git -C "$BUILD_DIR" fetch --depth 1 origin
    git -C "$BUILD_DIR" reset --hard FETCH_HEAD
else
    echo "[1/4] Cloning JSBSim repository (shallow)..."
    git clone --depth 1 "$JSBSIM_REPO" "$BUILD_DIR"
fi
COMMIT=$(git -C "$BUILD_DIR" rev-parse --short HEAD)
echo "      commit: $COMMIT"

# ---------------------------------------------------------------------------
# 2. Generate pyproject.toml from the CMake template
# ---------------------------------------------------------------------------
echo "[2/4] Generating pyproject.toml..."
"$PYTHON" - "$BUILD_DIR" <<'PY'
import sys, re
from pathlib import Path

build_dir = Path(sys.argv[1])
cmake = (build_dir / 'CMakeLists.txt').read_text()
maj  = re.search(r'set\(PROJECT_VERSION_MAJOR\s+"([^"]+)"\)', cmake).group(1)
min_ = re.search(r'set\(PROJECT_VERSION_MINOR\s+"([^"]+)"\)', cmake).group(1)
pat  = re.search(r'set\(PROJECT_VERSION_PATCH\s+"([^"]+)"\)', cmake).group(1)
version = f"{maj}.{min_}.{pat}"
tpl = (build_dir / 'python' / 'pyproject.toml.in').read_text()
(build_dir / 'pyproject.toml').write_text(tpl.replace('${PROJECT_VERSION}', version))
print(f"      version: {version}")
PY

# ---------------------------------------------------------------------------
# 3. Ensure python/__init__.pyi is present (required by the CMake install step)
# ---------------------------------------------------------------------------
echo "[3/4] Checking for __init__.pyi stub..."
PYI_DEST="$BUILD_DIR/python/__init__.pyi"
if [ ! -f "$PYI_DEST" ]; then
    EXISTING_PYI=$("$PYTHON" -c "
import jsbsim
from pathlib import Path
p = Path(jsbsim.__file__).parent / '__init__.pyi'
print(p if p.exists() else '')
" 2>/dev/null || true)

    if [ -n "$EXISTING_PYI" ] && [ -f "$EXISTING_PYI" ]; then
        cp "$EXISTING_PYI" "$PYI_DEST"
        echo "      copied from existing installation"
    else
        touch "$PYI_DEST"
        echo "      created empty stub"
    fi
else
    echo "      already present"
fi

# ---------------------------------------------------------------------------
# 4. Build wheel and install
# ---------------------------------------------------------------------------
echo "[4/4] Building and installing wheel (this may take a few minutes)..."
"$PYTHON" -m pip install --user --upgrade "$BUILD_DIR"

# ---------------------------------------------------------------------------
# Result
# ---------------------------------------------------------------------------
echo ""
echo "=== Installed package ==="
"$PYTHON" -c "
import importlib.metadata as m, jsbsim
print('  JSBSim version :', m.version('JSBSim'))
print('  Module path    :', jsbsim.__file__)
"
echo "  Git commit     : $COMMIT  ($(git -C "$BUILD_DIR" show -s --format=%ci HEAD))"
echo ""
echo "Done."
