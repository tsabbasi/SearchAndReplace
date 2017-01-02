import unittest
#import SearchAndReplace
from SearchAndReplace import find_replace_2, files_dictionary

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

class SearchAndReplaceTestCase(unittest.TestCase):
    def test_find_replace_2(search_string):
        find_replace_2('~/Desktop/TestFolder', 'HI', 'HELLO')
        updated_content = list(files_dictionary.values())
        for updated_content in files_dictionary:
            assertFalse(search_string in updated_content)

if __name__== '__main__':
    unittest.main()


''' iterate through directories, read files, and see if we can find replace_string TRUE '''
''' iterate through directories, read files, and see if we can find search_string FALSE

need to use regex pattern to ensure whole words are tested
i.e. check if <<<<pattern = r"\b{}\b".format(search_string)>>>> exists in content 
    if pattern not in content:

'''


# iterating through dicitonary values (content)
# assert False for search_string existing in content (values) of dictionary



