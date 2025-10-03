# Multi-Modal Language Processing System

This project provides a suite of Python tools for performing multi-modal language processing tasks, combining audio, image, and text analysis. The system integrates functionalities including Optical Character Recognition (OCR), speech-to-text, text-to-speech, translation, and conversion between different modalities.

## Features

- **OCR**: Extract text from images using Optical Character Recognition.
- **Speech-to-Text**: Convert spoken audio files to text.
- **Text-to-Speech**: Generate speech audio from text input.
- **Translation**: Translate recognized or inputted text into different languages, including support for Arabic.
- **OCR to Audio**: Directly convert text extracted from images into audio.
- **Audio to Text**: Convert audio files into text for further processing.

## File Overview

- `OCR`: Run OCR tasks on images.
- `Audio to text`: Convert audio files to text.
- `OCR to Audio`: Convert text extracted from images to speech.
- `SpeechToText.py`: Python script for speech-to-text conversion.
- `TextToSpeech.py`: Python script for text-to-speech conversion.
- `ocr_to_translated_lang.py`: Translate OCR results into target languages.
- `translator_arabic_fixed.py`: Improved Arabic translation integration.
- `voice_to_translate.py`: Translate spoken audio to different languages.

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Yahya-Sabbagh/Multi-Modal-Language-Processing-System.git
   cd Multi-Modal-Language-Processing-System
   ```

2. **Install dependencies:**
   - Ensure you have Python 3.7+ installed.
   - Install required Python packages (see `requirements.txt` if provided):
     ```bash
     pip install -r requirements.txt
     ```

3. **Set up OCR (Tesseract):**
   - Follow instructions in `OCR-INSTALL-TESSERACT.txt` (if present) to install Tesseract OCR.

## Usage

Run individual scripts for each task. Example:
```bash
python SpeechToText.py input_audio.wav
python TextToSpeech.py "Hello, world!"
python ocr_to_translated_lang.py input_image.png --lang ar
```
Refer to script documentation or command-line help for details on arguments.

## Contributing

Contributions are welcome! Feel free to open issues or pull requests to improve features, add support for new languages, or fix bugs.

## License

This project is open source and available under the [MIT License](LICENSE).

## Author

SABBAGH Yahya
