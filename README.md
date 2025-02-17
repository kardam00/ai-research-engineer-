# ai research engineer (agentic reasoning & tool use)

## Non-Coding Component

## A. Conceptual Map for Agentic Reasoning & Tool Use in LLMs

### **I. Extracting Core Concepts from Each Paper**

**1. ReAct: Synergizing Reasoning and Acting in Language Models**
- **Approach**: Combines reasoning and acting in an interleaved fashion.
- **Key Mechanism:**
  - Generates reasoning traces (thoughts).
  - Executes actions based on reasoning.
  - Uses external sources (e.g., Wikipedia) to verify and refine responses.
- **Workflow:**
  - User Query → Thought Generation → Action Execution → Observation Integration → Final Answer
- **Strengths:**
  - Reduces hallucinations by grounding reasoning in external information.
  - Provides interpretability through explicit reasoning traces.

**2. Toolformer: Self-Supervised Learning of Tool Use**
- **Approach:** Enables LLMs to learn when and how to use external tools in a self-supervised manner.
- **Key Mechanism:**
  - Uses API calls to retrieve external information.
  - Incorporates API results into token prediction.
  - Trains using a perplexity-based filtering approach (removes unhelpful API calls).
- **Workflow:**
  - User Query → Model Decides API Call → API Execution → API Response Integration → Final Answer
- **Strengths:**
  - No need for human-annotated data.
  - Learn tool usage autonomously.

**3. ReST meets ReAct: Self-Improvement for Multi-Step Reasoning Agents**
- **Approach:** Enhances ReAct by introducing self-critique and iterative training.
- **Key Mechanism:**
  - Uses Reinforced Self-Training (ReST) for continuous improvement.
  - Generates synthetic reasoning traces and fine-tunes itself.
  - Uses search-based evaluation to refine responses.
- **Workflow:**
  - User Query → Initial Answer → Self-Critique → Iterative Refinement → Final Response
- **Strengths:**
  - Reduces errors through self-improvement.
  - Increases robustness in multi-step reasoning.

**4. Chain of Tools: Automatic Multi-Tool Learning**
- **Approach:** Empowers LLMs to autonomously discover and use a sequence of tools.
- **Key Mechanism:**
  - Uses Automatic Tool Chain (ATC) to determine tool dependencies.
  - Implements black-box probing to discover new tools.
  - Uses programmatic execution instead of human-defined workflows.
- **Workflow:**
  - User Query → Tool Selection → Multi-Step Execution → Error Handling & Refinement → Final Answer
- **Strengths:**
  - Handles complex workflows.
  - Learn new tools dynamically.

**5. Language Agent Tree Search (LATS): Planning & Decision-Making with LLMs**
- **Approach:** Uses Monte Carlo Tree Search (MCTS) to optimize reasoning paths.
- **Key Mechanism:**
  - Expands ReAct by exploring multiple reasoning steps simultaneously.
  - Uses heuristics and self-reflection to select the best reasoning trajectory.
- **Workflow:**
  - User Query → Multi-Path Search → Evaluation & Pruning → Best Path Execution → Final Answer
- **Strengths:**
  - Optimizes reasoning steps.
  - Adapts dynamically based on previous errors.

### **II. Identifying Common Themes & Differences**

| Paper | Reasoning Type | Tool Use | Self-Improvement | Strengths |
|---|---|---|---|---|
| **ReAct** | Thought-action-observation loops | External sources (e.g., Wikipedia) | No | Improves reasoning interpretability |
| **Toolformer** | Single-step decision-making | API-based tool execution | No | Learns tool use autonomously |
| **ReST + ReAct** | Iterative refinement loops | Search API + AI feedback | Yes | Enhances multi-step reasoning accuracy |
| **Chain of Tools** | Multi-tool sequence execution | Dynamic discovery of new tools | Limited (error handling) | Automates complex workflows |
| **LATS** | Multi-path decision-making |External information sources | Yes | Optimizes reasoning and tool selection |

### **III. Creating a Flow Diagram**

