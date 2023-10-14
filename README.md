# debian_markdown_update
- This project was done under the project title "Experiment to modernize the Debian Wiki"
- The Script reads the News page in the Debian Wiki, parses the data, and writes its content to a file in Markdown.
----------------------------------------------------------------------------------------------------------------------------------------------------------------------
- Clone this project to your local computer.
  - `git clone https://github.com/boazleleina/debian_markdown_update.git` 
  
- To install project dependencies, run the code
     `pip install -r requirements.txt`

- The project dependencies are:
    - requests
    - beautifulsoup4

- cd into the directory with the file, and run
    - `python debian_markdown.py`

- If the dependencies are installed correctly and the file runs, a new .md file is created called 'debian_wiki.md'
- The project also has a test file that runs tests on all functions of the debian_markdown.py file. To run tests:
     - `python test_debian_markdown.py`
