import sys
from dataclasses import dataclass
class UDGraph: 
    def __init__(self):
        self.graph = dict() # create a dictionary as a member of the class

    #1
    def addVertex(self, vertex): # add a vertex to the graph
        if vertex not in self.graph: # check if vertex(key) already exists
            self.graph[vertex] = [] # initialize an empty list for the vertex
    
    #1
    def addEdge(self, from_vertex, to_vertex):    #add an edge to the graph
        # check if both vertices exist in the graph
        if from_vertex in self.graph and to_vertex in self.graph:   # en
            self.graph[from_vertex].append(to_vertex)
        else:
            #one or both vertices do not exist
            raise ValueError("One or both vertices not found in the graph.")
    
    #1
    def listOutgoingAdjacentVertex(self, vertex): #return the neighbours of a vertex
        return self.graph.get(vertex,[] ) 

    def check_has_vertex(self, vertex):
        return vertex in self.graph # return True if vertex exists, else False
    
    #checks the connection between two vertices(from_vertex -> to_vertex)
    def check_has_edge(self, from_vertex, to_vertex):
        if from_vertex in self.graph:
            return to_vertex in self.graph[from_vertex] # return True if edge exists
        return False #if from_vertex not in graph, return False
    
    def get_all_vertices(self):
        return list(self.graph.keys())
    
    def get_all_edges(self):
        edges = []
        for from_node, neighbours in self.graph.items():
            for to_node in neighbours:  
                edges.append((from_node, to_node))  # add edge as a tuple
        return edges

    def remove_edge(self, from_vertex, to_vertex):
        if from_vertex in self.graph:
            if to_vertex in self.graph[from_vertex]:
                self.graph[from_vertex].remove(to_vertex)
            else:
                raise ValueError(f"Edge {from_vertex} -> {to_vertex} does not exist.")
        else:
            raise ValueError(f"Vertex {from_vertex} does not exist.")

    def remove_vertex(self, vertex):
        if vertex not in self.graph:
            raise ValueError(f"Vertex {vertex} does not exist.")
        else:
            # Remove all edges to this vertex
            for v in self.graph:
                if vertex in self.graph[v]:
                    self.graph[v].remove(vertex)
            # Remove the vertex
            del self.graph[vertex]

    def incomingOf(self, v):    # return list of vertices that point to vertex v
        followers = []
        for u, nbrs in self.graph.items():
            if v in nbrs:
                followers.append(u)
        return followers
   
    #5(mandatory)
    def display(self):
        print("********************************************")
        print("Follow Gram, Who is Folloing Who Media App:")
        print("********************************************")
        print("1. View names of all profiles")
        print("2. View details for any profiles")
        print("3. View followers of any profile")
        print("4. View followed accounts of any profile")
        print("5. Add a new profile")
        print("6. Follow someone")
        print("7. Unfollow someone")
        print("8. Quit")
        print("********************************************")
        choice = input("Enter your choice (1 - 8): ")
        return choice
    
    #5(mandatory)
    def menuSelection(self, people, choice):
        choice = str(choice).strip()
        match choice:
            case "1":   # (1) View names of all profiles #5(mandatory)
                print("\nList of all profiles:")
                for uname in sorted(people.keys()):
                    print(f" > {uname}")

            case "2":   # (2) View details for any profile #5(mandatory)
                uname = input("\nEnter username to view profile: ").strip()
                p = people.get(uname)
                if uname not in people:
                    print("User not found.")
                #5(optional)
                else:
                    print(f"\n@{p.username}")
                    if p.privacy:  # True = public
                        print(f"Name     : {p.name}")
                        print(f"Gender   : {p.gender}")
                        print(f"Privacy  : Public")
                        print(f"Biography: {p.biography}")
                    else:          # False = private
                        print("Privacy  : Private")
                       
            case "3":   # (3) View followers (incoming) #5(mandatory)
                uname = input("\nEnter username to view followers: ").strip()
                if uname not in people:
                    print("User not found.")
                else:
                    followers = []
                    # Check every user u: if uname is in u's outgoing list, then u follows uname
                    for u in sorted(self.graph.keys()):
                        if uname in self.listOutgoingAdjacentVertex(u):    # get u's outgoing list
                            followers.append(u)

                    print(f"\nFollowers of @{uname} ({len(followers)}):")
                    if followers:
                        for u in followers:
                            print(f"{uname} <- {u}")
                    else:
                        print("No followers yet.")

            case "4":   # (4) View followed accounts #5(mandatory)
                uname = input("\nEnter username to view followed accounts: ").strip()
                if uname not in people:
                    print("User not found.")
                else:
                    following = self.listOutgoingAdjacentVertex(uname)  # get username's outgoing list
                    print(f"\n@{uname} is following ({len(following)}):")
                    if following:
                        for v in following:
                            print(f" {uname} -> {v}")
                    else:
                        print("This user isn't following anyone yet.")

            case "5":   # (5) Add a new profile #5(optional)
                print("\nAdd new profile:")
                new_username = input("Enter new username: ").strip()
                if not new_username:
                    print("Username cannot be empty.")
                elif new_username in people:
                    print("That username already exists.")
                else:
                    name = input("Enter full name: ").strip()
                    gender = input("Enter gender (M/F): ").strip()
                    biography = input("Enter biography: ").strip()
                    priv_input = input("Make profile public? (y/n): ").strip().lower()
                    privacy = True if priv_input == "y" else False
                    # create Person and add to dict + graph
                    people[new_username] = Person(new_username, name, gender, biography, privacy)
                    self.addVertex(new_username)
                    print(f"Profile @{new_username} created successfully.")

            case "6":   # (6) Follow someone #5(optional)
                print("\nFollow someone:")
                follower = input("Enter username of follower: ").strip()
                if follower not in people:
                    print("User not found.")
                else:
                    print("\nExisting profiles:")
                    for uname in sorted(people.keys()):
                        if uname != follower:
                            print(f" > {uname}")
                    followee = input("Enter username to follow: ").strip()
                    if followee not in people:
                        print("Target user not found.")
                    elif followee == follower:
                        print("A user cannot follow themselves.")
                    else:
                        try:
                            if self.check_has_edge(follower, followee):
                                print(f"{follower} is already following {followee}.")
                            else:
                                self.addEdge(follower, followee)
                                print(f"{follower} now follows {followee}.")
                        except ValueError as e:
                            print(e)

            case "7":   # (7) Unfollow someone #5(optional)
                print("\nUnfollow someone:")
                follower = input("Enter username of follower: ").strip()
                if follower not in people:
                    print("User not found.")
                else:
                    following = self.listOutgoingAdjacentVertex(follower)
                    if not following:
                        print(f"{follower} is not following anyone.")
                    else:
                        print(f"\n{follower} is currently following:")
                        for uname in following:
                            print(f" > {uname}")
                        followee = input("Enter username to unfollow: ").strip()
                        if followee not in following:
                            print(f"{follower} is not following {followee}.")
                        else:
                            try:
                                self.remove_edge(follower, followee)
                                print(f"{follower} has unfollowed {followee}.")
                            except ValueError as e:
                                print(e)

            case "8":   # (8) Quit
                print("\nThank you for using Slow Gram. Goodbye!")
                sys.exit(0)

            case _:
                print("\nInvalid choice. Please enter 1 - 8.")

        # small pause so CMD users can see output before next menu
        input("\nPress Enter to return to the menu...")

