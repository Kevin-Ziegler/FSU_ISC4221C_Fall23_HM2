from answers_module import basic_io
def test_basic_io(capsys):
    import os
    if os.path.exists('../test_folder'):
        folder1 = '../test_folder'
    else:
        folder = 'test_folder'

    res = basic_io(folder)
    assert res['number_files'] ==  6
    assert res['files'] ==  ['f1.txt', 'f2', 'f3.txt', 'f4.py', 'f5.csv', 'folder1']
    assert res['file_or_folder'] ==  ['file', 'folder', 'file', 'file', 'file', 'folder']

    res = basic_io('../test_folder3')
    captured = capsys.readouterr()
    assert captured.out.lower().find("Folder does not exist".lower()) != -1

