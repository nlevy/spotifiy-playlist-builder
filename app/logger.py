import logging
import os

# Create logger
log_level = logging.INFO if os.getenv('FLASK_ENV') == 'production' else logging.DEBUG
logger = logging.getLogger('spotify_playlist')
logger.setLevel(log_level)

# Create console handler
ch = logging.StreamHandler()
ch.setLevel(log_level)

# Create formatter
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# Add formatter to ch
ch.setFormatter(formatter)

# Add ch to logger
logger.addHandler(ch) 