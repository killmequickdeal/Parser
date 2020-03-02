"""
Riley Deal
Johnson Controls Interview Question
3/2/2020

controls reading in data & the main loop of the program
"""
import argparse

from SegmentUtilities.SegmentController import SegmentController


def menu() -> str:
    """
    Prints the choices for execution and returns the users' choice
    :returns: the users choice of function to execute
    """
    print("{1} Iterate through segments \n"
          "{2} Search by segment name \n"
          "{3} Search by field name \n"
          "{4} Quit \n"
          "Make a selection: ")
    return input()


if __name__ == "__main__":
    # read in file name from arguments
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument('-f', "--file", dest="file",
                            help="data file containing segments", nargs="?", default="../test1.txt")
    args = arg_parser.parse_args()

    # parse the file and give the segments to the segment controller
    seg_ctrl = SegmentController()
    seg_ctrl.parse_from_file(args.file)

    # continue execution until the user quits
    keep_executing = True
    while keep_executing:
        input_val = menu()

        if input_val == "1":
            print("Press 'enter' to iterate through the segments and their fields \n"
                  "In order to exit early, type 'exit'\n")
            seg_ctrl.iterate_through_segments()
        elif input_val == "2":
            segment_name = input("Input a segment name to search by: ")
            seg_ctrl.search_by_segment_name(segment_name)
        elif input_val == "3":
            field_name = input("Input a field name to search by ")
            seg_ctrl.search_by_field_name(field_name)
        elif input_val == "4":
            keep_executing = False
        else:
            print("Invalid input")


