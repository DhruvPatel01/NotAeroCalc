
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'nonassocINleft+-left*/rightUMINUSrightUPLUSright^DEL EQUATION FLOAT IMPORT IN RAWSTR RESET SI SOLVE STRING UNIVARIATE_FN VARIABLESstart : statement\n             | command \';\'\n             | command \n             |\n    command : DEL STRING\n               | VARIABLES\n               | IMPORT RAWSTR \n               | RESET\n               | SOLVE to_solve\n               | EQUATION RAWSTRto_solve : STRING\n                | to_solve \',\' STRING\n    statement : STRING "=" expression\n                 | STRING "=" expression \';\'\n    statement : expression\n                 | expression \';\'\n    expression : expression \'+\' expression\n                  | expression \'-\' expression\n                  | expression \'*\' expression\n                  | expression \'/\' expression\n                  | expression \'^\' expression\n                  | expression IN expression \n                  | expression IN SIexpression : \'-\' expression %prec UMINUSexpression : \'+\' expression %prec UPLUSexpression : \'(\' expression \')\'expression : FLOATexpression : STRINGexpression : UNIVARIATE_FN \'(\' expression \')\' '
    
_lr_action_items = {'$end':([0,1,2,3,4,5,7,9,15,17,19,26,27,28,29,30,31,32,33,36,37,38,39,40,41,42,43,45,47,48,49,],[-4,0,-1,-3,-28,-15,-6,-8,-27,-2,-16,-5,-7,-9,-11,-10,-25,-28,-24,-13,-17,-18,-19,-20,-21,-22,-23,-26,-14,-12,-29,]),'STRING':([0,6,10,12,13,14,18,20,21,22,23,24,25,35,44,],[4,26,29,32,32,32,32,32,32,32,32,32,32,32,48,]),'DEL':([0,],[6,]),'VARIABLES':([0,],[7,]),'IMPORT':([0,],[8,]),'RESET':([0,],[9,]),'SOLVE':([0,],[10,]),'EQUATION':([0,],[11,]),'-':([0,4,5,12,13,14,15,18,20,21,22,23,24,25,31,32,33,34,35,36,37,38,39,40,41,42,43,45,46,49,],[13,-28,21,13,13,13,-27,13,13,13,13,13,13,13,-25,-28,-24,21,13,21,-17,-18,-19,-20,-21,21,-23,-26,21,-29,]),'+':([0,4,5,12,13,14,15,18,20,21,22,23,24,25,31,32,33,34,35,36,37,38,39,40,41,42,43,45,46,49,],[12,-28,20,12,12,12,-27,12,12,12,12,12,12,12,-25,-28,-24,20,12,20,-17,-18,-19,-20,-21,20,-23,-26,20,-29,]),'(':([0,12,13,14,16,18,20,21,22,23,24,25,35,],[14,14,14,14,35,14,14,14,14,14,14,14,14,]),'FLOAT':([0,12,13,14,18,20,21,22,23,24,25,35,],[15,15,15,15,15,15,15,15,15,15,15,15,]),'UNIVARIATE_FN':([0,12,13,14,18,20,21,22,23,24,25,35,],[16,16,16,16,16,16,16,16,16,16,16,16,]),';':([3,4,5,7,9,15,26,27,28,29,30,31,32,33,36,37,38,39,40,41,42,43,45,48,49,],[17,-28,19,-6,-8,-27,-5,-7,-9,-11,-10,-25,-28,-24,47,-17,-18,-19,-20,-21,-22,-23,-26,-12,-29,]),'=':([4,],[18,]),'*':([4,5,15,31,32,33,34,36,37,38,39,40,41,42,43,45,46,49,],[-28,22,-27,-25,-28,-24,22,22,22,22,-19,-20,-21,22,-23,-26,22,-29,]),'/':([4,5,15,31,32,33,34,36,37,38,39,40,41,42,43,45,46,49,],[-28,23,-27,-25,-28,-24,23,23,23,23,-19,-20,-21,23,-23,-26,23,-29,]),'^':([4,5,15,31,32,33,34,36,37,38,39,40,41,42,43,45,46,49,],[-28,24,-27,24,-28,24,24,24,24,24,24,24,24,24,-23,-26,24,-29,]),'IN':([4,5,15,31,32,33,34,36,37,38,39,40,41,42,43,45,46,49,],[-28,25,-27,-25,-28,-24,25,25,-17,-18,-19,-20,-21,25,-23,-26,25,-29,]),'RAWSTR':([8,11,],[27,30,]),')':([15,31,32,33,34,37,38,39,40,41,42,43,45,46,49,],[-27,-25,-28,-24,45,-17,-18,-19,-20,-21,-22,-23,-26,49,-29,]),'SI':([25,],[43,]),',':([28,29,48,],[44,-11,-12,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'start':([0,],[1,]),'statement':([0,],[2,]),'command':([0,],[3,]),'expression':([0,12,13,14,18,20,21,22,23,24,25,35,],[5,31,33,34,36,37,38,39,40,41,42,46,]),'to_solve':([10,],[28,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> start","S'",1,None,None,None),
  ('start -> statement','start',1,'p_start_statement','parsing.py',86),
  ('start -> command ;','start',2,'p_start_statement','parsing.py',87),
  ('start -> command','start',1,'p_start_statement','parsing.py',88),
  ('start -> <empty>','start',0,'p_start_statement','parsing.py',89),
  ('command -> DEL STRING','command',2,'p_start_command','parsing.py',95),
  ('command -> VARIABLES','command',1,'p_start_command','parsing.py',96),
  ('command -> IMPORT RAWSTR','command',2,'p_start_command','parsing.py',97),
  ('command -> RESET','command',1,'p_start_command','parsing.py',98),
  ('command -> SOLVE to_solve','command',2,'p_start_command','parsing.py',99),
  ('command -> EQUATION RAWSTR','command',2,'p_start_command','parsing.py',100),
  ('to_solve -> STRING','to_solve',1,'p_to_solve','parsing.py',128),
  ('to_solve -> to_solve , STRING','to_solve',3,'p_to_solve','parsing.py',129),
  ('statement -> STRING = expression','statement',3,'p_statement_assign','parsing.py',140),
  ('statement -> STRING = expression ;','statement',4,'p_statement_assign','parsing.py',141),
  ('statement -> expression','statement',1,'p_statement_expr','parsing.py',150),
  ('statement -> expression ;','statement',2,'p_statement_expr','parsing.py',151),
  ('expression -> expression + expression','expression',3,'p_expression_binop','parsing.py',159),
  ('expression -> expression - expression','expression',3,'p_expression_binop','parsing.py',160),
  ('expression -> expression * expression','expression',3,'p_expression_binop','parsing.py',161),
  ('expression -> expression / expression','expression',3,'p_expression_binop','parsing.py',162),
  ('expression -> expression ^ expression','expression',3,'p_expression_binop','parsing.py',163),
  ('expression -> expression IN expression','expression',3,'p_expression_binop','parsing.py',164),
  ('expression -> expression IN SI','expression',3,'p_expression_binop','parsing.py',165),
  ('expression -> - expression','expression',2,'p_expression_uminus','parsing.py',199),
  ('expression -> + expression','expression',2,'p_expression_uplus','parsing.py',204),
  ('expression -> ( expression )','expression',3,'p_expression_group','parsing.py',209),
  ('expression -> FLOAT','expression',1,'p_expression_number','parsing.py',214),
  ('expression -> STRING','expression',1,'p_expression_name','parsing.py',226),
  ('expression -> UNIVARIATE_FN ( expression )','expression',4,'p_expression_func','parsing.py',244),
]
