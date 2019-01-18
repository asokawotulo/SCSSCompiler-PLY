import ply.yacc as yacc
from plytoken import tokens
from parsed import ParsedObject

result = ParsedObject()

variables = {}

# Erases Whitespace
def elim_space(var):
	return var.replace(' ', '')
# Erases Colon
def elim_colon(var):
	return var.replace(':', '')
# Erases Semicolon
def elim_semicolon(var):
	return var.replace(';', '')

def p_expression_selector(p):
	'''expression : selector LCURLY factor RCURLY expression
	'''
	global result
	if p[5] != None:
		p[0] = p[1] + '{ ' + p[3] + '}' + p[5]
	else:
		p[0] = p[1] + '{ ' + p[3] + '}'
	result.addSelector(p[1])


def p_expression_factor_term_general(p):
	'''expression : assign_variable expression
       factor : assign_variable factor
              | attribute factor
              | expression
	'''
	try:
		if p[2] != None and p[1] != None:
			p[0] = p[1] + p[2]
		elif p[2] != None:
			p[0] = p[2]
		elif p[1] != None:
			p[0] = p[1]
		else:
			pass
	except IndexError:
		p[0] = p[1]

def p_term_general(p):
	'''term : val term
	'''
	try:
		if p[2] != None and p[1] != None:
			p[0] = p[1] + ' ' + p[2]
		elif p[2] != None:
			p[0] = p[2]
		elif p[1] != None:
			p[0] = p[1]
		else:
			pass
	except IndexError:
		p[0] = p[1]

def p_attribute_general(p):
	'''attribute : PROPERTY COLON term SEMICOLON
	'''
	global result
	if p[3] != None:
		p[0] = p[1] + ':' + p[3] + ';'
	result.addProperty(p[0])

def p_assign_variable(p):
	'''assign_variable : DEC_VARIABLE term SEMICOLON
	'''
	p[1] = elim_space(elim_colon(p[1]))
	variables[p[1]] = p[2]

def p_selector_general(p):
	'''selector : ELEMENT
				| CLASS
				| ID
				| ATTRI_ELEMENT
				| PSEUDO_ELEMENT
				| PARENT_REF
	'''
	p[0] = p[1]

def p_multiple_selector_general(p):
	'''selector : selector COMMA mulsec
	'''
	p[0] = p[1] + ',' + p[3]

def p_multiple_selector_empty(p):
	'''mulsec : selector
	          | empty
	'''
	p[0] = p[1]

def p_val_call_var(p):
	'''val : CALL_VARIABLE
	'''
	p[1] = elim_space(p[1])
	if p[1] in variables:
		p[0] = variables[p[1]]
	else:
		print('{} is not defined'.format(p[1]))

def p_val_general(p):
	'''val : HEX
		   | UNITS
		   | VALUE
		   | URLS
	'''
	p[0] = p[1]

def p_empty_nonterminal(p):
	'''expression : empty
	   factor : empty
	   term : empty
	'''
	p[0] = p[1]

# Passes Empty
def p_empty(p):
    'empty :'
    pass

def p_error(p):
	result.setText(p)
	result.setSuccess(False)

# Build the parser
parser = yacc.yacc(errorlog=yacc.NullLogger())