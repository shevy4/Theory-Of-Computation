
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'colon comma double_equals else equals float for identifier if in integer lparen operator print range rparen stringprogram : statement_liststatement_list : statement\n                      | statement_list statementstatement : assignment\n                 | comparison\n                 | expression\n                 | print_statement\n                 | for_loop\n                 | if_statementfor_loop : for expression in range lparen expression rparen colon\n    if_statement : if expression colon statement\n                 | if expression colon statement else colon statement\n    assignment : identifier equals expressioncomparison : identifier double_equals expressionexpression : integer\n                  | float\n                  | string\n                  | identifier\n                  | expression operator expression\n                  | expression double_equals expression\n                  | lparen expression rparenprint_statement : print expressionexpression_list : expression\n                       | expression_list comma expression'
    
_lr_action_items = {'identifier':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,24,25,28,29,30,31,32,34,36,37,40,42,43,],[10,10,-2,-4,-5,-6,-7,-8,-9,-18,-15,-16,-17,24,24,24,24,-3,24,24,24,24,-18,-22,-19,-20,-13,-14,-21,10,-11,24,10,-12,-10,]),'integer':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,24,25,28,29,30,31,32,34,36,37,40,42,43,],[11,11,-2,-4,-5,-6,-7,-8,-9,-18,-15,-16,-17,11,11,11,11,-3,11,11,11,11,-18,-22,-19,-20,-13,-14,-21,11,-11,11,11,-12,-10,]),'float':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,24,25,28,29,30,31,32,34,36,37,40,42,43,],[12,12,-2,-4,-5,-6,-7,-8,-9,-18,-15,-16,-17,12,12,12,12,-3,12,12,12,12,-18,-22,-19,-20,-13,-14,-21,12,-11,12,12,-12,-10,]),'string':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,24,25,28,29,30,31,32,34,36,37,40,42,43,],[13,13,-2,-4,-5,-6,-7,-8,-9,-18,-15,-16,-17,13,13,13,13,-3,13,13,13,13,-18,-22,-19,-20,-13,-14,-21,13,-11,13,13,-12,-10,]),'lparen':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,24,25,28,29,30,31,32,34,35,36,37,40,42,43,],[14,14,-2,-4,-5,-6,-7,-8,-9,-18,-15,-16,-17,14,14,14,14,-3,14,14,14,14,-18,-22,-19,-20,-13,-14,-21,14,37,-11,14,14,-12,-10,]),'print':([0,2,3,4,5,6,7,8,9,10,11,12,13,18,24,25,28,29,30,31,32,34,36,40,42,43,],[15,15,-2,-4,-5,-6,-7,-8,-9,-18,-15,-16,-17,-3,-18,-22,-19,-20,-13,-14,-21,15,-11,15,-12,-10,]),'for':([0,2,3,4,5,6,7,8,9,10,11,12,13,18,24,25,28,29,30,31,32,34,36,40,42,43,],[16,16,-2,-4,-5,-6,-7,-8,-9,-18,-15,-16,-17,-3,-18,-22,-19,-20,-13,-14,-21,16,-11,16,-12,-10,]),'if':([0,2,3,4,5,6,7,8,9,10,11,12,13,18,24,25,28,29,30,31,32,34,36,40,42,43,],[17,17,-2,-4,-5,-6,-7,-8,-9,-18,-15,-16,-17,-3,-18,-22,-19,-20,-13,-14,-21,17,-11,17,-12,-10,]),'$end':([1,2,3,4,5,6,7,8,9,10,11,12,13,18,24,25,28,29,30,31,32,36,42,43,],[0,-1,-2,-4,-5,-6,-7,-8,-9,-18,-15,-16,-17,-3,-18,-22,-19,-20,-13,-14,-21,-11,-12,-10,]),'else':([4,5,6,7,8,9,10,11,12,13,24,25,28,29,30,31,32,36,42,43,],[-4,-5,-6,-7,-8,-9,-18,-15,-16,-17,-18,-22,-19,-20,-13,-14,-21,38,-12,-10,]),'operator':([6,10,11,12,13,23,24,25,26,27,28,29,30,31,32,39,],[19,-18,-15,-16,-17,19,-18,19,19,19,19,19,19,19,-21,19,]),'double_equals':([6,10,11,12,13,23,24,25,26,27,28,29,30,31,32,39,],[20,22,-15,-16,-17,20,-18,20,20,20,20,20,20,20,-21,20,]),'equals':([10,],[21,]),'rparen':([11,12,13,23,24,28,29,32,39,],[-15,-16,-17,32,-18,-19,-20,-21,41,]),'in':([11,12,13,24,26,28,29,32,],[-15,-16,-17,-18,33,-19,-20,-21,]),'colon':([11,12,13,24,27,28,29,32,38,41,],[-15,-16,-17,-18,34,-19,-20,-21,40,43,]),'range':([33,],[35,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'program':([0,],[1,]),'statement_list':([0,],[2,]),'statement':([0,2,34,40,],[3,18,36,42,]),'assignment':([0,2,34,40,],[4,4,4,4,]),'comparison':([0,2,34,40,],[5,5,5,5,]),'expression':([0,2,14,15,16,17,19,20,21,22,34,37,40,],[6,6,23,25,26,27,28,29,30,31,6,39,6,]),'print_statement':([0,2,34,40,],[7,7,7,7,]),'for_loop':([0,2,34,40,],[8,8,8,8,]),'if_statement':([0,2,34,40,],[9,9,9,9,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program","S'",1,None,None,None),
  ('program -> statement_list','program',1,'p_program','parser.py',8),
  ('statement_list -> statement','statement_list',1,'p_statement_list','parser.py',13),
  ('statement_list -> statement_list statement','statement_list',2,'p_statement_list','parser.py',14),
  ('statement -> assignment','statement',1,'p_statement','parser.py',22),
  ('statement -> comparison','statement',1,'p_statement','parser.py',23),
  ('statement -> expression','statement',1,'p_statement','parser.py',24),
  ('statement -> print_statement','statement',1,'p_statement','parser.py',25),
  ('statement -> for_loop','statement',1,'p_statement','parser.py',26),
  ('statement -> if_statement','statement',1,'p_statement','parser.py',27),
  ('for_loop -> for expression in range lparen expression rparen colon','for_loop',8,'p_for_loop','parser.py',32),
  ('if_statement -> if expression colon statement','if_statement',4,'p_if_statement','parser.py',38),
  ('if_statement -> if expression colon statement else colon statement','if_statement',7,'p_if_statement','parser.py',39),
  ('assignment -> identifier equals expression','assignment',3,'p_assignment','parser.py',49),
  ('comparison -> identifier double_equals expression','comparison',3,'p_comparison','parser.py',54),
  ('expression -> integer','expression',1,'p_expression','parser.py',59),
  ('expression -> float','expression',1,'p_expression','parser.py',60),
  ('expression -> string','expression',1,'p_expression','parser.py',61),
  ('expression -> identifier','expression',1,'p_expression','parser.py',62),
  ('expression -> expression operator expression','expression',3,'p_expression','parser.py',63),
  ('expression -> expression double_equals expression','expression',3,'p_expression','parser.py',64),
  ('expression -> lparen expression rparen','expression',3,'p_expression','parser.py',65),
  ('print_statement -> print expression','print_statement',2,'p_print_statement','parser.py',75),
  ('expression_list -> expression','expression_list',1,'p_expression_list','parser.py',80),
  ('expression_list -> expression_list comma expression','expression_list',3,'p_expression_list','parser.py',81),
]