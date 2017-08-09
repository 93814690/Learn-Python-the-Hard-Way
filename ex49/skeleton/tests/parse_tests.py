from nose.tools import *
from ex48 import lexicon
from ex49 import parse

def test_peek():
    word_list = lexicon.scan("eat the door")
    assert_equal(parse.peek(word_list), 'verb')

def test_match():
    word_list = lexicon.scan("eat the door")
    assert_equal(parse.match(word_list, 'verb'), ('verb', 'eat'))
    assert_equal(word_list, [('stop', 'the'), ('noun', 'door')])

def test_skip():
    word_list = lexicon.scan("eat the door")
    parse.skip(word_list, 'verb')
    assert_equal(word_list, [('stop', 'the'), ('noun', 'door')])

def test_verb():
    word_list = lexicon.scan("eat the door")
    result = parse.parse_verb(word_list)
    assert_equal(result, ('verb', 'eat'))

def test_object():
    word_list = lexicon.scan("the door open")
    result = parse.parse_object(word_list)
    assert_equal(result, ('noun', 'door'))

    word_list = lexicon.scan("at north")
    result = parse.parse_object(word_list)
    assert_equal(result, ('direction', 'north'))

def test_subject():
    word_list = lexicon.scan("eat the door")
    result = parse.parse_subject(word_list, ('noun', 'player'))
    assert_equal(result.subject, 'player')
    assert_equal(result.verb, 'eat')
    assert_equal(result.object, 'door')

def test_sentence():
    word_list = lexicon.scan("bear go east")
    result = parse.parse_sentence(word_list)
    assert_equal(result.subject, 'bear')
    assert_equal(result.verb, 'go')
    assert_equal(result.object, 'east')
