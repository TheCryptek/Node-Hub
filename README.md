# Node-Hub
Node-Hub is the first part of the Node Network Project, in which Node-Clients will be able to connect as long as they know what port and IP to use. So what
information will the Node-Hub receive?

If you look at the table below, it will be what the Node-Hub terminal looks
like to the server owner.

| Node | IP Address | Service | CPU Usage | RAM Usage |
|------|------------|---------|-----------|-----------|
| Node 1 | 127.0.0.1 | HTTPS | 4% | 8% |
| Node 2 | 127.0.0.2 | Minecraft Server | 35% | 45% |

This information is to establish what service the node is using, and the
system resource usage. The IP is visible to allow the Node owner to know
who is connect. 

# Why the information?
Node-Hub is being created so I can monitor my servers and what they are doing easily with my raspberry pi, instead of setting up a web interface or some
other solution I chose to go with this since I am a command line junkie. I
included the IP Address in the displayed information because I know that
their will be applications for this project that I am either not using
or someone will edit the code and either improve it or adapt it to their
situation.

