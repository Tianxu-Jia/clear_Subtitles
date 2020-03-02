import argparse
import re

parser = argparse.ArgumentParser(description="clearn srt subtitle file and save it as txt file", argument_default=argparse.SUPPRESS)
parser.add_argument('-i', '--input',  type=str, help='input subtitle file')
args = parser.parse_args()

file = args.input
out_file = file[:-4] + '.txt'

fp_out = open(out_file, 'w')

start_pattern = re.compile('<font.*">')
end_pattern = re.compile('</font>')
shark_pattern = re.compile('#')

with open(file) as fp:
    lines = fp.readlines()
    for line in lines:        
        if (not line[:-1].isdigit()) and (not re.search('-->', line[:-1])) and (len(line)>1):
            ll = line.split('</font>')
            the_line=''
            for L in ll:
                text = re.sub(start_pattern, '', L)
                text = re.sub(end_pattern, '', text)
                the_line += text
            
            the_line = re.sub(shark_pattern, '', the_line)
            print(the_line)
            fp_out.write(the_line)  
        
fp_out.close() 
        