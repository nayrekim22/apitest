from training_package import file_handling_functions as fhf

test_file = "training_package/example.txt"
output_file = "file.out"

fobj = fhf.open_file_for_read(test_file)
fhf.print_file_line_by_line(fobj)

wobj = fhf.open_file_for_write(output_file)
wobj.writelines(fhf.get_file_as_list_of_strings(test_file))
fobj.close()