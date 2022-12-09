"""
This serves as the entry point into the program
Enter a name to search for their Bacon Number and press Enter

To quit Press "return" and enter
"""

if __name__ == "__main__":
    import sys
    from shortestPath import get_bacon_number
    from plotGraph import plot_graph
    name = input("Enter the name of the actor: ")
    while name.strip() != "return":
        if (name.strip() == ""):
            sys.exit()
        else:
            nodes = get_bacon_number(name.strip())
            if nodes:
                plot_graph(nodes)
        name = input("Enter the name of the actor: ")

    