import sys
from plyparse import result, parser

# arguments = sys.argv
# print(arguments)

# Set Source Path
source_path = "yes.scss"
source_file = open(source_path, encoding="UTF-8")
line = source_file.read()
source_file.close()

# Create destination path with same name 
dest_path = source_path.split('.')[0] + '.css'
	
temp = parser.parse(line)

# print(result.text)
if temp != None:
	result.setText(temp)
	result.setSuccess(True)

	inp = [k.lstrip() for k in result.text.replace('{', '\n{\n').replace('}', '}\n').replace(';', ';\n').split('\n')]

	parents = []
	nest = 0
	for i in inp:
		if i in result.selectors:
			parents.append(i)

			if len(parents) > 1:
				parent_string = ""

				for j in range(len(parents)):
					if j == 0:
						parent_string += parents[j]

					elif ',' in parents[j]:
						multi_parent = []
						split_parents = parents[j].split(',')
						for k in split_parents:
							if k.startswith('&'):
								multi_parent.append(parent_string + k[1::])
							else:
								multi_parent.append(parent_string + ' ' + k)
						parent_string = ', '.join(multi_parent)
				
					elif parents[j].startswith('&'):
						parent_string += parents[j][1::]
					
					else:
						parent_string += ' ' + parents[j]

				result.writeConverted('}\n' + parent_string + ' {\n')
			else:
				result.writeConverted(i + ' {\n')

		elif i in result.properties:
			result.writeConverted('\t' + i + '\n')

		elif i == '}':
			parents.pop()
			if len(parents) == 0:
				result.writeConverted('}\n')

	# Creates .CSS file within the Directory
	try:
		with open(dest_path, "x") as fout:
			print("Generating your CSS file...")
		with open(dest_path,'w',encoding = 'UTF-8') as parsecss:
			parsecss.write(result.converted)
		print('\nYour CSS file has been generated')

	# Updates file if .CSS file already exist. 
	except FileExistsError:
		print('Updating your CSS file...')
		with open(dest_path,'w',encoding = 'UTF-8') as parsecss:
			parsecss.write(result.converted)
		print("\nYour CSS file has been updated")

else:
	print("Syntax Error detected in line {} involving value \"{}\"".format(result.text.lineno, result.text.value))