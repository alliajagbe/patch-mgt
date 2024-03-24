### This is the Descriptions and Details (explanations for easier reading) file for the Quantum Computing Project - `Prioritizing Patch Management for Cybersecurity using a Quantum-inspired Vertex Cover Algorithm` – undertook by `Ayush Sheth` and `Alli Ajagbe`. 

#### The citations through the document are as in Lit Review Sheet 2 

## What is Patch Management? What are its Applications in Cybersecurity? 
Patch management is a process used in cybersecurity to manage and apply patches or updates to software systems and devices. It involves identifying vulnerabilities, classifying assets, establishing patch management lists, and monitoring the patch status of devices<sup>[1]</sup>. Patch management is crucial for mitigating cybersecurity risks, ensuring production availability, and reducing maintenance costs<sup>[2]</sup>. It helps enterprises develop, implement, and monitor well-structured patch management programs, which are essential for risk management and compliance with regulations<sup>[3]</sup>. Patch management also addresses the complex challenges faced by enterprises in testing and deploying patches across their networks, improving workload visibility, and vulnerability management<sup>[4]</sup>. It enables the rapid injection of software patches into live applications without disrupting production workflows and facilitates threat information gathering and counterreconnaissance<sup>[5]</sup>. However, there is a need for further research and evaluation of patch management solutions, as many challenges remain unaddressed and only a small percentage of solutions have been rigorously evaluated in industrial settings. 

## What are Vertex Cover Graphs? 
A vertex cover in graph theory refers to a set of vertices that has a special property: every edge in the graph must have at least one of its endpoints in this set. In other words, a vertex cover touches every edge, ensuring that no edge is left uncovered. 

In the context of patch management, think of the graph as representing the software system or network infrastructure. The vertices in this graph correspond to software components, devices, or nodes within the system. The edges represent dependencies or interactions between these components or devices. Now, consider software vulnerabilities as the edges that need to be addressed (covered). A vertex cover in this context would be a minimal set of components or devices that need to be patched or updated to address these vulnerabilities. By ensuring that these critical vertices (components or devices) are patched, we effectively cover all the vulnerable edges (dependencies) in the system. 

- In terms of practical implementation: 
When managing patches, focus on the critical nodes (vertices) that impact the overall security and stability of the system. Identify the software components, servers, or devices that are most susceptible to vulnerabilities. Prioritize patching these critical vertices to minimize the risk of exploitation. Keep in mind that patching every single vertex (component) may not be feasible due to resource constraints or compatibility issues. Therefore, finding the optimal vertex cover (minimal set of patches) becomes crucial for effective patch management. 

Borrowed and Adapted from: [GeeksforGeeks](https://www.geeksforgeeks.org/introduction-and-approximate-solution-for-vertex-cover-problem/)<sup>[6]</sup>, [JuliaGraphs](https://juliagraphs.org/Graphs.jl/dev/algorithms/vertexcover/)<sup>[7]</sup>, [Brilliant](https://brilliant.org/wiki/vertex-cover/)<sup>[8]</sup>


## What are Vulnerability Graphs? 
Vulnerability graphs play a crucial role in understanding and managing security vulnerabilities within complex systems. 

A vulnerability graph is a graphical representation that captures the relationships between various software components, network nodes, or system elements and their associated security vulnerabilities. The definition is the same in the context of patch management as well.  
In these graphs, vertices represent individual components (such as software packages, devices, or servers), and edges depict the connections or dependencies between them. The presence of an edge between two vertices indicates that a vulnerability in one component may impact the security of another. 

Their applications in patch management are as follows: 

- Visualizing Dependencies: Vulnerability graphs help visualize intricate dependencies among components. Prioritize patching based on these connections. 
- Risk Assessment: Analyse the graph to determine which vulnerabilities pose the greatest threat. 
- Patch Management: Identify critical vertices (highly connected components) for effective patching. 
- Threat Modelling: Understand attack vectors and exploit paths using the graph.

Borrowed and Adapted from: [Guide to Enterprise Patch Management Planning - NIST](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-40r4.pdf)<sup>[9]</sup>, [Vulnerability Metrics for Graph-based Configuration Security](https://www.scitepress.org/Papers/2021/105594/105594.pdf)<sup>[10]</sup>, [Graph Vulnerability and Robustness: A Survey](https://arxiv.org/pdf/2105.00419.pdf)<sup>[11]</sup>
