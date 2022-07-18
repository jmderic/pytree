from .. import __main__

def test_argparse():
    args = __main__.parse_args(['.','-i','-c','-s'])
    assert (args.icons == True)
    assert (args.color == True)
    assert (args.size == True)
    assert (args.filt == "")
    assert (args.dir == False)

def test_main_call():
    __main__.main(['.','-ics'])
    assert(True)
