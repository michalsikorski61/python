def manually_calling_close_on_a_file(filename):
    f = open(filename, 'r')
    f.write('Hello\n') # if this throws an error, the file will not be closed
    f.close()

# instead use with statement to automatically close the file
def manually_calling_close_on_a_file(filename):
    with open(filename,r) as f:
        f.write('Hello\n')

#  ensure the file is closed even if an exception occurs

# you can also use the finally block to ensure the file is closed
def finally_instead_of_context_manager(host,port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.connect((host,port))
        s.sendall(b'Hello, world')
    finally:
        s.close()