**Generalized Conceptual Map for Tool-Using LLMs**

| User Query Input |
|:----------------:|
|      &#8595;     |
| Reasoning Loop <br> (LLM decides) |
|      &#8595;     |
| Tool Selection <br> (API Calls, Search) |
|      &#8595;     |
| Tool Invocation <br> (Execution) |
|      &#8595;     |
| Tool Responses <br> (Parsed Results) |
|      &#8595;     |
| Final Agent Response <br> (Answer to User) |

## B. Research Paper Analysis: Agentic Reasoning & Tool Use in LLMs

### **I. Paper Summaries**

**1. ReAct: Synergizing Reasoning and Acting in Language Models**
- **Main Idea:** ReAct introduces an approach where LLMs interleave reasoning (thoughts) and actions, allowing them to make decisions dynamically while interfacing with external tools.
- **Reasoning Implementation:** The model generates thoughts before each action, enabling it to track progress, adjust its plan, and reduce hallucinations.
- **Tool Use Management:** The agent decides dynamically when to invoke external tools, such as a Wikipedia search API, and integrates retrieved information into its reasoning.
- **Key Strength:** Enhances interpretability, reduces hallucinations, and performs well in multi-turn decision-making tasks.

**2. Toolformer: Self-Supervised Learning of Tool Use**
- **Main Idea:** Toolformer enables LLMs to autonomously learn when and how to use external tools without human supervision by fine-tuning on API calls.
- **Reasoning Implementation:** Instead of explicit reasoning, Toolformer learns tool use patterns from self-supervised data and predicts tool calls based on context.
- **Tool Use Management:** The model inserts tool calls into text automatically and decides whether an API response improves its token prediction.
- **Key Strength:** Reduces human involvement in tool selection and execution while improving efficiency across various tasks (e.g., arithmetic, fact-checking, and translations).
    
**3. ReST meets ReAct: Self-Improvement for Multi-Step Reasoning Agents**
- **Main Idea:** ReST extends ReAct by incorporating self-reflection and reinforcement learning to iteratively refine reasoning steps.
- **Reasoning Implementation:** The model self-critically evaluates its past outputs, refines its decision-making, and improves responses over multiple iterations.
- **Tool Use Management:** Similar to ReAct, but with added layers of self-revision and reinforcement-based learning, improving its ability to integrate external knowledge effectively.
- **Key Strength:** Enables self-improvement over time, making it more robust in multi-step reasoning tasks.

**4. Chain of Tools: Automatic Multi-Tool Learning**
- **Main Idea:** This approach empowers LLMs to use multiple tools sequentially by autonomously discovering tool dependencies and executing workflows.
- **Reasoning Implementation:** The model follows a step-by-step tool execution plan, ensuring efficient tool selection and coordination.
- **Tool Use Management:** The agent dynamically selects and chains tools together to complete a task, instead of relying on predefined tool sequences.
- **Key Strength:** Optimized for complex multi-step tasks, making it suitable for automation-heavy applications.

**5. Language Agent Tree Search (LATS): Planning & Decision-Making with LLMs**
- **Main Idea:** LATS introduces Monte Carlo Tree Search (MCTS) for LLMs, optimizing decision-making by exploring multiple reasoning paths before selecting the best one.
- **Reasoning Implementation:** Instead of relying on a single-step decision, LATS searches over multiple paths, evaluates them, and chooses the best reasoning trajectory.
- **Tool Use Management:** The model considers several reasoning chains, integrates external feedback, and uses heuristics to refine tool selection dynamically.
- **Key Strength:** Best suited for long-horizon planning and adaptive problem-solving, making it ideal for complex reasoning tasks.

