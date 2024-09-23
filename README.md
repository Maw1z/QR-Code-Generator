# QR Code Generator
This project is a Python script that generates QR codes from user input and saves them in JPG, PNG, or SVG formats.

## Features
- Generate QR codes: Convert any text or URL into a QR code.
- Multiple formats: Save QR codes as .jpg, .png, or .svg.
- Customizable: Set custom file names and formats for each generated QR code.
- Generate multiple codes: Option to create more than one QR code during a single run.

## Prerequisites
- Python 3.x
- Required packages:
    - qrcode package (install via pip install qrcode)

## Usage
1.  Clone the repository or download the script.
2. Run the script in your terminal or IDE:
```bash
python script_name.py
```
3. Follow the prompts:
- Enter the data you want to encode in the QR code.
- Enter the desired file name (without extension).
- Choose the output format (jpg, png, or svg).
- The file will be saved in the current directory with the provided name and format.
4. Optionally, generate additional QR codes by responding to the prompt.

## Example
```sh
Enter your data to turn into QR code: https://example.com
Enter name of file without output type: example_qr
Enter output type (jpg, png, svg): png
QR code saved as example_qr.png

Generate another QR code? Enter 1 for Yes, 0 for No: 1
```

## License
MIT License

Copyright (c) 2024 Mawiz

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
