from typing import List, Dict


"""
Initial Ideas: large data set normally stored in file. 
1. Read from file
2. Parse string into Segments (segment names can repeat (cant use hash)
3. Parse segment into fields (fields can repeat, cant use hash) database would probably make these easier if I have time
4. Provide a simple GUI interface for iteration and searching through segments
*Search might be inefficient with this initial idea. O(num_segments*num_fields)*

Test Ideas:
1. Empty file
2. Single Segment, single fields
2. multi segment, multi fields
3. duplicate segment name
4. duplicate field name
5. segment with no fields
6. field without a segment?
"""


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


class SegmentController:
    def __init__(self, segments: List[Segment]) -> None:
        self._segments = segments

    def iterate_through_segments(self) -> None:
        for segment in self._segments:
            segment.print_info()

    def search_by_segment_name(self, search_val: str) -> None:
        for segment in self._segments:
            if segment.name() == search_val:
                print("\nSegment found matching search value: \n")
                segment.print_info()

    def search_by_field_name(self, search_val: str) -> None:
        for segment in self._segments:
            segment.find_field(search_val)


class SegmentParser:
    def parse_from_file(self, filename: str) -> List[Segment]:
        with open(filename) as f:
            file_data = f.read()

        return self.parse_from_string(file_data)

    @staticmethod
    def parse_from_string(segment_string: str) -> List[Segment]:
        segment_list = segment_string.split("||")
        if len(segment_list[-1]) == 0:
            del segment_list[-1]

        segments = []
        for segment in segment_list:
            segments.append(Segment(segment.split('|')))

        return segments


if __name__ == "__main__":
    parser = SegmentParser()
    seg_ctrl = SegmentController(parser.parse_from_file("../test1.txt"))

    seg_ctrl.iterate_through_segments()
    seg_ctrl.search_by_segment_name("NAM")
    seg_ctrl.search_by_field_name("DOB")
