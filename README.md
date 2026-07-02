# sysmon

A command-line system monitor for Linux, written in Python — a lightweight, from-scratch take on tools like `htop` and `top`.

`sysmon` reads directly from the Linux `/proc` filesystem to report live CPU, memory, and process information, with no external monitoring dependencies. Built as a hands-on study of how system-monitoring tools actually work under the hood.

## Status

🚧 Early development — built feature by feature. See the roadmap below.

## Planned features

- [ ] CPU usage (overall and per-core) from `/proc/stat`
- [ ] Memory usage from `/proc/meminfo`
- [ ] Top processes by CPU / memory from `/proc/[pid]/`
- [ ] Live auto-refreshing terminal dashboard
- [ ] Configurable CLI with `argparse` (refresh rate, output format)
- [ ] Docker container for portable deployment
- [ ] Unit tests

## Requirements

- Linux (reads the `/proc` filesystem)
- Python 3.10+

## Usage

_Coming soon as features land._

## Why this project

Built as part of a systems + AI/ML engineering track — understanding Linux internals and writing clean, dependency-light Python is the foundation for infrastructure and ML systems work.

## License

MIT