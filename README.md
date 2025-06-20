# pdfscripts



✅ Requirements
Make sure Python is installed.
If not: Download Python from here and install with "Add to PATH" checked.

.

🧱 Folder Structure (Create this before running)
your-folder/
├── input_pdfs/          ← Place all PDFs to edit here
│   ├── file1.pdf
│   ├── file2.pdf
├── output_pdfs/         ← Output files will be saved here (auto-created)
├── logo.png             ← Your logo image (PNG recommended)
├── script.py            ← The watermarking script


⚙️ Step-by-Step Setup
Install Python dependencies

Open Command Prompt or PowerShell and run:


pip install pymupdf

Download or create this folder structure (as above)

Place PDFs to be processed inside the input_pdfs folder.

Put your logo in the root folder and rename it to logo.png.

Edit the script (optional):

Change YourBrandName for watermark text

Update social_links in the script for your Instagram/Telegram

Run the script

In terminal, navigate to the folder and run:

python script.py
Check output_pdfs/ folder — all modified PDFs will be saved there.

🧼 Notes
Logo must be a .png image (transparent recommended).

Ensure you keep the input_pdfs and output_pdfs folder names unless modified in the script.

Works on any number of PDFs — just drop them in the input_pdfs folder.
