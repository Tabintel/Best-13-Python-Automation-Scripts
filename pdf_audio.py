import pyttsx3
import PyPDF2

# Open the PDF file
with open('example.pdf', 'rb') as pdf_file:
    pdf_reader = PyPDF2.PdfFileReader(pdf_file)

    # Initialize the text-to-speech engine
    speaker = pyttsx3.init()

    # Extract text from each page and convert to audio
    for page_num in range(pdf_reader.numPages):
        page = pdf_reader.getPage(page_num)
        text = page.extractText()

        # Convert text to speech
        speaker.say(text)

        # Save the speech to an audio file (in this case, MP3 format)
        speaker.save_to_file(text, f'page_{page_num}.mp3')

    # Run the text-to-speech engine
    speaker.runAndWait()