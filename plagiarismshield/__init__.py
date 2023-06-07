
import glob, os
from pathlib import Path
from PyPDF2 import PdfReader
from difflib import SequenceMatcher
import argparse
import progressbar

txt_extension_list = [".txt", ".nc", ".py", ".c", ".cpp", ".java", ".js", ".html", ".css", ".php", ".sql", ".xml", ".json", ".md"]
pdf_file_list = [".pdf"]

class PlagiarismShield:
    def __init__(self):
        pass
    
        
    def compare_content(self,file1,file2,file_type=None):
        if os.path.splitext(file1)[1] in pdf_file_list or file_type == "pdf":
            text1 = self.extract_text_from_pdf(file1)
        #elif os.path.splitext(file1)[1] in txt_extension_list or file_type == "txt":
        #    text1 = Path(file1).read_text()
        else:
            text1 = Path(file1).read_text()
            
        if os.path.splitext(file2)[1] in pdf_file_list or file_type == "pdf":
            text2 = self.extract_text_from_pdf(file2)
        else:
            text2 = Path(file2).read_text()
        
        return self.compute_similarity_score(text1, text2)


    def extract_text_from_pdf(self,file_path):
        final_text = ""
        text = []
        # creating a pdf reader object
        reader = PdfReader(file_path)
        # getting a specific page from the pdf file
        text = [page.extract_text() for page in reader.pages]
        # extracting text from page
        final_text = final_text.join(text)
        final_text=" ".join(final_text.split())
        return final_text


    def compute_similarity_score(self,text1,text2):
        similarity_ratio = SequenceMatcher(None, text1, text2).ratio()
        return similarity_ratio

    def compare_pdf_content(self,file1, file2):
        text1 = self.extract_text_from_pdf(file1)
        text2 = self.extract_text_from_pdf(file2)
        # Compare the text content of the PDFs here
        similarity_score = self.compute_similarity_score(text1, text2)
        return similarity_score


    def search_files_in_dir(self,directory,file_name,recoursive=False):
        if recoursive:
            return [glob.glob(directory + "/**/" + file_name, recursive=True)]
        else:
            return [glob.glob(directory + "/" + file_name, recursive=False)]
            
                
    def compare_files(self,file_list:list,similarity_threshold:float,file_type=None):
        results = {}
        list_threshold = []
        if len(file_list) > 0 and file_list is not None:
            size_list = len(file_list)*len(file_list)
            bar = progressbar.ProgressBar(maxval=size_list, widgets=[progressbar.Bar('=', '[', ']'), ' ', progressbar.Percentage()])
            bar.start()
            for i in range(len(file_list)):
                file1 = file_list[i]
                results[file1] = {}
                for j in range(i + 1, len(file_list)):
                    file2 = file_list[j]
                    similarity = self.compare_content(file1, file2, file_type=file_type)
                    results[file1][file2] = similarity
                    if(similarity)>=similarity_threshold:
                        #print(f"Comparing {file1} and {file2}: {similarity}")
                        list_threshold.append(f"Comparing {file1} and {file2}: {similarity}")
                        
                    bar.update(i*j)
            bar.finish()
        return results,list_threshold   

