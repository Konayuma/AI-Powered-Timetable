# AI-Powered-Timetable

A starter scaffold for an AI-assisted timetable planning project.

## Project Structure

- `docs/SRS.md` - Software Requirements Specification
- `docs/SAMPLE_TEST_CASES_AND_FINDINGS.md` - Sample test cases and findings
- `docs/UML_CLASS_DIAGRAM.md` - Class diagram (Mermaid)
- `docs/UML_SEQUENCE_DIAGRAM.md` - Sequence diagram (Mermaid)
- `src/timetable.py` - Core timetable data model scaffold
- `src/scheduler.py` - Basic scheduler interface scaffold

## Quick Start

No build/test tooling is configured yet.  
You can run a basic Python smoke check:

```bash
python -c "from src.scheduler import BasicScheduler; print(BasicScheduler().generate())"
```