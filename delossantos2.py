import copy


class Set:
    """
    Set class
    """
    def __init__(self, s1, s2, dt, sdt, item):
        self.set1 = s1
        self.set2 = s2
        self.data = dt
        self.setdata = sdt
        self.items = item
        self.result = []

    # Parser
    def parse(self, index):
        """
        Parse operation
        """
        self.result.clear()
        if int(self.items[index][0]) == 1:
            if self.data == 1 or self.data == 2:
                self.insert(int(self.items[index][1]), int(self.items[index][2]))
            elif self.data >= 3 and self.data <= 4:
                self.insert(int(self.items[index][1]), self.items[index][2])
            elif self.data == 5:
                self.insertset(int(self.items[index][1]), self.items[index][2])
        elif int(self.items[index][0]) == 2:
            if self.data == 1 or self.data == 2:
                self.remove(int(self.items[index][1]), int(self.items[index][2]))
            elif self.data >= 3 and self.data <= 4:
                self.remove(int(self.items[index][1]), self.items[index][2])
            elif self.data == 5:
                self.removeset(int(self.items[index][1]), self.items[index][2])
        elif int(self.items[index][0]) == 3:
            self.subset()
        elif int(self.items[index][0]) == 4:
            self.union()
        elif int(self.items[index][0]) == 5:
            self.intersection()
        elif int(self.items[index][0]) == 6:
            self.difference()
        elif int(self.items[index][0]) == 7:
            if int(self.items[index][1]) == 1:
                self.power(self.set1)
            elif int(self.items[index][1]) == 2:
                self.power(self.set2)

# TODO Implement powerset Wednesday
    def insertset(self, setter, value):
        """
        Insert set to a set
        """
        if '{' in value:
            if self.setdata == 1:
                tsplit = value[1:-1].split(',')
                value = sorted(list(map(int, tsplit)))
            elif self.setdata == 2:
                tsplit = value[1:-1].split(',')
                value = sorted(list(map(float, tsplit)))

        self.insert(setter, value)

    def insert(self, setter, value):
        """
        Insert item to a set
        """
        if setter == 1:
            if value not in self.set1:
                self.set1.append(value)
            else:
                pass
            self.preformat(self.set1)
        if setter == 2:
            if value not in self.set2:
                self.set2.append(value)
            else:
                pass
            self.preformat(self.set2)

    def removeset(self, setter, value):
        """
        Remove set from set
        """
        if '{' in value:
            if self.setdata == 1:
                tsplit = value[1:-1].split(',')
                value = list(map(int, tsplit))
            elif self.setdata == 2:
                tsplit = value[1:-1].split(',')
                value = list(map(float, tsplit))

        self.remove(setter, value)

    def remove(self, setter, value):
        """
        Remove item from a set
        """
        if setter == 1:
            if value in self.set1:
                self.set1 = [item for item in self.set1 if item != value]
            else:
                self.append("Not in set!")
            self.preformat(self.set1)

        if setter == 2:
            if value in self.set2:
                self.set2 = [item for item in self.set2 if item != value]
            else:
                self.append("Not in set!")
            self.preformat(self.set2)

    def subset(self):
        """
        If set 1 is a subset of set 2
        """
        if len(self.set1) > len(self.set2):
            self.append("false")
        elif len(self.set1) == len(self.set2) or len(self.set1) < len(self.set2):
            subset = 0
            iterator = 0
            while iterator < len(self.set1):
                if self.set1[iterator] in self.set2:
                    subset += 1
                iterator += 1
            if subset < len(self.set1):
                self.append("false")  # if not subset
            else:
                self.append("true")   # if subset

    def union(self):
        """
        Union of two sets
        """
        self.result = copy.copy(self.set1)
        for item in self.set2:
            if item not in self.result:
                self.result.append(item)
            else:
                continue
        self.preformat(self.result)

    def intersection(self):
        """
        Intersection of two sets
        """
        for item in self.set1:
            if item in self.set2:
                self.result.append(item)
            else:
                continue
        self.preformat(self.result)

    def difference(self):
        """
        Difference of two sets (S1-S2)
        """
        for item in self.set1:
            if item not in self.set2:
                self.result.append(item)
            else:
                continue
        self.preformat(self.result)

    def power(self, val):
        """
        Power set given a set
        """
        init = ['empty']
        for item in val:
            init.append(item)
        rest = (2**len(val))-len(init)
        if rest == 1:
            init.append(val)
            self.preformat(init)
        else:
            init.append('Not Implemented')
            self.preformat(init)

    def preformat(self, setter):
        """
        Preformat stage: Useful for set of sets
        """
        if self.data != 5:
            self.format(setter)
        else:
            tmpstr = str(setter)
            tmpstr = tmpstr.replace('[', '{')
            tmpstr = tmpstr.replace(']', '}')
            tmpstr = tmpstr.replace(' ', '')
            if "'" in tmpstr:
                tmpstr = tmpstr.replace("'", '')
            self.append(tmpstr)

    def format(self, lst):
        """
        Format stage: Useful for set of data types
        """
        string = '{'
        for item in lst:
            string += str(item) + ','
        string = string[:-1] + '}'
        self.append(string)

    def append(self, string):
        """
        Append to output file
        """
        with open('delossantos2.out', 'a') as file:
            file.write(string + '\n')
            file.close()


