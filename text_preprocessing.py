import argparse
import os
import re
from num2words import num2words


def remove_punct(args):

    output_dir = args.output_dir

    for text_file in os.listdir(args.input_dir):

        text_file_name = text_file.split(".")[0]

        with open(args.input_dir + text_file, "r") as fp:
            lines = fp.readlines()

        # because first 6 lines are NOT spoken out by speaker eg. course name, prof name and this is true for all pdfs
        lines = lines[6:]

        lines = [line.rstrip() for line in lines]
        lines = [line.lower() for line in lines]

        for line in lines:
            if line.__contains__(":"):
                new = line.replace(":", "")
                lines[lines.index(line)] = new


        # if refer slide time occurs as part of sentence in line or new line
        for line in lines:
            new = re.sub(r'\([a-z\s*0-9]+\)',"",line)
            lines[lines.index(line)] = new

        lines = [line for line in lines if line != ""]

        for line in lines:
            if line.__contains__(","):
                new = line.replace(",", "")
                lines[lines.index(line)] = new

        for line in lines:
            if line.__contains__("."):
                new = line.replace(".","")
                lines[lines.index(line)] = new

        for line in lines:
            if line.__contains__("?"):
                new = line.replace("?", "")
                lines[lines.index(line)] = new

        for line in lines:
            if line.__contains__(";"):
                new = line.replace(";", "")
                lines[lines.index(line)] = new

        for line in lines:
            if line.__contains__(".."):
                new = line.replace("..", "")
                lines[lines.index(line)] = new


        for line in lines:
            if line.__contains__("-"):
                new = line.replace("-", "")
                lines[lines.index(line)] = new

        for line in lines:
            if line.__contains__("--"):
                new = line.replace("--", "")
                lines[lines.index(line)] = new

        for line in lines:
            if line.__contains__("`"):
                new = line.replace("`", "")
                lines[lines.index(line)] = new

        for line in lines:
            if line.__contains__("/"):
                new = line.replace("/", "")
                lines[lines.index(line)] = new

        for line in lines:
            if line.__contains__(r"[\']"):
                new = line.replace(r"[\']", "")
                lines[lines.index(line)] = new

        #if empty spaces are generated because of above operations as sometimes "." occurs in new line
        lines = [line for line in lines if line != ""]

        #converting num to words from each line
        for line in lines:
            new_line = ''
            for word in line.rstrip().lstrip().split(' '):
                if word.isdigit():
                    new = num2words(int(word))
                    new_line = new_line + new + " "
                else:
                    new_line = new_line + word + " "
            lines[lines.index(line)] = new_line

        with open(f"{output_dir}/{text_file_name}.txt", 'w') as fp:
            for line in lines:
                fp.write(line + "\n")


if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument("--input_dir",type=str, help="Path of input directory with all txts")
    parser.add_argument("--output_dir", type=str, help="Path of output directory")
    args = parser.parse_args()
    remove_punct(args)