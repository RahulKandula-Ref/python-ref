
def g_sheets():
    all_sheets = {

    }
    def read_all():
        nonlocal all_sheets
        all_sheets.update({
            'tracker': 'nv 24 tracker',
            'notes': 'very serious notes'
        })
    def update_sheet(sheet, new_note):
        nonlocal all_sheets
        if sheet not in all_sheets:
            return
        all_sheets[sheet] += new_note
    def read_sheet(sheet):
        if sheet not in all_sheets:
            return
        else:
            return all_sheets[sheet]

    read_all()    
    return (update_sheet, read_sheet)
    
        

def test():
    print(f"you have imported g_sheets_mod succesfully and its name is {__name__}")

if __name__ == "__main__":
    print('There are no errors comiling this module! Feel free to use it.')


