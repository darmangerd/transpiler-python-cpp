
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftPLUSMINUSleftTIMESDIVIDEAND ASSIGN BOOL COLON COMMA DEDENT DEF DIVIDE ELSE EQUALS FALSE FLOAT FLOAT_VALUE GE GT ID IF INDENT INT INTEGER_VALUE LE LPAREN LT MINUS NEQUALS NEWLINE NOT OR PLUS RETURN RETURN_TYPE RPAREN STR STRING_VALUE TIMES TRUE VOID WHILEprogram : statement_liststatement_list : statement\n                      | statement_list statement\n                      | statement_list NEWLINEstatement : assignment\n                 | if_statement\n                 | while_statement\n                 | return_statement\n                 | function\n                 | function_call\n                 | statement NEWLINEblock : INDENT statement_list DEDENT\n             | block NEWLINEassignment : ID ASSIGN expression\n                  | ID COLON type ASSIGN expressionif_statement : IF logical COLON block\n                    | IF logical COLON block NEWLINE ELSE COLON blockwhile_statement : WHILE logical COLON block\n                       | WHILE TRUE COLON blockreturn_statement : RETURN expressionid : IDboolean : TRUE\n               | FALSEinteger : INTEGER_VALUEfloat : FLOAT_VALUEstring : STRING_VALUEvalue : integer\n             | float\n             | boolean\n             | stringvariable : id\n                | function_callfactor : value\n              | variableunary : NOTlogical : factor LT factor\n               | factor LE factor\n               | factor GT factor\n               | factor GE factor\n               | factor EQUALS factor\n               | factor NEQUALS factor\n               | factor AND factor\n               | factor OR factormath : factor PLUS factor\n            | factor MINUS factor\n            | factor TIMES factor\n            | factor DIVIDE factorbinary : logical\n              | mathexpression : factor\n                  | unary\n                  | binarytype : INT\n            | FLOAT\n            | STR\n            | BOOL\n            | VOIDargument_list_definition : ID COLON type\n                     | ID COLON type COMMA argument_list_definitionfunction : DEF ID LPAREN argument_list_definition RPAREN RETURN_TYPE type COLON blockfunction_call : ID LPAREN RPAREN\n                     | ID LPAREN argument_list_call RPARENargument_list_call : expression\n                     | expression COMMA argument_list_call'
    
