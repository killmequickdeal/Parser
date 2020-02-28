from SegmentUtilities.SegmentController import SegmentController
from SegmentUtilities.SegmentParser import SegmentParser

if __name__ == "__main__":
    parser = SegmentParser()
    seg_ctrl = SegmentController(parser.parse_from_file("../test1.txt"))

    seg_ctrl.iterate_through_segments()
    seg_ctrl.search_by_segment_name("NAM")
    seg_ctrl.search_by_field_name("DOB")
