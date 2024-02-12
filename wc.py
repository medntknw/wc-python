import argparse
import os
import sys
import traceback
import locale

def get_stdout(res, files):
    out = ""
    ncols = len(res[0])
    total = [0] * ncols
    for i, fr in enumerate(res):
        for idx, c in enumerate(fr):
            total[idx] += fr[idx]
            out += f'{c} '
        out+=f'{files[i]}\n'
    if len(files) > 1:
        for i in range(ncols):
            out += f'{total[i]} '
        out += 'total\n'
    return out

def default_action(args):
    if not any([args.c, args.m, args.l, args.w]):
        args.c = True
        args.w = True
        args.l = True

def main(args):
    try:
        file_contents = []
        if not sys.stdin.isatty():
            content = sys.stdin.buffer.read() # taking in bytes
            file_contents.append(content)
        else:
            for file_path in args.files:
                if not os.path.isabs(file_path):
                    file_path = os.path.join(os.getcwd(), file_path)
                with open(file_path, 'rb') as fp:
                    content = fp.read()
            file_contents.append(content)
        res = []
        files = []
        for i, content in enumerate(file_contents):
            r = []
            f = args.files[i] if len(args.files) > 0 else ''
            files.append(f)
            if args.l:
                flines = content.decode('utf-8').count('\n') + (not content.decode('utf-8').endswith('\n'))
                r.append(flines)
            if args.w:
                words = len(content.split())
                r.append(words)
            if args.c:
                fsz = len(content)
                r.append(fsz)
            if args.m:
                encoding = locale.getpreferredencoding()
                try:
                    chars = len(content.decode(encoding))
                except:
                    chars = len(content)
                r.append(chars)
            res.append(r)
        sys.stdout.write(get_stdout(res, files))
    except Exception as ex:
        print(traceback.format_exc())
        sys.stderr.write(f'{str(ex)}\n')

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-c",
        help="The number of bytes in each input file is written to the standard output.This will cancel out any prior usage of the -m option.",
        action="store_true"
    )
    parser.add_argument(
        "-l",
        help="Write the length of the line containing the most bytes (default) or characters (when -m is provided) to standard output.  When more than one file argument is specified, the longest input line\
             of all files is reported as the value of the final “total”.",
        action="store_true"
    )
    parser.add_argument(
        "-w",
        help="The number of words in each input file is written to the standard output.",
        action="store_true"
    )
    parser.add_argument(
        "-m",
        help="The number of characters in each input file is written to the standard output.  If the current locale does not support multibyte characters, this is equivalent to the -c option.  This will\
             cancel out any prior usage of the -c option.",
        action="store_true"
    )
    parser.add_argument("files", help="Path to the file to be processed", nargs='*')
    parser.set_defaults(func=default_action)
    args = parser.parse_args()
    args.func(args)
    main(args)
