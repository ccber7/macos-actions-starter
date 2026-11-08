# macOS GitHub Actions Starter

Template proyek untuk menjalankan pengujian kode dan otomatisasi di mesin **macOS (`macos-latest`)** menggunakan GitHub Actions.

## Fitur Workflow (`macos-ci.yml`)

- **Runner**: `macos-latest` (Apple Silicon / ARM64 macOS).
- **Trigger Otomatis**: Berjalan setiap ada `push` atau `pull_request` ke branch `main`.
- **Trigger Manual (`workflow_dispatch`)**: Dapat dijalankan kapan saja melalui tab **Actions** di GitHub atau lewat GitHub CLI (`gh`), dengan opsi:
  - Memilih versi Python (`3.13`, `3.12`, `3.11`).
  - Menjalankan pengujian browser headless menggunakan Playwright (`run_playwright_check`).

## Cara Menjalankan via GitHub CLI (`gh`)

1. **Memicu workflow secara manual**:
   ```bash
   gh workflow run macos-ci.yml -f python_version=3.13 -f run_playwright_check=true
   ```

2. **Melihat status eksekusi workflow**:
   ```bash
   gh run list --workflow=macos-ci.yml
   ```

3. **Melihat log hasil eksekusi**:
   ```bash
   gh run watch
   ```
