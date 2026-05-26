from dataclasses import dataclass, field

from .timetable import TimeSlot, Timetable


@dataclass(frozen=True)
class CourseRequest:
    course_name: str
    preferred_slots: list[TimeSlot] = field(default_factory=list)


class BasicScheduler:
    def generate(self, course_requests: list[CourseRequest] | None = None) -> dict[str, list[dict[str, str]]]:
        timetable = Timetable()
        for request in course_requests or []:
            for slot in request.preferred_slots:
                timetable.add_entry(request.course_name, slot)
        return timetable.to_dict()
