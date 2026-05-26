# Sample Test Cases and Findings

## Test Case 1: Empty Input

### Input
- No courses
- No constraints

### Expected Result
- Returns an empty timetable structure.

### Finding
- Scaffold implementation returns a default object with no slots, as expected.

---

## Test Case 2: Single Course, Single Slot

### Input
- Course: `Math101`
- Allowed slot: Monday 09:00-10:00

### Expected Result
- Timetable includes one entry for `Math101` at the specified time.

### Finding
- Current scaffold stores requested slots and surfaces them in output.

---

## Test Case 3: Conflicting Slots

### Input
- `Math101`: Monday 09:00-10:00
- `Physics101`: Monday 09:00-10:00

### Expected Result
- Conflict detected or one slot rejected.

### Finding
- Conflict-resolution is marked for future implementation; tracked as a known gap.
