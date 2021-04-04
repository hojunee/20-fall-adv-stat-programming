def sed(src, dst, fin_dir, fout_dir):
    try:
        fin = open(fin_dir)
        fout = open(fout_dir, 'w')
        for line in fin:
            fout.write(line.replace(src, dst))
        fin.close()
        fout.close()
    except:
        print ("An Exception Occured")

sed("python", "C++", "in", "out")