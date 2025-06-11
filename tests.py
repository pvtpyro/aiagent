# from functions import get_files_info, get_file_content, write_file, run_python_file, call_function

from run_python import run_python_file

def test():
    result = run_python_file("calculator", "main.py")
    print(result)

    result = run_python_file("calculator", "tests.py")
    print(result)

    result = run_python_file("calculator", "../main.py")
    print(result)

    result = run_python_file("calculator", "nonexistent.py")
    print(result)


if __name__ == "__main__":
    test()


# get_files_info
# result = get_files_info.get_files_info("calculator", ".")
# print(result)
# result = get_files_info.get_files_info("calculator", "pkg")
# print(result)
# result = get_files_info.get_files_info("calculator", "/bin")
# print(result)
# result = get_files_info.get_files_info("calculator", "../")
# print(result)


# get_file_content
# result = get_file_content.get_file_content("calculator", "main.py")
# print(result)
# result = get_file_content.get_file_content("calculator", "pkg/calculator.py")
# print(result)
# result = get_file_content.get_file_content("calculator", "/bin/cat")
# print(result)
# result = get_file_content.get_file_content("calculator", "lorem.txt")
# print(result)

# result = write_file.write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum")
# print(result)
# result = write_file.write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet")
# print(result)
# result = write_file.write_file("calculator", "/tmp/temp.txt", "this should not be allowed")
# print(result)


# result = run_python_file.run_python_file("calculator", "main.py")
# print(result)   
# result = run_python_file.run_python_file("calculator", "tests.py")
# print(result)   
# result = run_python_file.run_python_file("calculator", "../main.py") #(this should return an error)
# print(result)   
# result = run_python_file.run_python_file("calculator", "nonexistent.py") #(this should return an error)
# print(result)   

# result = call_function.call_function("calculator", "get_files_info", {"directory": "pkg"})
# print(result)
