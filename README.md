Description
===========
This repo serves an example on how to migrate a project using maturin as build-backend and poetry as a dependency manager.

As an aside, the steps to create (smoothly) a project similar to this one are:

1. Install maturin

    ```shell
    pipx install maturin
    ```

2. Install poetry

    ```shell
    pipx install poetry
    ```

3. Create a project with `maturin`

    ```shell
    maturin new --mixed <PROJECT_NAME>
    ```

4. Delete the `[build-system]` section from the generated `pyproject.toml` and run `poetry init`, rollback to maturin as a build system.
