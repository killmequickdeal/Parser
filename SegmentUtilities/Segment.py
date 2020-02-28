from typing import List, Dict


class Segment:
    def __init__(self, raw_segment: List[str]) -> None:
        self._segment_name = raw_segment[0]
        if len(raw_segment) > 1:
            self._fields = {field[0:3]: field[3:] for field in raw_segment[1:]}
        else:
            self._fields = {}

    def name(self) -> str:
        return self._segment_name

    def fields(self) -> Dict[str, str]:
        return self._fields

    def print_info(self) -> None:
        print(self.name())
        for key, value in self.fields().items():
            print(f"    {key}: {value}")

    def find_field(self, field: str) -> None:
        if field in self._fields:
            print("\nField found matching search value: \n")
            print(f"{self._segment_name}\n    {field}: {self._fields[field]}\n")

