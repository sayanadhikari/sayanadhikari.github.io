import nbformat
import sys

filename = sys.argv[-1]
with open(filename) as f:
    nb = nbformat.read(f, as_version=4)

nb['metadata']['kernelspec'] = {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
}
nb['metadata']["language_info"] = {
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.5"
}

with open(filename, 'w', encoding='utf-8') as f:
    nbformat.write(nb, f)
