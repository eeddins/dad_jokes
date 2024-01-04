from diagrams import Cluster, Diagram
from diagrams.custom import Custom
from diagrams.programming.language import Python
from diagrams.onprem.ci import GithubActions
from diagrams import Node
from diagrams import Edge

# Define the attributes for the graph
graph_attr = {
    "layout": "dot",
    "concentrate": "true",
    "compound": "true",
    "splines": "spline",
    "fontsize": "45",
    "bgcolor": "white",
    "nodesep": "0.5",
    "ranksep": "2",
}

# Create a new Diagram with the specified attributes
with Diagram("Architecture", show=False, direction="LR", curvestyle="ortho", graph_attr=graph_attr):

    # Create a Cluster named "Github Repo" with two Custom nodes
    with Cluster("Github Repo", graph_attr={"fontsize":"15"}):
        cc_joke_of_the_day = Custom("jod.txt", "icons/textfile.png", height="1", width="0.75", imagescale="false", labelloc="t")
        cc_jokes_list = Custom("dadjokes.list", "icons/textfile.png", height="1", width="0.75", imagescale="false", labelloc="t")

    # Create a GithubActions node and two Python nodes
    cc_github_action = GithubActions("Github Action")        
    py_daily_dad_joke = Python("daily_dad_jokes.py")
    py_weekly_dad_joke = Python("dad_joke_scapper.py")

    # Create a Custom node for the website source
    cc_website_source = Custom("Website Source", "icons/website.png")

    # Define the edges between the nodes
    cc_github_action >> Edge(label="weekly cron") >> py_weekly_dad_joke >> Edge(label="git push", style="dotted") >> cc_jokes_list
    py_weekly_dad_joke >> Edge(label="fetch rss") >> cc_website_source
    cc_github_action >> Edge(label="daily cron") >> py_daily_dad_joke >> Edge(label="git push", style="dotted") >> cc_joke_of_the_day
    py_daily_dad_joke << cc_jokes_list
