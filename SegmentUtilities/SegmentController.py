"""
Riley Deal
Johnson Controls Interview Question
3/2/2020

SegmentController is in charge of interactions between the user and the segments
"""
from SegmentUtilities.Segment import Segment


class SegmentController:
    def __init__(self) -> None:
        self._segments = []

    def iterate_through_segments(self) -> None:
        """
        iterate through each segment and each value in the segments
        Print the data for the user to see, and give the option of early termination
        """
        for segment in self._segments:
            for data in segment:
                print(data)
                iter_input = input()
                if iter_input.upper() == "EXIT":
                    return

    def search_by_segment_name(self, search_val: str) -> None:
        """
        Loop through all segments and print any with names matching the search value
        :param search_val: the segment name to search for throughout all segments
        """
        for segment in self._segments:
            if segment.name() == search_val:
                print("\nSegment found matching search value: \n")
                segment.print_info()

    def search_by_field_name(self, search_val: str) -> None:
        """
        Loop through all fields and print any with names matching the search value
        :param search_val: the field name to search for throughout all fields in all segments
        """
        for segment in self._segments:
            segment.find_field(search_val)

    def parse_from_file(self, filename: str) -> None:
        """
        Read in segments from a given filename
        :param filename: the name of the file
        """
        with open(filename) as f:
            file_data = f.read()

        self.parse_from_string(file_data)

    def parse_from_string(self, segment_string: str) -> None:
        """
        Read in segments from a string
        :param segment_string: the string containing the segments to read from
        """
        segment_list = segment_string.split("||")

        # if string ended in || the last segment will be empty string
        if len(segment_list[-1]) == 0:
            del segment_list[-1]

        for segment in segment_list:
            self._segments.append(Segment(segment.split('|')))

