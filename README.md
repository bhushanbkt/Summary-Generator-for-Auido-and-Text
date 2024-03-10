# Summary-Generator-for-Auido-and-Text

 Summary Generator

## Overview
This project is a Title Summary Generator, utilizing Natural Language Processing (NLP) techniques to generate summaries for given texts. The application is implemented as a Streamlit web app, providing users with the ability to select specific domains such as health, business, news, sports, and politics. The summary generation process is conditioned on the selected domain; if the input text belongs to the chosen domain, the app generates a summary tailored to that domain.

## Features
- **Domain-specific Summarization**: Users can select from five different domains, and the summarization process is customized based on the selected domain.
- **Text and Audio Input**: The app supports both text and audio input. Users can either input text directly or upload audio files containing the text for summarization.
- **Downloadable Summaries**: Generated summaries can be downloaded in both text and audio formats, providing users with convenient access to the summarized content.

## Demo Video
A demo video showcasing the functionality of the Title Summary Generator web app is available [here](https://drive.google.com/file/d/1md0BkEiCSeh2tbzln9q3ptEKxV2CldSO/view?usp=sharing).

## Dataset
The underlying models for summarization were trained on diverse datasets corresponding to each domain. The datasets were carefully curated to ensure the effectiveness of domain-specific summarization.

## Things can be Downloded
Models code files and sample test Audio and text  available in the following Google Drive link:
[Download Models and Code](https://drive.google.com/drive/folders/1F4ZlhktqSCv3FtE7WPWH_W1bw7x1huqC?usp=sharing)

## Dependencies
- Python 3.9
- Streamlit
- NLP libraries (e.g., spaCy, NLTK)
- Other dependencies (listed in requirements.txt)

## Usage
1. Clone this repository to your local machine.
2. Install the required dependencies using `pip install -r requirements.txt`.
3. Run the Streamlit app using `streamlit run app.py`.
4. Select the desired domain from the dropdown menu.
5. Input the text or upload an audio file for summarization.
6. Click on the "Generate Summary" button to obtain the summary.
7. Download the generated summary in text or audio format, if desired.

## Folder Structure
- `data/`: Contains datasets and other relevant data.
- `models/`: Stores the trained NLP models.
- `utils/`: Utility functions for text processing and summarization.
- `app.py`: Main file containing the Streamlit application code.
- `requirements.txt`: List of Python dependencies.

## Contribution
Contributions to this project are welcome! If you encounter any issues or have suggestions for improvements, feel free to open an issue or submit a pull request.

## License
This project is licensed under the [MIT License](LICENSE).

## Acknowledgments
- We would like to thank the creators of Streamlit and various NLP libraries for their invaluable contributions to this project.

## Contact
For any inquiries or feedback, please contact [Bhushan Taksande](bhushant731@gmail.com).
