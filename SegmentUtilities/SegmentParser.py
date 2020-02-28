from typing import List
from SegmentUtilities.Segment import Segment


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