### **II. Comparative Table**
| Paper | Reasoning Approach | Tool Use Strategy | Self-Improvement | Key Strength |
| --- | --- | --- | --- | --- |
| ReAct | Interleaved thinking & acting | Calls tools as needed | No | Works well in multi-turn interactions |
| Toolformer | Inserts tool calls in text | Uses fine-tuning for tool discovery | No | Reduces human involvement in tool selection |
| ReST + ReAct | Iterative reflection & correction | Tool use similar to ReAct | Yes | Improves multi-step reasoning | 
| Chain of Tools | Sequential tool use planning | Uses multiple tools per query | No | Optimized for automation |
| LATS | Tree search for planning | Optimized tool use based on search space | Yes | Best for long-horizon planning |

### **III. Compare & Contrast Methodologies**

**1. How does tool invocation differ?**
- **ReAct:** Decides dynamically in a reasoning loop.
- **Toolformer:** Pre-learns when to call APIs and embeds calls within text.
- **ReST + ReAct:** Uses reflection and revision to improve tool use over time.
- **Chain of Tools:** Plans multiple tool calls in sequence, ensuring efficient execution.
- **LATS:** Uses search-based planning to optimize tool selection dynamically.

**2. Which one is more flexible?**
- **LATS** and **ReST** allow for reflection and iteration, making them adaptive in complex reasoning tasks.
- **Chain of Tools** is also highly flexible in multi-tool execution scenarios.

**3. Which one is more efficient?**
- **Toolformer** is the most automated, reducing unnecessary tool calls.
- **Chain of Tools** is highly optimized for workflow automation.
- **ReAct** provides efficiency in multi-turn interactions.
    
### **IV. Assessing Real-World Applicability**

**1. Which model would work best for a personal shopping assistant?**
- **ReAct** and **Chain of Tools** are the most suitable because they can:
  - Interpret user queries dynamically.
  - Invoke multiple tools as needed.
  - Adjust reasoning based on tool outputs (e.g., checking price comparisons, applying discount codes, estimating shipping times).
- **LATS** could also be useful for optimizing longer decision-making processes, such as recommending personalized shopping strategies.

**2. Other Potential Use Cases**
- **ReAct:** Customer support agents that need to interact with knowledge bases.
- **Toolformer:** Automating API-driven processes like data retrieval and calculations.
- **ReST + ReAct:** Research assistants that require iterative refinement of answers.
- **Chain of Tools:** Automated business workflows that involve multiple interconnected APIs.
- **LATS:** Complex decision-making tasks like financial planning, medical diagnostics, or game-playing AI.

## C. Open Questions & Future Improvements: LLM-Based Agentic Reasoning & Tool Use

### **I. Key Challenges in Deploying LLM Agents**

**1. Scalability:** Handling Large-Scale Deployments
- **Issue:** Most existing approaches (e.g., ReAct, Toolformer) are evaluated on small datasets. However, in real-world applications like e-commerce assistants or research agents, LLMs may need to handle millions of tool calls per day.
- **Challenges:**
  - High computational costs associated with frequent API calls.
  - Bottlenecks in sequential tool execution (e.g., waiting for search results).
  - Increased latency, making real-time responses impractical.

**2. Adaptability: Learning New Tools Dynamically**
- **Issue:** Models like Toolformer and Chain of Tools require predefined APIs and tool instructions. But real-world scenarios involve new tools emerging frequently (e.g., new shopping platforms, new pricing APIs).
- **Challenges:**
  - Manual intervention is needed to integrate new tools.
  - Models struggle to generalize beyond their training set.
  - Lack of self-learning mechanisms for discovering new tools.

**3. Error Handling: Dealing with Incorrect or Failing Tool Outputs**
- **Issue:** Current models assume that tool outputs are reliable (e.g., ReAct assumes Wikipedia provides correct information). However, in practice:
  - APIs can return incorrect or outdated results.
  -  Some API calls may fail due to server downtime or bad input formatting.
- **Challenges:**
  - No built-in fallback mechanisms when tool responses are incorrect.
  - Lack of confidence estimation (models can’t assess if a tool’s response is trustworthy).
  - **ReAct** and **Chain of Tools** do not self-correct tools use errors dynamically.

