from jooxdl import rs
def main(args):
    
    a=rs(args,debug=False,debug_lang="en")
    til=a.main()
    for _ in til:
        print(_)
    
if __name__ == '__main__':
    main('https://open.joox.com/s/rd?k=rq3UP')
    
