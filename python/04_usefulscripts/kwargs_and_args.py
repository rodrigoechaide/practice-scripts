import sys

def test_var_args(f_arg, f_arg2, *argv):
    print "first normal arg:", f_arg
    print "second normal arg:", f_arg2
    for arg in argv:
        print "another arg through *argv :", arg


test_var_args('yasoob','python','eggs','test', 'test2')

sys.argv.pop(0)
args = tuple(sys.argv)

test_var_args(*args)