**4. Integration Complexity: Working with Real-World APIs**
- **Issue:** Most research models (e.g., Toolformer, Chain of Tools) test tool usage in controlled environments with mock APIs. However, real-world APIs (e.g., Google Shopping, Shopify, OpenWeather) come with:
  - **Rate limits** (limited requests per minute).
  - **Authentication & security** requirements.
  - **Complex data formats** (e.g., JSON structures, paginated results).
- **Challenges:**
  - **Adapting models** to different API response structures.
  - **Managing authentication** (e.g., API keys, OAuth tokens).
  - **Ensuring compliance** with API usage policies.

### **II. Proposed Solutions & Improvements**

**1. Reducing Latency**
- **Current Issue:** Models like ReAct and Chain of Tools execute tool calls sequentially, leading to high response times.
- **Solution:** Implement parallel execution of tool calls where possible.
- **Example:** Instead of waiting for a search query to complete before checking for a discount code, the model can call both APIs simultaneously.

**2. Enhancing Adaptability**
- **Current Issue:** Toolformer and Chain of Tools rely on predefined APIs and do not automatically learn new tools.
- **Solution:** Introduce meta-learning frameworks where models:
  - Analyze tool documentation dynamically.
  - Use few-shot learning to test API calls before integrating them.
  - Implement a feedback loop that allows the model to refine how it interacts with newly discovered tools.

**3. Improving Error Handling**
- **Current Issue:** No robust system exists for detecting and correcting faulty tool responses.
- **Solution:**
  - Implement confidence scores before using tool outputs (e.g., "Is this tool’s response reliable?").
  - Integrate self-verification mechanisms (e.g., if a tool provides incorrect shipping costs, cross-check with another source).
  - Use multi-agent approaches where one agent validates another's output.

**4. Optimizing Multi-Agent Collaboration**
- **Current Issue:** Most current approaches assume a single LLM agent making all decisions.
- **Solution:** Introduce multi-agent systems where:
  - One agent specializes in reasoning.
  - Another handles tool selection.
  - A third agent validates outputs before presenting them to users.
- **Example:** Instead of one agent handling an entire shopping query, different agents could specialize in:
  - Searching for the product.
  - Applying discounts.
  - Comparing competitor prices.

### **III. Identifying Research Gaps**

**1. Lack of Multi-Modal Reasoning**
- **Current Issue:** All papers focus only on text-based reasoning.
- **Research Gap:** LLMs should also process images, videos, and structured data.
- **Example:** A shopping assistant should be able to analyze product images along with textual descriptions.

**2. Lack of Self-Monitoring Capabilities**
- **Current Issue:** Models do not track their own mistakes.
- **Research Gap:** Develop LLMs that:
  - Track reasoning failures.
  - Maintain long-term memory to avoid repeating errors.
- **Example:** If an LLM repeatedly fails to apply a discount, it should recognize the pattern and attempt a different approach.

### **IV. Future Research Directions**

**1. Multi-Modal Reasoning Agents**
- Expand LLMs beyond text processing:
  - Integrate image recognition (e.g., understanding product photos).
  - Process structured data (e.g., reading price trends from CSV files).
  - **Example:** A fashion shopping agent could analyze trending styles from Instagram before making recommendations.

**2. Advanced Error Correction Mechanisms**
- Develop more robust self-improvement strategies:
  - Implement automated reasoning audits to flag incorrect tool use.
  - Use human-in-the-loop validation to correct errors dynamically.
  - **Example:** An LLM assistant should be able to cross-check Wikipedia sources for fact verification before using them.

**3. Multi-Agent Collaboration Frameworks**
- Shift from single-agent to multi-agent systems:
  - Allow multiple LLMs to collaborate for better performance.
  - One agent could specialize in searching, another in pricing, and a third in returns & policies.
  - **Example:** In e-commerce, different agents could handle:
    - Searching for items.
    - Applying discounts.
    - Checking competitor prices.
    - Verifying return policies.

**4. Real-World API Adaptation**
- Research more robust API integration techniques:
  - Develop models that can adapt to different API structures automatically.
  - Implement API authentication management.
  - Use caching mechanisms to minimize redundant API calls.
  - Example: A shopping assistant should seamlessly switch from Amazon APIs to Shopify APIs when required.

