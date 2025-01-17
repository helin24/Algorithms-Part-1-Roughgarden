import math

class BinaryTree:
    def __init__(self, alist=[]):
        self.rep = []
        for number in alist:
            self.insert(number)
        # can augment to have size metric on each node


    def __str__(self):
        pointer = 1
        size = len(self.rep)
        string = ""
        levels = math.ceil(math.log(size, 2))
        max_width = (2**(levels) + 1) * 5

        while pointer <= size:
            level = math.floor(math.log(pointer, 2))
            remaining = 2** level
            step = ' ' * int(max_width / (remaining + 1))

            while remaining and pointer <= size:
                string += step + str(self.rep[pointer - 1])
                pointer += 1
                remaining -= 1

            string += "\n\n"

        return string


    def min(self, index=0):
        min_num = None
        
        while index < len(self.rep) and self.rep[index] != None:
            min_num = self.rep[index]
            index = 2 * index + 1

        return min_num


    def max(self, index=0):
        max_num = None

        while index < len(self.rep) and self.rep[index] != None:
            max_num = self.rep[index]
            index = 2 * (index + 1)

        return max_num


    def find(self, value):
        index = 0
        answer = None

        while index < len(self.rep) and self.rep[index] != None:
            if value == self.rep[index]:
                answer = index
                break
            elif value < self.rep[index]:
                index = 2 * index + 1
            else:
                index = 2 * (index + 1)

        return answer


    def left_child(self, index=0):
        if 2 * index + 1 < len(self.rep) and self.rep[2 * index + 1] != 0:
            return self.rep[2 * index + 1], 2 * index + 1
        else:
            return None, 2 * index + 1
        

    def right_child(self, index=0):
        if 2 * (index + 1) < len(self.rep) and self.rep[2 * (index + 1)] != 0:
            return self.rep[2 * (index + 1)], 2 * (index + 1)
        else:
            return None, 2 * (index + 1)


    def parent(self, index):
        parent_index = (index - 1) / 2
        if parent_index >= 0:
            return self.rep[parent_index], parent_index
        else:
            return None, None
        

    def predecessor(self, sub):
        index = self.find(sub)
        left_child, left_index = self.left_child(index)
        if left_child:
            return self.max(left_index)
        else:
            parent, parent_index = self.parent(index)
            while parent:
                if parent < sub:
                    return parent
                else:
                    parent, parent_index = self.parent(parent_index)
        return None

    def successor(self, sub):
        index = self.find(sub)
        right_child, right_index = self.right_child(index)
        if right_child:
            return self.max(right_index)
        else:
            parent, parent_index = self.parent(index)
            while parent:
                if parent > sub:
                    return parent
                else:
                    parent, parent_index = self.parent(parent_index)
        return None


    def insert(self, number):
        index = 0

        if len(self.rep) == 0:
            self.rep.append(number)
            return index
        
        while index < len(self.rep) and self.rep[index] != None:
            if self.rep[index] >= number:
                index = 2 * index + 1
            else:
                index = 2 * (index + 1)

        if index > len(self.rep):
            self.rep.extend([None] * (index - len(self.rep)))
            self.rep.append(number)
        elif index == len(self.rep):
            self.rep.append(number)
        else:
            self.rep[index] = number

        return index


    def delete(self, number):
        pass

    def select(self, rank):
        pass

    def rank(self, value):
        pass


t = BinaryTree([5,2,7,3,4])
print t
t.insert(8)
print t
t.insert(6)
print t
print t.min()
t.insert(0)
print t.min()
print t.max()
print t.find(8)
t.insert(1)
print t
print t.successor(0)

