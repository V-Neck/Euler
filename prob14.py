class Node:
    def __init__(self, data, next_node=None, is_root=False):
        self.data = data
        self.next = next_node
        self.is_root = is_root
        self.chain_length = None

    def print_to_root(self):
        cur_node = self
        while not cur_node.is_root:
            print str(cur_node.data) + "->",
            cur_node = cur_node.next
        print "1"

    def length(self):
        if self.chain_length != None:
            return self.chain_length
        else:
            l = 1
            cur_node = self
            while not cur_node.is_root:
                l += 1
                cur_node = cur_node.next
            return l

def collatz(node, graph):
    if node.data % 2 == 0:
        next_node_data = node.data / 2
    else:
        next_node_data = 3 * node.data + 1

    for i in xrange(len(graph)):
        if next_node_data == graph[i].data:
            node.next = graph[i]
            return node
    node.next = collatz(Node(next_node_data), graph)
    return node

def gen_collatz_chains(n, show_progress=False):
    percent = 0
    root = Node(1, is_root=True)
    graph = [root]
    for i in range(1, n + 1):
        if show_progress:
            cur_percent = int(100 * i / n)
            if percent != cur_percent:
                print cur_percent, "%"
            percent = cur_percent
        node = Node(i)
        graph.append(collatz(node, graph))
    return graph

if __name__ == "__main__":
    chains = gen_collatz_chains(10**6)

    longest = 0
    longest_chain = 0
    for chain in chains:
        length = chain.length()
        if length > longest:
            longest = length
            longest_chain = chain

    print longest_chain.data
