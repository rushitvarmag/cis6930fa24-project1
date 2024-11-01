# cis6930fa24-project1
Name: Manoj Kumar Galla

# Project Description
This Python package accepts a glob pattern, output directory, and file flags to locate matching files, process each one by masking names, phone numbers, addresses, and dates, and generate document statistics in stderr, stdout, or a specified stats file. The censored content is then saved in a new file with a '.censored' extension.

PROJECT STRUCTURE

The project is organized with an initial redactor file that triggers the process, leveraging four modules—redact_dates, redact_phone, redact_address, redact_names, and redact_concepts—to carry out the specified actions. All these files are located in the root directory.

The downloaded files is saved into the directory path given in the --output flag. 

TESTING
This project contains test files that test all the redactor modules along with the stats. each test case to test redactor modules is written in test_redactor.py.


# Installation
pipenv install

## Run the code
pipenv run python redactor.py --input '*.'                     --names --dates --phones --address  --concept 'kid'                  --output 'files/'                     --stats stderr

## Testing
pipenv run python3 -m pytest <test_file>

## Functions
#### redactor.py \
redact_names() - This function detects and redacts names from an input text

redact_dates() - This function detects and redacts dates from an input text

redact_phones() - This function detects and redacts phones from an input text

redact_address() - This function detects and redacts address from an input text

redact_concepts() - This function detects and redacts concepts from an input text

process_file() - Proesses each file and handles the output of each redactor function

write_stats() - This function writes stats to the output

 