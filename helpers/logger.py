
import logging

log = logging.getLogger('2048.py')
_ch = logging.StreamHandler()
_formatter = logging.Formatter('[%(levelname)s:%(asctime)s] %(message)s')
_ch.setFormatter(_formatter)
log.addHandler(_ch)
log.setLevel(logging.DEBUG)
