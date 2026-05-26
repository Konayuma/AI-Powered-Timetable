from dataclasses import dataclass, field


@dataclass(frozen=True)
class TimeSlot:
    day: str
    start_time: str
    end_time: str


@dataclass
class Timetable:
    entries: dict[str, list[TimeSlot]] = field(default_factory=dict)

    def add_entry(self, course_name: str, slot: TimeSlot) -> None:
        self.entries.setdefault(course_name, []).append(slot)

    def to_dict(self) -> dict[str, list[dict[str, str]]]:
        return {
            course: [
                {"day": slot.day, "start_time": slot.start_time, "end_time": slot.end_time}
                for slot in slots
            ]
            for course, slots in self.entries.items()
        }
