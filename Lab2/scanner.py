#!/usr/bin/python

import sys

import ply.lex as lex


class Scanner:

    def __init__(self, text) -> None:
        self.text = text
        self.lexer = lex.lex(object=self)
        Scanner.text = text

    text = ""
    reserved = {
        'print': 'PRINT',
        'eye': 'EYE',
        'ones': 'ONES',
        'zeros': 'ZEROS',
        'break': 'BREAK',
        'continue': 'CONTINUE',
        'return': 'RETURN',
        'while': 'WHILE',
        'for': 'FOR',
        'if': 'IF',
        'else': 'ELSE'
    }

    tokens = [
                 'LEQ',
                 'GEQ',
                 'NOTEQ',
                 'EQUAL',
                 'ASSIGN',
                 'ADDASSIGN',
                 'SUBASSIGN',
                 'MULASSIGN',
                 'DIVASSIGN',

                 'COMMA',
                 'SEMICOLON',
                 'APOSTROPHE',

                 'FLOAT',
                 'INT',
                 'STRING',

                 'DOTADD',
                 'DOTSUB',
                 'DOTMUL',
                 'DOTDIV',
                 'ID'
             ] + list(reserved.values())

    t_COMMA = r','
    t_SEMICOLON = ';'
    t_APOSTROPHE = '\''
    
    t_DOTADD = r'\.\+'
    t_DOTSUB = r'\.-'
    t_DOTMUL = r'\.\*'
    t_DOTDIV = r'\./'

    t_STRING = r'"[\^]\*"'

    # t_PRINT = r'print'
    # t_EYE = r'eye'
    # t_ONES = r'ones'
    # t_ZEROS = r'zeros'
    # t_CONTINUE = r'continue'
    # t_RETURN = r'return'
    # t_WHILE = r'while'
    # t_FOR = r'for'
    # t_IF = r'if'
    # t_ELSE = r'else'

    t_LEQ = r'<='
    t_GEQ = r'>='
    t_NOTEQ = r'!='
    t_EQUAL = r'=='

    t_ASSIGN = r'='
    t_ADDASSIGN = r'\+='
    t_SUBASSIGN = r'-='
    t_MULASSIGN = r'\*='
    t_DIVASSIGN = r'/='  

    def t_ID(t):
        r'[A-Za-z_][A-Za-z0-9_]*'
        t.type = Scanner.reserved.get(t.value, 'ID')  # Check for reserved words
        return t

    literals = ['+', '-', '*', '/', '(', ')', '[', ']', '{', '}', '=', '<', '>',
                ':', "'", ',', ';', '\"']

    t_ignore = ' \t'

    def t_FLOAT(t):
        r'([0-9]*[.])[0-9]+(e-?[0-9]+)?'
        t.value = float(t.value)
        return t

    def t_INT(t):
        r'\d+'
        t.value = int(t.value)
        return t

    def t_COMMENT(t):
        r'\#.*\n*'
        t.lexer.lineno += t.value.count('\n')
        pass

    def t_newline(t):
        r'\n+'
        t.lexer.lineno += len(t.value)

    def t_error(t):
        print("line %d, col %d: illegal character '%s'" % (
        t.lineno, Scanner.find_column(t), t.value[0]))
        t.lexer.skip(1)

    def find_column(token):
        line_start = Scanner.text.rfind('\n', 0, token.lexpos) + 1
        return (token.lexpos - line_start) + 1
