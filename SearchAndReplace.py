#!/usr/bin/python -u
# -*- coding: utf-8 -*-

"""
SearchAndReplace.py

Overview:

    Write a search and replace method in Python that will modify all files
    in a directory (including subdirectories) replacing all instances of
    a 'search string' with a 'replacement string'.

Example:

    phython SearchAndReplace.py --dir ~/ProjectDir --search 'Foo=1' --replace 'Bar=2'

Requirements:

    1. Use python
    2. Use only native python libraries
    3. Program should be executable via shell (E.G. MacOS Terminal)

Grading:

    Code exersize will be graded using using the follwing criteria.
    1. Does it work.
    2. Code Style & Commenting.
    3. Are Test Cases Included.
    4. Approaches to edge cases and potential misuse of the program.


Example Edge Cases:
    1. What happens if the search string is ''?
    2. What happend if a file is read only?
    ...

"""

# HINT: Use the 'os' module to search for files.
import os

# HINT: Use the 'argparse' module to parse command line arguments
import argparse

# regex module
import re


# writeable files' filepaths (key) with the corresponding content (value)
files_dictionary = {}

# list of read-only files
rejected_files = []

# list of updated files
updated_files = []


def search_and_replace(directory, search_string, replace_string):
    """The main method.


    This method will search a directory (and sub directories) for
    search_string and replace the string with replace_string.


    Arguments:
        directory:      (String) The directory to search in
        search_string:  (String) The string to search for
        replace_string: (String) Replace search_string with this string
    """

    # regex search ensuring no special characters exist in search_string (edge case)
    if (re.search("^[a-zA-Z0-9_]*$", search_string) or search_string == " "):

        # regex operation ensuring strictly whole words are being accounted for and not partial
        # e.g. search_string = 'HELLO' ---> Replace HELLO, not HELLOWORLD
        pattern = r"\b{}\b".format(search_string)

        # helper function (find below) to retrieve a dictionary of writable files with their content 
        get_files(directory)

        # iterating through dictionary that contains filepaths as key and the content as the values
        for filepath, content  in files_dictionary.iteritems():

            # search_string is not an empty string : regex operation (with pattern defined above) applied ensuring only whole words are being replaced
            if (search_string != " "):
                content = re.sub(pattern, replace_string, content)

            # search_string is an empty string : replace function applied since regex operation (according to pattern defined above) does not account for words starting with a space
            else:
                # since this is an edge case, a message about the execution is printed
		print("Replacing all empty spaces within file in directory {}\n".format(filepath))
                content = content.replace(search_string, replace_string)

            # overwriting each file with the updates performed above
            with open(filepath, "w") as f:
                f.write(content)

	    # adding files that were overwritten to updated files list
	    updated_files.append(filepath)

        print('SUCCESS: All instances of the string {} within the directory {} were replaced with {}\n'.format(search_string, directory, replace_string))

        # overwritten files
        print("These files were updated:\n")
        for files in updated_files:
            print(files)

        # read-only files
        print("\nThese files were rejected:\n")
        for files in rejected_files:
            print(files)

    # special character was entered in the search string
    else:        
        print('\nInvalid search string — special characters not allowed\n')
    #return pattern, content


def get_files(directory):
    """Helper method.

	This method iterates through directories and subdirectories and adds the writable files a dictionary
	with their corresponding content.

	Dictionary Key = filepath
	Dictionary Value = filecontent

    """
    # iterating through all subdirectories within the current directory
    for path, dirs, files in os.walk(os.path.abspath(directory)):
        for filename in files:

            # filepath with the current file included
            filepath = os.path.join(path, filename)

            # EDGE CASE - file is read-only (not writable) : user notified about the file and the path where it resides
            if (os.access(filepath, os.W_OK) == False):
                print('\n\nWARNING: The file {} at the path {} is not writable, please change permissions and try again.\n'.format(filename, filepath))

		# adding read-only file to rejected files list
		rejected_files.append(filepath)

            # the file is writable -- read content and pair with corresponding filepath in files_dictionary
            else:
                with open(filepath) as f:
                    filecontent = f.read()

		    # pairing filepath with it's content in dictionary
                    files_dictionary[filepath] = filecontent

    return files_dictionary


if __name__ == '__main__':

    # Parse Command Line Arguments

    parser = argparse.ArgumentParser(description='Perform search and replace within directory — including subdirectories')
    parser.add_argument("--dir", help="directory: (String) The directory to search in")
    parser.add_argument("--search", help="search_string: (String) The string to search for")
    parser.add_argument("--replace", help="replace_string: (String) Replace search_string with this string")
    args = parser.parse_args()

    # parsed values for arguments

    directory = args.dir
    search_string = args.search
    replace_string = args.replace

    # Call search_and_replace(...)

    search_and_replace(directory, search_string, replace_string)
    
    

""" COMMENTS AREA - BELOW ARE SOME NOTES ON PROBLEMS OR ISSUES I TACKLED OR CAME ACCROSS """

# IN PROGRESS
# test cases - program is suppose to executed through terminal, though test cases require calling the main function with hardcoded values
    # clarification needed on how to proceed

# TEST
# read files and check if search_string still exists anywhere

    #Test Cases: (all tried manually)

        #test : search_string -> replace_string

        #assertFalse : HELLO -> HI          
        #assertFalse : HI -> HELLO          
        #assertFalse : 1 -> HEY
        #assertFalse : " " -> *
        #INVALID : * -> " "
        #INVALID : * -> !
        #INVALID : ! -> 1
        #assertFalse : HELLO -> " "

# COMPLETED
# strings within a word i.e. partial world : do not replace in such case ----> DONE
# EDGE CASE - special characters after search_string : replace in such case ---> DONE
# EDGE CASE - file is read only : print file name that was read only and notify ---> DONE
    # better implementation for the above case would be to ask user if they want to change file settings and then ask for password to continue
# program is executable through command line ---> DONE
# function to filter file types ---> DONE
    # taken out as this was not needed : would use fnmatch to filter file types such as .txt, .py, etc...
# when file is empty : program should continue --> DONE
# EDGE CASE - search string is '' : empty spaces in the file will be replaced, user is notified when this is being executed --—> DONE
# EDGE CASE - check for special characters : special characters will be considered invalid ---> DONE
# list files that were overwritten ---> DONE
# list files that were not rejected ---> DONE
