from g_sheets_mod import g_sheets as gsheets
from rps import rps_game

(g_update, g_read) = ( gsheets() )
print(g_read('tracker'))
g_update('notes', '.\nmore serious notes')
print(g_read('notes'))

rps_game()

