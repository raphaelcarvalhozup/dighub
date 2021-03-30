import base64
import requests
import sys
import re

def converter(content, dork):

    string_base = dork

    space = dork.find(' ')

    if space != -1:
        string_parts = dork.split()
        dork = string_parts[0]

    string_length = len(dork)
    encoded_content = content
    decoded_64content = base64.standard_b64decode(encoded_content)
    decoded_content = decoded_64content.decode("UTF-8")

    lines = decoded_content.split('\n')

    code_position = decoded_content.find(dork)

    if code_position:
        code_line = [i for i, s in enumerate(lines) if dork in s]
        if code_line:
            print('Number of ocurrences: ', len(code_line))
            line = int(code_line[0]) + 1
            print('First occurrence line: ', line)
        else:
            string_parts = string_base.split(' ')
            componentsQt = len(string_parts)
            if componentsQt > 1:
                dork = string_parts[1]
                string_length = len(dork)
                code_line = [i for i, s in enumerate(lines) if dork in s]
            if code_line:
                print('Number of ocurrences: ', len(code_line))
                line = int(code_line[0]) + 1
                print('First occurrence line: ', line)
            else:
                return False
            
    string_end = (code_position+string_length-1)

    def second_break_before(text):
        if code_line[0] > 2:
            lines_start = text.rfind('\n', 0, decoded_content.rfind('\n', 0, code_position)-1)
            return lines_start
        elif code_line[0] == 0:
            lines_start = 0
        else:
            lines_start = text.rfind('\n', 0, decoded_content.rfind('\n', 0, code_position))
            return lines_start

    def second_break_after(text):
        if code_line[0] > 2:
            lines_end = text.find('\n', decoded_content.find('\n', string_end)+1)
            return lines_end
        else:
            lines_end = text.find('\n', decoded_content.find('\n', string_end))
            return lines_end

    start_break = second_break_before(decoded_content)

    end_break = second_break_after(decoded_content)

    code_part = decoded_content[start_break:end_break]

    return code_part
