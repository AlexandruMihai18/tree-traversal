from tree import Tree
from node import Node

class TestTree(object):

	def test_find1(self):
		tree = Tree()
		tree.add(3)
		tree.add(4)
		tree.add(0)
		tree.add(8)
		tree.add(2)
		assert tree.find(5) == None
	
	def test_find2(self):
		tree = Tree()
		tree.add(3)
		tree.add(4)
		tree.add(0)
		tree.add(8)
		tree.add(2)
		assert tree.find(4).data == 4
	