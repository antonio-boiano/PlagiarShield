#!/usr/bin/env python

import argparse
import os
from plagiarismshield import PlagiarismShield


def main():
    
    plagiar_shield = PlagiarismShield()
      
    parser = argparse.ArgumentParser(description="Plagiarism Shield \n This script is used to compare files in a directory and check if students copied among each other" )
    parser.add_argument('directory', type=str, help='directory to search for files')
    parser.add_argument('--file', '-f',  metavar='',type=str,required=True, help="file extension to search for e.g. '*.txt', 'homework*.pdf', '*route.nc'" )
    parser.add_argument('--filetype', '-t', metavar='',type=str, required=False, default=None, help="force file type e.g. 'pdf', 'txt', 'nc'")
    parser.add_argument('--similarity', '-s', metavar='',type=float, required=False, default=0.8, help="similarity threshold to consider two files as similar")

    
    group = parser.add_mutually_exclusive_group()

    group.add_argument('-r',  action='store_true', help="recoursive search in subdirectories")
    group.add_argument('-R', action='store_true', help="recoursive search in subdirectories")

    args = parser.parse_args()
    recoursive = args.r or args.R
    
    file_list = plagiar_shield.search_files_in_dir(args.directory,args.file,recoursive)
    results,list_threshold  = plagiar_shield.compare_files(file_list,args.similarity,file_type=args.filetype)
    print(list_threshold)
  

if __name__ == "__main__":
  main()