_lr_action_items = {'ID':([0,2,3,4,5,6,7,8,9,11,12,13,14,15,16,17,18,20,23,24,25,26,27,28,29,30,31,32,33,34,35,36,39,40,41,42,43,44,45,47,54,58,59,60,61,62,63,64,65,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,94,96,97,98,102,106,108,111,],[10,10,-2,-5,-6,-7,-8,-9,-10,36,36,36,46,-3,-4,-11,36,36,-33,-34,-27,-28,-29,-30,-31,-32,-24,-25,-22,-23,-26,-21,-20,-50,-51,-52,-35,-48,-49,-14,-61,36,36,36,36,36,36,36,36,36,36,36,36,92,36,-62,36,-16,10,-36,-37,-38,-39,-40,-41,-42,-43,-18,-19,-44,-45,-46,-47,-15,-13,10,-13,-12,92,-17,-60,]),'IF':([0,2,3,4,5,6,7,8,9,15,16,17,23,24,25,26,27,28,29,30,31,32,33,34,35,36,39,40,41,42,43,44,45,47,54,74,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,94,96,97,98,102,108,111,],[11,11,-2,-5,-6,-7,-8,-9,-10,-3,-4,-11,-33,-34,-27,-28,-29,-30,-31,-32,-24,-25,-22,-23,-26,-21,-20,-50,-51,-52,-35,-48,-49,-14,-61,-62,-16,11,-36,-37,-38,-39,-40,-41,-42,-43,-18,-19,-44,-45,-46,-47,-15,-13,11,-13,-12,-17,-60,]),'WHILE':([0,2,3,4,5,6,7,8,9,15,16,17,23,24,25,26,27,28,29,30,31,32,33,34,35,36,39,40,41,42,43,44,45,47,54,74,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,94,96,97,98,102,108,111,],[12,12,-2,-5,-6,-7,-8,-9,-10,-3,-4,-11,-33,-34,-27,-28,-29,-30,-31,-32,-24,-25,-22,-23,-26,-21,-20,-50,-51,-52,-35,-48,-49,-14,-61,-62,-16,12,-36,-37,-38,-39,-40,-41,-42,-43,-18,-19,-44,-45,-46,-47,-15,-13,12,-13,-12,-17,-60,]),'RETURN':([0,2,3,4,5,6,7,8,9,15,16,17,23,24,25,26,27,28,29,30,31,32,33,34,35,36,39,40,41,42,43,44,45,47,54,74,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,94,96,97,98,102,108,111,],[13,13,-2,-5,-6,-7,-8,-9,-10,-3,-4,-11,-33,-34,-27,-28,-29,-30,-31,-32,-24,-25,-22,-23,-26,-21,-20,-50,-51,-52,-35,-48,-49,-14,-61,-62,-16,13,-36,-37,-38,-39,-40,-41,-42,-43,-18,-19,-44,-45,-46,-47,-15,-13,13,-13,-12,-17,-60,]),'DEF':([0,2,3,4,5,6,7,8,9,15,16,17,23,24,25,26,27,28,29,30,31,32,33,34,35,36,39,40,41,42,43,44,45,47,54,74,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,94,96,97,98,102,108,111,],[14,14,-2,-5,-6,-7,-8,-9,-10,-3,-4,-11,-33,-34,-27,-28,-29,-30,-31,-32,-24,-25,-22,-23,-26,-21,-20,-50,-51,-52,-35,-48,-49,-14,-61,-62,-16,14,-36,-37,-38,-39,-40,-41,-42,-43,-18,-19,-44,-45,-46,-47,-15,-13,14,-13,-12,-17,-60,]),'$end':([1,2,3,4,5,6,7,8,9,15,16,17,23,24,25,26,27,28,29,30,31,32,33,34,35,36,39,40,41,42,43,44,45,47,54,74,76,78,79,80,81,82,83,84,85,86,87,88,89,90,91,94,96,98,102,108,111,],[0,-1,-2,-5,-6,-7,-8,-9,-10,-3,-4,-11,-33,-34,-27,-28,-29,-30,-31,-32,-24,-25,-22,-23,-26,-21,-20,-50,-51,-52,-35,-48,-49,-14,-61,-62,-16,-36,-37,-38,-39,-40,-41,-42,-43,-18,-19,-44,-45,-46,-47,-15,-13,-13,-12,-17,-60,]),'NEWLINE':([2,3,4,5,6,7,8,9,15,16,17,23,24,25,26,27,28,29,30,31,32,33,34,35,36,39,40,41,42,43,44,45,47,54,74,76,78,79,80,81,82,83,84,85,86,87,88,89,90,91,94,96,97,98,102,108,111,],[16,17,-5,-6,-7,-8,-9,-10,17,-4,-11,-33,-34,-27,-28,-29,-30,-31,-32,-24,-25,-22,-23,-26,-21,-20,-50,-51,-52,-35,-48,-49,-14,-61,-62,96,-36,-37,-38,-39,-40,-41,-42,-43,98,98,-44,-45,-46,-47,-15,-13,16,-13,-12,98,98,]),'DEDENT':([3,4,5,6,7,8,9,15,16,17,23,24,25,26,27,28,29,30,31,32,33,34,35,36,39,40,41,42,43,44,45,47,54,74,76,78,79,80,81,82,83,84,85,86,87,88,89,90,91,94,96,97,98,102,108,111,],[-2,-5,-6,-7,-8,-9,-10,-3,-4,-11,-33,-34,-27,-28,-29,-30,-31,-32,-24,-25,-22,-23,-26,-21,-20,-50,-51,-52,-35,-48,-49,-14,-61,-62,-16,-36,-37,-38,-39,-40,-41,-42,-43,-18,-19,-44,-45,-46,-47,-15,-13,102,-13,-12,-17,-60,]),'ASSIGN':([10,48,49,50,51,52,53,],[18,73,-53,-54,-55,-56,-57,]),'COLON':([10,21,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,49,50,51,52,53,54,74,78,79,80,81,82,83,84,85,92,101,107,],[19,57,-33,-34,-27,-28,-29,-30,-31,-32,-24,-25,-22,-23,-26,-21,66,67,-53,-54,-55,-56,-57,-61,-62,-36,-37,-38,-39,-40,-41,-42,-43,99,105,110,]),'LPAREN':([10,36,46,],[20,20,72,]),'INTEGER_VALUE':([11,12,13,18,20,58,59,60,61,62,63,64,65,68,69,70,71,73,75,],[31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,]),'FLOAT_VALUE':([11,12,13,18,20,58,59,60,61,62,63,64,65,68,69,70,71,73,75,],[32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,]),'TRUE':([11,12,13,18,20,58,59,60,61,62,63,64,65,68,69,70,71,73,75,],[33,38,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,]),'FALSE':([11,12,13,18,20,58,59,60,61,62,63,64,65,68,69,70,71,73,75,],[34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,]),'STRING_VALUE':([11,12,13,18,20,58,59,60,61,62,63,64,65,68,69,70,71,73,75,],[35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,]),'NOT':([13,18,20,73,75,],[43,43,43,43,43,]),'INT':([19,99,104,],[49,49,49,]),'FLOAT':([19,99,104,],[50,50,50,]),'STR':([19,99,104,],[51,51,51,]),'BOOL':([19,99,104,],[52,52,52,]),'VOID':([19,99,104,],[53,53,53,]),'RPAREN':([20,23,24,25,26,27,28,29,30,31,32,33,34,35,36,40,41,42,43,44,45,49,50,51,52,53,54,55,56,74,78,79,80,81,82,83,84,85,88,89,90,91,93,95,103,109,],[54,-33,-34,-27,-28,-29,-30,-31,-32,-24,-25,-22,-23,-26,-21,-50,-51,-52,-35,-48,-49,-53,-54,-55,-56,-57,-61,74,-63,-62,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-46,-47,100,-64,-58,-59,]),'LT':([22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,38,40,54,74,],[58,-33,-34,-27,-28,-29,-30,-31,-32,-24,-25,-22,-23,-26,-21,-22,58,-61,-62,]),'LE':([22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,38,40,54,74,],[59,-33,-34,-27,-28,-29,-30,-31,-32,-24,-25,-22,-23,-26,-21,-22,59,-61,-62,]),'GT':([22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,38,40,54,74,],[60,-33,-34,-27,-28,-29,-30,-31,-32,-24,-25,-22,-23,-26,-21,-22,60,-61,-62,]),'GE':([22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,38,40,54,74,],[61,-33,-34,-27,-28,-29,-30,-31,-32,-24,-25,-22,-23,-26,-21,-22,61,-61,-62,]),'EQUALS':([22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,38,40,54,74,],[62,-33,-34,-27,-28,-29,-30,-31,-32,-24,-25,-22,-23,-26,-21,-22,62,-61,-62,]),'NEQUALS':([22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,38,40,54,74,],[63,-33,-34,-27,-28,-29,-30,-31,-32,-24,-25,-22,-23,-26,-21,-22,63,-61,-62,]),'AND':([22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,38,40,54,74,],[64,-33,-34,-27,-28,-29,-30,-31,-32,-24,-25,-22,-23,-26,-21,-22,64,-61,-62,]),'OR':([22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,38,40,54,74,],[65,-33,-34,-27,-28,-29,-30,-31,-32,-24,-25,-22,-23,-26,-21,-22,65,-61,-62,]),'PLUS':([23,24,25,26,27,28,29,30,31,32,33,34,35,36,40,54,74,],[-33,-34,-27,-28,-29,-30,-31,-32,-24,-25,-22,-23,-26,-21,68,-61,-62,]),'MINUS':([23,24,25,26,27,28,29,30,31,32,33,34,35,36,40,54,74,],[-33,-34,-27,-28,-29,-30,-31,-32,-24,-25,-22,-23,-26,-21,69,-61,-62,]),'TIMES':([23,24,25,26,27,28,29,30,31,32,33,34,35,36,40,54,74,],[-33,-34,-27,-28,-29,-30,-31,-32,-24,-25,-22,-23,-26,-21,70,-61,-62,]),'DIVIDE':([23,24,25,26,27,28,29,30,31,32,33,34,35,36,40,54,74,],[-33,-34,-27,-28,-29,-30,-31,-32,-24,-25,-22,-23,-26,-21,71,-61,-62,]),'COMMA':([23,24,25,26,27,28,29,30,31,32,33,34,35,36,40,41,42,43,44,45,49,50,51,52,53,54,56,74,78,79,80,81,82,83,84,85,88,89,90,91,103,],[-33,-34,-27,-28,-29,-30,-31,-32,-24,-25,-22,-23,-26,-21,-50,-51,-52,-35,-48,-49,-53,-54,-55,-56,-57,-61,75,-62,-36,-37,-38,-39,-40,-41,-42,-43,-44,-45,-46,-47,106,]),'INDENT':([57,66,67,105,110,],[77,77,77,77,77,]),'ELSE':([96,],[101,]),'RETURN_TYPE':([100,],[104,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'program':([0,],[1,]),'statement_list':([0,77,],[2,97,]),'statement':([0,2,77,97,],[3,15,3,15,]),'assignment':([0,2,77,97,],[4,4,4,4,]),'if_statement':([0,2,77,97,],[5,5,5,5,]),'while_statement':([0,2,77,97,],[6,6,6,6,]),'return_statement':([0,2,77,97,],[7,7,7,7,]),'function':([0,2,77,97,],[8,8,8,8,]),'function_call':([0,2,11,12,13,18,20,58,59,60,61,62,63,64,65,68,69,70,71,73,75,77,97,],[9,9,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,9,9,]),'logical':([11,12,13,18,20,73,75,],[21,37,44,44,44,44,44,]),'factor':([11,12,13,18,20,58,59,60,61,62,63,64,65,68,69,70,71,73,75,],[22,22,40,40,40,78,79,80,81,82,83,84,85,88,89,90,91,40,40,]),'value':([11,12,13,18,20,58,59,60,61,62,63,64,65,68,69,70,71,73,75,],[23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,]),'variable':([11,12,13,18,20,58,59,60,61,62,63,64,65,68,69,70,71,73,75,],[24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,]),'integer':([11,12,13,18,20,58,59,60,61,62,63,64,65,68,69,70,71,73,75,],[25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,]),'float':([11,12,13,18,20,58,59,60,61,62,63,64,65,68,69,70,71,73,75,],[26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,]),'boolean':([11,12,13,18,20,58,59,60,61,62,63,64,65,68,69,70,71,73,75,],[27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,]),'string':([11,12,13,18,20,58,59,60,61,62,63,64,65,68,69,70,71,73,75,],[28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,]),'id':([11,12,13,18,20,58,59,60,61,62,63,64,65,68,69,70,71,73,75,],[29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,]),'expression':([13,18,20,73,75,],[39,47,56,94,56,]),'unary':([13,18,20,73,75,],[41,41,41,41,41,]),'binary':([13,18,20,73,75,],[42,42,42,42,42,]),'math':([13,18,20,73,75,],[45,45,45,45,45,]),'type':([19,99,104,],[48,103,107,]),'argument_list_call':([20,75,],[55,95,]),'block':([57,66,67,105,110,],[76,86,87,108,111,]),'argument_list_definition':([72,106,],[93,109,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program","S'",1,None,None,None),
  ('program -> statement_list','program',1,'p_program','yacc.py',13),
  ('statement_list -> statement','statement_list',1,'p_statement_list','yacc.py',18),
  ('statement_list -> statement_list statement','statement_list',2,'p_statement_list','yacc.py',19),
  ('statement_list -> statement_list NEWLINE','statement_list',2,'p_statement_list','yacc.py',20),
  ('statement -> assignment','statement',1,'p_statement','yacc.py',31),
  ('statement -> if_statement','statement',1,'p_statement','yacc.py',32),
  ('statement -> while_statement','statement',1,'p_statement','yacc.py',33),
  ('statement -> return_statement','statement',1,'p_statement','yacc.py',34),
  ('statement -> function','statement',1,'p_statement','yacc.py',35),
  ('statement -> function_call','statement',1,'p_statement','yacc.py',36),
  ('statement -> statement NEWLINE','statement',2,'p_statement','yacc.py',37),
  ('block -> INDENT statement_list DEDENT','block',3,'p_block','yacc.py',42),
  ('block -> block NEWLINE','block',2,'p_block','yacc.py',43),
  ('assignment -> ID ASSIGN expression','assignment',3,'p_assignment','yacc.py',51),
  ('assignment -> ID COLON type ASSIGN expression','assignment',5,'p_assignment','yacc.py',52),
  ('if_statement -> IF logical COLON block','if_statement',4,'p_if_statement','yacc.py',60),
  ('if_statement -> IF logical COLON block NEWLINE ELSE COLON block','if_statement',8,'p_if_statement','yacc.py',61),
  ('while_statement -> WHILE logical COLON block','while_statement',4,'p_while_statement','yacc.py',70),
  ('while_statement -> WHILE TRUE COLON block','while_statement',4,'p_while_statement','yacc.py',71),
  ('return_statement -> RETURN expression','return_statement',2,'p_return_statement','yacc.py',76),
  ('id -> ID','id',1,'p_id','yacc.py',81),
  ('boolean -> TRUE','boolean',1,'p_boolean_value','yacc.py',86),
  ('boolean -> FALSE','boolean',1,'p_boolean_value','yacc.py',87),
  ('integer -> INTEGER_VALUE','integer',1,'p_integer_value','yacc.py',92),
  ('float -> FLOAT_VALUE','float',1,'p_float_value','yacc.py',97),
  ('string -> STRING_VALUE','string',1,'p_string_value','yacc.py',102),
  ('value -> integer','value',1,'p_value','yacc.py',107),
  ('value -> float','value',1,'p_value','yacc.py',108),
  ('value -> boolean','value',1,'p_value','yacc.py',109),
  ('value -> string','value',1,'p_value','yacc.py',110),
  ('variable -> id','variable',1,'p_variable','yacc.py',115),
  ('variable -> function_call','variable',1,'p_variable','yacc.py',116),
  ('factor -> value','factor',1,'p_factor','yacc.py',121),
  ('factor -> variable','factor',1,'p_factor','yacc.py',122),
  ('unary -> NOT','unary',1,'p_unary','yacc.py',128),
  ('logical -> factor LT factor','logical',3,'p_logical','yacc.py',133),
  ('logical -> factor LE factor','logical',3,'p_logical','yacc.py',134),
  ('logical -> factor GT factor','logical',3,'p_logical','yacc.py',135),
  ('logical -> factor GE factor','logical',3,'p_logical','yacc.py',136),
  ('logical -> factor EQUALS factor','logical',3,'p_logical','yacc.py',137),
  ('logical -> factor NEQUALS factor','logical',3,'p_logical','yacc.py',138),
  ('logical -> factor AND factor','logical',3,'p_logical','yacc.py',139),
  ('logical -> factor OR factor','logical',3,'p_logical','yacc.py',140),
  ('math -> factor PLUS factor','math',3,'p_math','yacc.py',146),
  ('math -> factor MINUS factor','math',3,'p_math','yacc.py',147),
  ('math -> factor TIMES factor','math',3,'p_math','yacc.py',148),
  ('math -> factor DIVIDE factor','math',3,'p_math','yacc.py',149),
  ('binary -> logical','binary',1,'p_binary','yacc.py',155),
  ('binary -> math','binary',1,'p_binary','yacc.py',156),
  ('expression -> factor','expression',1,'p_expression','yacc.py',162),
  ('expression -> unary','expression',1,'p_expression','yacc.py',163),
  ('expression -> binary','expression',1,'p_expression','yacc.py',164),
  ('type -> INT','type',1,'p_type','yacc.py',170),
  ('type -> FLOAT','type',1,'p_type','yacc.py',171),
  ('type -> STR','type',1,'p_type','yacc.py',172),
  ('type -> BOOL','type',1,'p_type','yacc.py',173),
  ('type -> VOID','type',1,'p_type','yacc.py',174),
  ('argument_list_definition -> ID COLON type','argument_list_definition',3,'p_argument_list_definition','yacc.py',179),
  ('argument_list_definition -> ID COLON type COMMA argument_list_definition','argument_list_definition',5,'p_argument_list_definition','yacc.py',180),
  ('function -> DEF ID LPAREN argument_list_definition RPAREN RETURN_TYPE type COLON block','function',9,'p_function_definition','yacc.py',190),
  ('function_call -> ID LPAREN RPAREN','function_call',3,'p_function_call','yacc.py',195),
  ('function_call -> ID LPAREN argument_list_call RPAREN','function_call',4,'p_function_call','yacc.py',196),
  ('argument_list_call -> expression','argument_list_call',1,'p_argument_list_call','yacc.py',204),
  ('argument_list_call -> expression COMMA argument_list_call','argument_list_call',3,'p_argument_list_call','yacc.py',205),
]