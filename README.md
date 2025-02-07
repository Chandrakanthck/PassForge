# PassForge - Word-Based Password Generator

##  Overview
**PassForge** is a Python-based password generator that transforms words into secure passwords. Users can choose to generate **a fixed number of passwords** or **all possible passwords** based on input criteria.

## Features  
- [x] Custom base word input  
- [x] Min/max password length  
- [x] Optional word slicing/permutation  
- [x] Special character customization  
- [x] Output to .txt file

## Installation
1. **Clone the repository:**
   ```sh
   git clone https://github.com/your-username/PassForge.git
   cd PassForge
   
2. **Run the Script**
   ```sh
   python passforge.py
   
3. **Usage**
   **Upon running the script, enter the required inputs:**
   ```sh
   Enter base word: example
   Min password length: 6
   Max password length: 8
   Enter allowed special characters (e.g., @!#): @#!
   Allow slicing? (y/n): y
   Generate (1) Fixed number or (2) All possible? Enter 1 or 2: 1
   Number of passwords to generate: 5


4. **Output (saved to passwords.txt):**
   **Word Slicing Enabled:**
   exampl1<br>
   exampl@<br>
   exampl9<br>
   example1<br>
   
   **Word Slicing Disabled:** <br>
   example2<br>
   example@<br>
   example9<br>
   example@9<br>

## Requirements <br>
   Python 3.x
   
## Contributing <br>
   Pull requests welcome! For major changes, open an issue first.

## License <br>
   This project is licensed under the MIT License.
