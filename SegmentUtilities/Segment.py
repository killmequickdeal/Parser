"""
Riley Deal
Johnson Controls Interview Question
3/2/2020

The segment is the core of the interview question. Each segment
has a name and between [0, n] fields
"""
from typing import List, Dict


class Segment:
    def __init__(self, raw_segment: List[str]) -> None:
        """
        splits the raw_segment list into the segment name and fields dictionary
        :param raw_segment: a list of all pieces of the segment, separated on '|'
        """
        self._segment_name = raw_segment[0]
        self._size = len(raw_segment)
        if self._size > 1:
            # split the fields into their name and value i.e) FNAFred -> FNA: Fred
            self._fields = {field[0:3]: field[3:] for field in raw_segment[1:]}
        else:
            self._fields = {}

    def name(self) -> str:
        """
        :return: the name of the segment
        """
        return self._segment_name

    def fields(self) -> Dict[str, str]:
        """
        :return: dictionary of fields mapping from name to value
        """
        return self._fields

    def print_info(self) -> None:
        """
        Print all information about the segment
        """
        print(self.name())
        for key, value in self.fields().items():
            print(f"    {key}: {value}")
        print()

    def find_field(self, field: str) -> None:
        """
        loop through all fields in the segment to see if it contains the specified field
        :param field: the field to check for in the field dictionary
        """
        if field in self._fields:
            print("\nField found matching search value: \n")
            print(f"{self._segment_name}\n    {field}: {self._fields[field]}\n")

    def __iter__(self):
        """
        Grab the iterator for the field dictionary for use in the segment iterator.
        """
        self._field_iter = self._fields.__iter__()
        self._return_name_on_iteration = True
        return self

    def __next__(self) -> str:
        """
        Iterates over the pair of segment name and field dictionary
        Field dictionary will raise StopIteration when done iterating, unnecessary to raise it in segment
        :return: the current value in the segment
        """
        if self._return_name_on_iteration:
            self._return_name_on_iteration = False
            return f"Segment -> {self.name()}"
        else:
            key = self._field_iter.__next__()
            return f"   Field -> {key}: {self._fields[key]}"
