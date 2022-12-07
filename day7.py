"""Advent of code 2022 - Day 7"""

import re

class File:
    """A file."""
    def __init__(self, size, name):
        self.size = size
        self.name = name

    def __str__(self):
        return f"File(size={self.size}, name={self.name})"

    def __repr__(self):
        return self.__str__()

    def __int__(self):
        return self.size

class Dir:
    """A directory in the structure."""
    def __init__(self, name:str, parent):
        self.name = name
        self.subdirs = {}
        self.files = []
        self.parent = parent

    def __repr__(self):
        return str(f"Directory(name={self.name})")

    def add_subdir(self, dname):
        """Add a subdirectory to this directory."""
        self.subdirs[dname] = Dir(dname, self)
 
    def add_file(self, fsize, fname):
        """Add a file to this directory."""
        self.files.append(File(fsize, fname))

    @property
    def size(self):
        """Return total size of directory (all files + subdirectories)"""
        return self._get_size()
    
    def _get_size(self):
        file_sums = sum([f.size for f in self.files])
        dir_sums = sum([self.subdirs[d].size for d in self.subdirs])
        return file_sums + dir_sums

class Filesystem:
    """A filesystem containing directories and properties."""
    def __init__(self, root:Dir, total_size:int):
        self.root = root
        self.total_size = total_size
    
    @property
    def unused(self):
        """Unused disk space."""
        return self._get_unused()

    def _get_unused(self):
        return self.total_size - self.used

    @property
    def used(self):
        """Used disk space."""
        return self._get_used_space()

    def _get_used_space(self):
        return self.root.size

    def get_space_delta(self, required):
        """Delta between required space and currently unused space."""
        return required - self.unused

    def find_smallest_dir_to_delete(self, requirement):
        """Get the Dir instance representing smallest directory to delete to meet requirement."""
        threshold = self.get_space_delta(requirement)
        qualified_dirs = _find_dirs_above_size(self.root, threshold)
        return _find_smallest_dir(qualified_dirs)


def main():
    data = _read_data("input/7.txt")
    root = _parse_structure(data)
    sum_of_qualified_dirs = _sum_of_dirs_below_threshold(root, 100000)

    print(f"Day 7, part 1: {sum_of_qualified_dirs}")

    filesystem_total = 70000000
    filesystem_required = 30000000

    filesystem = Filesystem(root, filesystem_total)
    delta = filesystem.get_space_delta(filesystem_required)
    smallest_to_delete = filesystem.find_smallest_dir_to_delete(filesystem_required)

    print(f"Day 7, part 1: {smallest_to_delete.size}")


def _parse_structure(data):
    root = Dir("/", None)
    cwd = root
    for line in data:
        if line.startswith("$ cd /"):
            cwd = root # keep track of cwd while parsing, point to a Dir instance.
            continue
        if line.startswith("$ cd .."):
            cwd = cwd.parent # go 1 level out
            continue
        if line.startswith("$ cd "):
            dname = line.split()[-1]
            cwd = cwd.subdirs[dname] # go 1 level in
            continue
        if line.startswith("$ ls"):
            ls = True
            continue
        if line.startswith("dir"):
            dname = line.split()[-1]
            cwd.add_subdir(dname)
            continue
        if re.match("\\d+ .", line):
            fsize, fname = line.split()
            fsize = int(fsize)
            cwd.add_file(fsize, fname)
            continue

    return root

def _sum_of_dirs_below_threshold(root, threshold):
    qualified_dirs = _find_dirs_below_size(root, threshold)
    return sum([d.size for d in qualified_dirs])


def _find_dirs_below_size(dir, threshold):
    qualified_dirs = []
    if dir.size <= threshold:
        qualified_dirs.append(dir)
    
    if dir.subdirs:
        for dname, subdir in dir.subdirs.items():
            qualified_dirs += _find_dirs_below_size(subdir, threshold)

    return qualified_dirs

def _find_smallest_dir(dirs):
    """Sort dirs by size, return smallest"""
    dirs_dict = {d:d.size for d in dirs}
    sorted_dirs = {k: v for k, v in sorted(dirs_dict.items(), key=lambda item: item[1])}
        
    return [d for d, _ in sorted_dirs.items()][0]


def _find_dirs_above_size(dir, threshold):
    qualified_dirs = []
    if dir.size > threshold:
        qualified_dirs.append(dir)
    
    if dir.subdirs:
        for dname, subdir in dir.subdirs.items():
            qualified_dirs += _find_dirs_above_size(subdir, threshold)

    return qualified_dirs

def _read_data(fin):
    with open(fin, "r") as file:
        lines = [x.strip() for x in file.readlines()]

    return lines

if __name__ == "__main__":
    main()