class Parser:
    """
    Parser class
    """
    def __init__(self):
        self.lineitems = []
        self.tmpline = []
        self.num_testcase = 0
        self.tmpdatatype = None
        self.tmpsetdatatype = None
        self.tmpset1 = None
        self.tmpset2 = None

    def tolist(self, line):
        """
        Convert each line of text to list
        """
        for item in line:
            self.tmpline = item.split(' ')
            self.lineitems.append(self.tmpline)
        self.num_testcase = len(self.lineitems)

    def parse(self, startline):
        """
        Convert textfile containing set codes into user-friendly
        set outputs
        """
        if startline + 1 == len(self.lineitems):
            return
        else:
            start = 1
            initset = 3
            position = 1 + startline
            operation = 0

            while initset > 0:
                if start == 1:
                    self.tmpdatatype = self.checktype(int(
                        self.lineitems[position][0]))
                    if self.tmpdatatype == 5:
                        self.tmpsetdatatype = self.checktype(int(
                            self.lineitems[position][1]))
                if start == 2:
                    self.tmpset1 = self.getset(self.lineitems[position])
                if start == 3:
                    self.tmpset2 = self.getset(self.lineitems[position])
                start += 1
                initset -= 1
                position += 1

            myset = Set(self.tmpset1, self.tmpset2,
                        self.tmpdatatype, self.tmpsetdatatype, self.lineitems)

            if start == 4:
                operation = int(self.lineitems[position][0])
                position += 1
                while operation > 0:
                    myset.parse(position)
                    operation -= 1
                    position += 1
            self.parse(position-1)

    def checktype(self, datatype):
        """
        checks datatype by number
        (1) int
        (2) double
        (3) char
        (4) string
        (5) set
        """
        return datatype

    def getset(self, tmplist):
        """
        Sets temporary list
        """
        if self.tmpdatatype == 1:
            return list(map(int, tmplist))
        elif self.tmpdatatype == 2:
            return list(map(float, tmplist))
        elif self.tmpdatatype >= 3 and self.tmpdatatype <= 4:
            return tmplist
        elif self.tmpdatatype == 5:
            tmpsetlist = []
            if self.tmpsetdatatype == 1:
                for index, item in enumerate(tmplist):
                    tsplit = tmplist[index][1:-1].split(',')
                    tmpsetlist.append(list(map(int, tsplit)))
                return tmpsetlist
            elif self.tmpsetdatatype == 2:
                for index, item in enumerate(tmplist):
                    tsplit = tmplist[index][1:-1].split(',')
                    tmpsetlist.append(list(map(float, tsplit)))
                return tmpsetlist
            elif self.tmpsetdatatype >= 3 and self.tmpsetdatatype <= 4:
                return tmplist


def main():
    """ main function """
    fileinput = input("Enter input file: ")
    with open(fileinput) as inputfile:
        line = [ln.strip() for ln in inputfile]

    open('delossantos2.out', 'w').close()
    setp = Parser()
    setp.tolist(line)
    setp.parse(0)
    print("Done! Open delossantos2.out.")

if __name__ == "__main__":
    main()