## Coding component: Personal Online Fashion Shopping Agent

### Project Overview

This project implements a virtual shopping assistant that helps users navigate multiple fashion e-commerce platforms. The agent utilizes agentic reasoning and tool use to interpret user queries, invoke appropriate external tools, and provide well-structured responses.

### Objective
- Demonstrate how LLMs leverage reasoning and tool use to perform complex tasks.
- Implement a personal shopping assistant capable of product search, price comparison, shipping estimates, discount application, and return policy retrieval.
- Evaluate the performance of the agent through test cases and example outputs.

### Key Research Papers Referenced
The design of this agent is inspired by the following research papers:
1. ReAct: Synergizing Reasoning and Acting in Language Models
2. Toolformer: Language Models Can Teach Themselves to Use Tools
3. ReST meets ReAct: Self-Improvement for Multi-Step Reasoning LLM Agent
4. Chain of Tools: Large Language Model is an Automatic Multi-tool Learner
5. Language Agent Tree Search Unifies Reasoning, Acting, and Planning in Language Models

### Project Structure
```
├── agent.py             # Core agent logic (intent extraction, tool invocation, response synthesis)
├── tools.py             # Tool implementations (product search, shipping, discounts, etc.)
├── test_agent.py        # Test cases to validate agent functionality
├── output.txt           # Sample interactions & agent responses
├── README.md            # Project documentation
└── requirements.txt     # (Optional) Dependencies
```

### Agent Architecture
1. Intent Extraction: The agent processes user input using Google Gemini Pro to extract structured intent.
2. Tool Invocation: Based on extracted intent, the agent calls appropriate tools.
3. Response Generation: Tool outputs are aggregated into a coherent response.

### Tools Implemented (tools.py)
| Tool | Function | 
| --- | --- |
| **E-Commerce Search Aggregator** | Searches products across multiple platforms |
| **Shipping Time Estimator** | Provides delivery time and cost estimates |
| **Discount Checker** | Applies discounts and calculates final price |
| **Competitor Price Comparison** | Retrieves price comparisons from multiple stores |
| **Return Policy Checker** | Fetches return policy details for various retailers |

### How to Run the Project
1. Set up the environment
```pip install -r requirements.txt```
2. Run the Agent
To interact with the agent, execute:
```python test_agent.py```
This script runs multiple test cases and prints the agent's responses.

### Example Queries & Responses
**Query: Find a red floral skirt under $40 in size S.**
Agent Response:
```
Searching for: Floral Skirt, Color: Red, Size: S, Max Price: $40
Found a match: Floral Skirt from ShopA for $35.
```

**Query: What is the shipping cost to New York from Zara?**
Agent Response:
```
Shipping to New York: Delivery in 3 days for $5.99.
```

### Challenges & Improvements

#### Challenges Faced:
1. Handling Missing Data: Some queries resulted in No information available due to a lack of mock data.
2. Multi-Step Query Resolution: Combining multiple tool responses effectively was challenging.
3. API Rate Limits & Latency: If deployed with real APIs, handling rate limits would require caching or batching strategies.

#### Future Improvements:
1. Expand the Product Database: Add a larger dataset for better product matching.
2. Implement Parallel Tool Calls: Reduce response latency by handling multiple tool requests simultaneously.
3. Improve Intent Extraction: Enhance query parsing for better accuracy.
4. Integrate Live APIs: Replace mock implementations with real-world API calls for better realism.

### Loom Video Walkthrough
[https://www.loom.com/share/a83201f84c984a8b9a88513ef913ede2?sid=0a8eb256-cdc2-4f8d-a046-a679900b2ba4](https://www.loom.com/share/a83201f84c984a8b9a88513ef913ede2?sid=0a8eb256-cdc2-4f8d-a046-a679900b2ba4)

-----------------------------------------------
Author: Abhishek Kardam

Submission Date: 17.02.2025
