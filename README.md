# Meme-Generator
<p>Meme generator is a CLI and Web-application based Meme-generator program.</p>
This program uses different Python libraries and the flask Web-framework to encapsulate the functionalities of a CLI-based tool as well as a web-based service. Meme generator can generate random memes on each request and can also create customized memes as per user inputs, by taking an input Image file and Quote/Caption texts for the custom made memes. As mentioned above, this software can be used as both a CLI based tool, as well as a web-application.

## Setup and Running of the program-
* On your computer, clone this repository or download the zip files and extract it.
* After the extraction, move to the "src" directory, which is the root directory for the actual executable files.
* To download and install all the dependencies and sub-dependencies to run this program, use "`pip install -r requirtements.txt`" command in your terminal .
* Also to use the Web-based service you can run "`python3 app.py`" command in your terminal and browse to the mentioned URL in the terminal through your browser.
* To use the CLI-based interface, run "`python3 meme.py`" command in your terminal. You can use "`python3 meme.py -h`" for any further help regarding the use cases of the CLI based interface.

## Roles and brief description of the modules and sub-modules-
> ### QuoteEngine Modue-
> * The **`QuoteEngine` Module** is responsible for the processing of raw input quote texts as available in the varied file-formats, viz. "CSV", "PDF", "Txt", "Docx", etc. to create caption-quotes for meme images.
> * It has four different sub-modules namely **`DocxIngester`**, **`TextIngester`**, **`PDFIngester`**, and **`CSVIngester`** modules, all of which have the primary functionality to ingest or process text-based quotes from different file formats, as per their specifications, for using them to caption the memes.
> * The import of text-based quotes are not done directly through the above mentioned submodules, but rather through an encapsulating object namely **`Ingester`** module, which again is a submodule of the **`QuoteEngine Module`** and this sub-module is responsible to import the files of different file-formats and ingest/process it depending on its file-format by using the above mentioned "Ingesting modules" and returning a **`QuoteModel` Object** .

> ### MemeEngine Modue-
> * The **MemeEngine Module** is responsible for the actual processing of raw input image files and quote texts to create meme images.
> * It has a sub-module named **MemeEngine**, with a class of same name, which processes the **`QuoteModel` Object**, as returned by the **`QuoteEngine` Module**, and uses the **Python `Pillow (PIL)`** library to process the input image file and captions the quote text over it and henceforth after resizing and all other preprocessing returns the Meme-Image file.

## Brief descriptions of the dependencies and libraries used-
> ### `py-docx` 
> * The **`py-docx` python library** is responsible for the processing of raw input "docx" files to ingest and extract quote texts from them, to create caption-quotes for meme images.

> ### `pandas`
> * The **`pandas` library** is responsible for the processing of raw input "CSV" files to ingest and extract quote texts from them, to create caption-quotes for meme images.

> ### `pdftotext`
> * The **`pdftotext` CLI tool** is responsible for the processing of raw input "PDF" files to ingest and extract quote texts from them, to create caption-quotes for meme images. 
> * To achieve the above mentioned functonalities, **`pdftotext`** first converts the "PDF" files to "txt" files and then the contents are then processed as processed for any "txt" based file in python. 

> ### `pillow (PIL)`
> * The **`pillow (PIL)` library** is used to manipuate image files and the library has exhaustive set of functinalities to work with images.
> * For the "Meme Generator" program, it is responsible for the processing of raw input image files as available in the varied file-formats, viz. ".jpg", ".svg", ".png", etc. to manipulate the images and draw text over them to get captioned quotes and hence return the meme images.

> ### `requests`
> * The **`requests` module** is responsible for the fetching and downloading of the custom input images as provided in the form of web-urls, to create customized meme images.

> ### `flask`
> * The **`flask` framework** is the main backbone of the web-based service as provided by the "Meme Generator".
> * It is the actual web-framework which instantiates and initializes Server to handle the requests and serves the Memes as response to the users, as per the requests. 

