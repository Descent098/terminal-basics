from ezprez.core import *
from ezprez.components import *

# Add in your slides here
Slide("Hello world", "for images, put them in /images and just use their filename", Image("low poly ice caps", "kieran-wood-lp-ice-caps-4k-w-peng.jpg"))

# Setup the presentation
presentation_title = "Here is the presentation title" # TODO: Fill in with the title of your presentation
presentation_description = "This is the description of the presentation" # TODO: Fill in with the description of your presentation
presentation_url = "https://example.com" # TODO: Fill in with the url of your presentation
prez = Presentation(presentation_title, presentation_description, presentation_url)

# Export the files to the current directory at /Presentation, do not change this if you want to use the auto-deployment
prez.export(".", force=True, folder_name="Presentation")
