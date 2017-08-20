import re
import numpy as np



class primary_search():
    
    def __init__(self):
        pass

    def clean_data(self,data):
        for primary_segment in data:
            for row in primary_segment:
                for cell in row:
                    if type(cell) is dict:
                        if cell['text'] == '':
                            del cell
                        else:
                            cell['text'] = cell['text'].lower()
                    else:
                        del cell
        return data

    def locator(self,any_list,identifier):
        new_list = []
        if type(any_list) is not dict:
            if len(any_list) >= identifier+2:
                # new_list.extend([any_list[identifier-2],any_list[identifier-1],any_list[identifier],any_list[identifier+1],any_list[identifier+2]])
                new_list = any_list[identifier-2:identifier+2]
            elif len(any_list) >= identifier+1:
                # new_list.extend([any_list[identifier-2],any_list[identifier-1],any_list[identifier],any_list[identifier+1]])
                new_list = any_list[identifier-2:identifier+1]
            else:
                new_list = any_list
            return new_list


    def data_division_start(self,data_list,key_word,index_of_start_idetifier,identifier_row,identifier_column):
        start= []
        for primary_segment in range(len(data_list)):
            for row in self.locator(data_list[primary_segment],identifier_row):
                if type(row) is dict:
                    break
                for column_offset in range(len(self.locator(row,identifier_column))):
                    if self.locator(row,identifier_column)[column_offset]['text'].startswith(key_word) or key_word in self.locator(row,identifier_column)[column_offset]['text']:
                        start = primary_segment
                        return start
                    

    def data_division_end(self,data_list,key_word,test_start_index):
        end= None
        end_found = False
        for primary_segment in range(test_start_index,len(data_list)):
            for row in data_list[primary_segment]:
                for column in row:
                    if type(column) is dict:
                        if column['text'].startswith(key_word):
                                end = primary_segment
                                end_found = True
                                break
                if end_found:
                    break
            if end_found:
                break
        return end




class secondary_search():

    def __init__(self):
        pass

    def secondary_division(self,start_index,end_index,data_list):
        divided_data = []
        for primary_segment in range(start_index,end_index+1):
            divided_data.append(data_list[primary_segment])

        return divided_data





    