#2   
@dataclass  # for simple data container
class Person:   # for user profile
    username: str
    name: str
    gender: str
    biography: str
    privacy: bool   # True = public, False = private

if __name__ == "__main__":
    follow = UDGraph()

    #3   
    people = {
        "erin":   Person("erin",   "Erin Tan",      "F", "Cats & coffee", False),
        "jack":   Person("jack",   "Jack Lim",      "M", "Gaming & streaming", True),
        "dan":    Person("dan",    "Dan Ho",       "M", "Photography", True),
        "fahmi":  Person("fahmi",  "A. Fahmi",      "M", "Running & podcasts", False),
        "haris":  Person("haris",  "Haris Teh","M", "Car reviews & lifestyle", False),
        "gina":   Person("gina",   "Gina Wong",     "F", "Art & sketching", True),
    }    

    if len(people) > 10:
        people = dict(list(people.items())[:10])

    # add vertices as usernames 
    for uname in people.keys():
        follow.addVertex(uname)
    

    # 4  "someone follows someone" (not necessarily mutual)
    follow.addEdge("erin", "gina")
    follow.addEdge("jack", "dan")
    follow.addEdge("dan",  "jack")
    follow.addEdge("jack", "erin")
    follow.addEdge("dan",  "gina")
    follow.addEdge("fahmi","erin")
    follow.addEdge("haris","jack")
    follow.addEdge("gina", "erin")
    follow.addEdge("gina", "haris")


    # show menu
    while True:
        user_choice = follow.display()
        follow.menuSelection(people, user_choice)
