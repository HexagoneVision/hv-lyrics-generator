<div align="center">
    <a href="https://github.com/HexagoneVision/hv-lyrics-generator/releases"><img src="https://img.shields.io/github/v/release/HexagoneVision/hv-lyrics-generator?label=lastest%20release&color=blue" alt="Latest release" /></a>
    <a href="https://github.com/HexagoneVision/hv-lyrics-generator/blob/main/LICENSE"><img src="https://img.shields.io/github/license/HexagoneVision/hv-lyrics-generator?label=license&color=white" alt="License" /></a>
    <a href="https://www.python.org/downloads/"><img src="https://img.shields.io/badge/Python-%3E%3D3.8-darkred?logo=python" alt="Python version" /></a>
</div>

# HV Lyrics Generator

**HV Lyrics Generator** is a Python tool to convert `.slrc` (segmented lyrics) files into LuaU scripts compatible with Roblox. This allows you to generate timed lyrics for songs in Roblox games or experiences.

More information about the `.slrc` format can be found in [docs/slrc_standard.md](docs/slrc_standard.md).

## Project Repository

You can find the project on GitHub: [https://github.com/HexagoneVision/hv-lyrics-generator](https://github.com/HexagoneVision/hv-lyrics-generator)

## Project Structure

- `CHANGELOG.md` – Project changelog.
- `CODE_OF_CONDUCT.md` – Guidelines for contributing.
- `CONTRIBUTING.md` – How to contribute to this project.
- `docs/` – Documentation files, including `.slrc` standard.
- `.github/` – GitHub-specific workflows and templates.
- `.gitignore` – Git ignore rules.
- `LICENSE` – GNU General Public License v3.
- `output/` – Default output folder for generated LuaU scripts.
- `ROADMAP.md` – Planned features and roadmap.
- `script.py` – Main Python script to convert `.slrc` to LuaU.
- `scripts/` – Additional scripts or utilities.
- `SECURITY.md` – Security policies.
- `tests/` – Unit tests and examples.

## Requirements

- Python 3.x

The project only uses Python standard libraries (`re`, `sys`), so no extra dependencies are needed.

## Installation

You can install required packages and Python via the provided `install.sh` script:

```bash
chmod +x install.sh
./install.sh
```

## Usage

You can run the converter script with command-line parameters or interactively:

### Using flags (any order):

```bash
python3 script.py --input path/to/lyrics.slrc --output path/to/song.luau --name "Song Name" --author "Song Author" --id 1234567890
```

### Interactive mode:

```bash
python3 script.py
```

The script will prompt you for any missing input.

### Output

The output LuaU script will contain:

- Song name, author, and Roblox SoundId
- All lyrics segmented with timing and duration
- Narration segments marked with `narrative = true`

## License

This project is licensed under the **GNU General Public License v3 (GPLv3)**.

Copyright (C) 2025 Hexagone Vision (hexagonevc.fr)

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
GNU General Public License for more details.

See the [LICENSE](LICENSE) file or [https://www.gnu.org/licenses/](https://www.gnu.org/licenses/) for details.

## Contributing

Please read [CONTRIBUTING.md](CONTRIBUTING.md) and [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md) before contributing.

## Security

For security issues, please refer to [SECURITY.md](SECURITY.md).

## Roadmap

Check [ROADMAP.md](ROADMAP.md) for upcoming features and improvements.
