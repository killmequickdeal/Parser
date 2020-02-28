from typing import List
from SegmentUtilities.Segment import Segment


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
