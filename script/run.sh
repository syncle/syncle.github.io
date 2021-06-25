#!/bin/sh

# bash function for checking return value of the script
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

run_and_check_success "python gen_html.py"
run_and_check_success "python gen_button_for_project_page.py"
run_and_check_success "python gen_headers.py"
run_and_check_success "python assemble_files.py"
run_and_check_success "python resize_images.py"
run_and_check_success "python gen_latex.py"
run_and_check_success "pdflatex --interaction=batchmode --jobname=cv_jaesik_park -output-directory .. ../cv.tex 2>&1 > /dev/null"