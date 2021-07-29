# Contact: Sara Ferreira [sara (dot) ferreira (at) fc (dot) up (dot) pt]
#
# This is free and unencumbered software released into the public domain.
#
# Anyone is free to copy, modify, publish, use, compile, sell, or
# distribute this software, either in source code form or as a compiled
# binary, for any purpose, commercial or non-commercial, and by any
# means.
#
# In jurisdictions that recognize copyright laws, the author or authors
# of this software dedicate any and all copyright interest in the
# software to the public domain. We make this dedication for the benefit
# of the public at large and to the detriment of our heirs and
# successors. We intend this dedication to be an overt act of
# relinquishment in perpetuity of all present and future rights to this
# software under copyright law.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
# IN NO EVENT SHALL THE AUTHORS BE LIABLE FOR ANY CLAIM, DAMAGES OR
# OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,
# ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
# OTHER DEALINGS IN THE SOFTWARE.

import sys 
import pickle


if len(sys.argv) != 3:
    print("Not enough arguments")
    print("insert pkl filename and output filename")
    print("pkl_to_txt.py <pkl> <output>")
    exit()

filename=sys.argv[1]
output_filename=sys.argv[2]

try:
    pkl_file = open(filename, 'rb')
except OSError:
    print("Could not open/read file:")
    exit()
data = pickle.load(pkl_file)
pkl_file.close()

X_train = data["data"]
y_train= data["label"]

f = open(output_filename+".txt", "a")

for i in range(0, len(X_train)):
    f.write("Sample "+str(i)+": \n"+"features: "+str(X_train[i])+"label: "+str(y_train[i])+"\n")

f.close()
