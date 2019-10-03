# Build Order: You are given a list of projects and a list of dependencies (which is a list of pairs of
# projects, where the second project is dependent on the first project). All of a project's dependencies
# must be built before the project is. Find a build order that will allow the projects to be built. If there
# is no valid build order, return an error.
# EXAMPLE
# Input:
# projects: a, b, c, d, e, f
# dependencies: (a, d), (f, b), (b, d), (f, a), (d, c)
# Output: f, e, a, b, d, c

projects = ['a','b','c','d','e','f']
dependencies = {
    'a': ['d'],
    'b': ['d'],
    'c': [],
    'd': ['c'],
    'e': [],
    'f': ['b']
}

def order_projects(projects: list, dependencies: dict):
    result = []
    visited = set()

    for project in projects:
        if project not in visited:
            do_dfs(project, dependencies, result, visited)
    
    return result

def do_dfs(project, dependencies, result: list, visited):
    visited.add(project)

    for d in dependencies[project]:
        if d not in visited:
            do_dfs(d, dependencies, result, visited)

    result.insert(0, project)

if __name__ == "__main__":
    print(order_projects(projects, dependencies))