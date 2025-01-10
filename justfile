default:
    @just --list --justfile {{justfile()}}

# Clean all non-important files from previous builds or tasks
clean:
    rm -rf docs/_build
    rm -rf build/
    rm -rf dist/

# Build the documentation
docs: sync
    sphinx-build -j auto -n -W docs docs/_build
# Open a web-browser with the docs, and re-build docs whne their content changes on disk, refreshing the page
docs-live: sync
    sphinx-autobuild -j auto -n -N -q --watch src --watch docs docs docs/_build

# Lint and fix code problems
lint:
    ruff check --fix src tests
# Lint code without changing any file
lint-check:
    ruff check src tests
# Format package and test source files
format:
    ruff format src tests
# Check that package and source files are correctly formatted, without modifying them
format-check:
    ruff format --diff src tests

# Install all dependencies
sync:
    uv sync --dev

# Run all tests
test: sync
    uv run pytest

# Build wheel distribuitions
package: sync
    uv build --wheel

# Publish a new release on GH, bumping the version and updating the changelog
publish:
    cz bump --git-output-to-stderr --changelog-to-stdout > .changes
    git push --follow-tags
    gh release create v$(cz version -p) --verify-tag -F .changes
