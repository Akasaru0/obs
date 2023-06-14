import re,random,string

input_file = open("script_mimi.ps1",'r')
output_file = open("outputfile2.ps1",'a')

regex_variable = r'(?!\$(_|Null|true|false))\$[a-zA-Z-_]*'
regex_fonction = r'^function\s+(\S+)'
regex_text = r'(\'((.+?))\')|(\"((.+?))\")'
regex_method = r'(\.\w*)'

variable_map = {}
function_map = {}

cont = 1

for line in input_file.readlines():
    new_line = line

    # #Check for string
    # for string_find in re.finditer(regex_method,line):
    #     print(string_find)
    #     new_string = ".$("
    #     string_match = string_find.group().split(".")[1]
            
    #     for j in range(0,len(string_match)):
    #         new_string = new_string+"[char]"+hex(ord(string_match[j]))
    #         if j != len(string_match)-1:
    #             new_string=new_string+"+"
    #         else:
    #             new_string= new_string+')'
    #     new_line = new_line.replace(string_find.group(),new_string)


    #Check for the variable
    match = re.search(regex_variable,line)
    if match:
        if match.group() not in variable_map:
            variable_map[match.group()] = ''.join(random.choice(string.ascii_lowercase) for i in range(random.randint(12,64)))            

    #Check for the fuction name
    match = re.search(regex_fonction,line)
    if match:
        if match.group() not in function_map:
            function_map[match.group().split(" ")[1]] = ''.join(random.choice(string.ascii_lowercase) for i in range(random.randint(12,64)))
    
    
    #Check for string
    match = re.finditer(regex_text,line)
    for string_find in re.finditer(regex_text,line):
        new_string = "$("
        if len(string_find.group().split("\"")) == 3:
            string_match = string_find.group().split("\"")[1]
        if len(string_find.group().split("\'")) == 3:
            string_match = string_find.group().split("\'")[1]
            
        for j in range(0,len(string_match)):

            new_string = new_string+"[char]"+hex(ord(string_match[j]))
            if j != len(string_match)-1:
                new_string=new_string+"+"
            else:
                new_string= new_string+')'
        new_line = new_line.replace(string_find.group(),new_string)

    for variable in variable_map:
        new_line = new_line.replace(variable,"$"+variable_map[variable])
    
    for function in function_map:
        new_line = new_line.replace(function_map,"$"+function_map[function])
        
    output_file.write(new_line)
    cont = cont +1
