upload_filename = "Chajka.txt"
dirname = "Directory1"


def test_upload_file(my_ftp):
    """
    check that where is no such file
    then upload it
    then check that it has appeared
    """
    assert not my_ftp.is_file_in_current_directory(filename=upload_filename)
    if my_ftp.upload_file(filename=upload_filename):
        assert my_ftp.is_file_in_current_directory(filename=upload_filename)


def test_create_dir(my_ftp):
    assert not my_ftp.is_file_in_current_directory(filename=dirname)
    if my_ftp.create_dir(dirname=dirname):
        assert my_ftp.is_file_in_current_directory(filename=dirname)


def test_delete_dir(my_ftp):
    if not my_ftp.is_file_in_current_directory(filename=dirname):
        my_ftp.create_dir(dirname)
    if my_ftp.delete_dir(dirname):
        assert not my_ftp.is_file_in_current_directory(filename=dirname)


def test_change_dir(my_ftp):
    if not my_ftp.is_file_in_current_directory(filename=dirname):
        my_ftp.create_dir(dirname)
    my_ftp.change_dir(dirname)
    assert dirname in my_ftp.get_current_dir()
