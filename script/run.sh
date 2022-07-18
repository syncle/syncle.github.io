#!/bin/sh

### bash function for checking return value of the script
run_and_check_success()
{
	$1					# run script
	success=$?			# store return value of the script
	if [ $success -ne 0 ]; then
	    echo "Job failed:: $1"
	else
		echo "Job success:: $1"
	fi
}

### prepare images for the publication page
run_and_check_success "python resize_images.py"

### make html files
run_and_check_success "python gen_index.py"
run_and_check_success "python gen_publication_html.py"
run_and_check_success "python gen_button_for_project_page.py"
run_and_check_success "python gen_headers.py"
run_and_check_success "python assemble_files.py"

### build latex cv.pdf
run_and_check_success "python gen_latex.py"
run_and_check_success "pdflatex --interaction=batchmode --jobname=cv -output-directory ../source/latex/build ../source/latex/cv.tex 2>&1 > /dev/null"
### compress cv.pdf (1/10 smaller)
run_and_check_success "gs -sDEVICE=pdfwrite -dCompatibilityLevel=1.5 -dNOPAUSE -dQUIET -dBATCH -dPrinted=false -sOutputFile=../cv_jaesik_park.pdf ../source/latex/build/cv.pdf"
run_and_check_success "rm ../source/latex/cv.tex"
